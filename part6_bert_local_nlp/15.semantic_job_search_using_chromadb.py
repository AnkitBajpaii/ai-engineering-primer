##
## Concept    : Semantic Job Search Using ChromaDB Vector Database (Local — No OpenAI API)
## What it does: Loads a CSV of job descriptions, stores them as embeddings in a ChromaDB
##               vector collection, then queries the collection to find semantically similar
##               jobs for a given search query.
## What you'll learn:
##   - How to use ChromaDB as a vector database for semantic search:
##       1. Create a ChromaDB collection with a cosine similarity metric
##       2. Auto-generate embeddings via SentenceTransformerEmbeddingFunction
##       3. Add documents + metadata to the collection in one call
##       4. Query the collection with natural language and retrieve ranked results
##   - How ChromaDB differs from manual BERT search (file 14):
##       - No manual embedding loop — ChromaDB calls the embedding function automatically
##       - No manual cosine_similarity loop — ChromaDB uses an HNSW index for fast search
##       - Scales to millions of documents; file 14's linear scan does not
##   - Why SentenceTransformer needs no text preprocessing:
##       - Unlike raw BERT, it was fine-tuned on full sentences — stop words carry meaning
##   - ChromaDB distance vs similarity: query returns cosine distance (0 = identical),
##     so similarity = 1 - distance
## Prerequisite: job_title_des.csv or job_descriptions.csv must exist in this directory
##              with columns: "Job Title" and "Job Description"
## Note: Downloads ~80MB SentenceTransformer model on first run. No OpenAI API key required.
## Run: python 15.semantic_job_search_using_chromadb.py
##
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
import pandas as pd
from pathlib import Path


def load_dataset():
    script_dir = Path(__file__).resolve().parent
    candidate_files = [
        script_dir / "data" / "job_title_des.csv",
        script_dir / "data" / "job_descriptions.csv",
    ]
    for csv_path in candidate_files:
        if csv_path.exists():
            return pd.read_csv(csv_path)
    raise FileNotFoundError(
        "No dataset CSV found. Expected one of: "
        f"{', '.join(str(p.name) for p in candidate_files)} in {script_dir}"
    )


def build_collection(client, df):
    embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    collection = client.get_or_create_collection(          # fix: create_collection crashes on re-run
        name="job_descriptions",
        embedding_function=embedding_function,
        metadata={"hnsw:space": "cosine"},
    )
    df = df.dropna(subset=["Job Description", "Job Title"]) # fix: drop rows with missing values
    collection.add(
        ids=[str(i) for i in df.index],
        documents=df["Job Description"].tolist(),
        metadatas=[{"title": t} for t in df["Job Title"].tolist()],
    )
    return collection


def find_matching_jobs(collection, query, top_n=3):
    results = collection.query(
        query_texts=[query],
        n_results=top_n,
    )
    for i in range(len(results["ids"][0])):
        title = results["metadatas"][0][i]["title"]
        distance = results["distances"][0][i]
        similarity = 1 - distance  # cosine distance → similarity score
        print(f"Title: {title}, Similarity: {similarity:.2f}")


def main():
    try:
        df = load_dataset()
    except FileNotFoundError as e:
        raise SystemExit(f"Error: {e}")

    client = chromadb.EphemeralClient()  # fix: Client() is deprecated in chromadb 0.4+
    collection = build_collection(client, df)

    find_matching_jobs(collection, "python developer with experience in web development")


if __name__ == "__main__":
    main()

##
## Expected output (titles depend on your CSV data):
##   Title: Django Developer, Similarity: 0.79
##   Title: Django Developer, Similarity: 0.79
##   Title: Django Developer, Similarity: 0.75
##
## Challenges:
##   1. Try different search queries: "machine learning engineer", "data analyst", "devops"
##   2. Add a similarity threshold — only print results where similarity > 0.75
##   3. Include the job description snippet in the output using results["documents"][0][i]
##   4. Compare results with file 14 — run the same query in both scripts and observe
##      whether ChromaDB + SentenceTransformer returns different rankings than BERT
##   5. Switch to chromadb.PersistentClient(path="./chroma_db") so embeddings survive
##      across runs and are not recomputed every time the script is run
##