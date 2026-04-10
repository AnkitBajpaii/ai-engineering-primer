##
## Concept    : Embeddings and Vector Search Using LangChain
## What it does: Creates a set of documents, embeds them using OpenAI's embedding model,
##               stores them in an in-memory vector store, and runs semantic similarity
##               searches to find the most relevant documents for a given query.
## What you'll learn:
##   - The Document abstraction: how LangChain wraps text with page_content and metadata
##   - How OpenAIEmbeddings converts text into high-dimensional vectors that capture meaning
##   - How InMemoryVectorStore indexes those vectors for fast similarity lookup
##   - similarity_search: retrieve the top-k most semantically similar documents to a query
##   - similarity_search_with_score: same as above but also returns the relevance score
##     (lower cosine distance = higher similarity)
##   - Why semantic search beats keyword search: a query about "tomorrow's weather" matches
##     a document about "forecast" even with no words in common
## Prerequisite: OPENAI_API_KEY must be set in .env
## Note: Uses text-embedding-3-large via OpenAI API. Embeddings are computed on every run
##       (in-memory store does not persist). Switch to a persistent store (e.g. ChromaDB,
##       Pinecone) to avoid recomputing on each run.
## Run: python 21.langchain_embedding.py
##
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

# Each Document wraps a piece of text (page_content) with optional metadata.
# metadata can hold anything useful for filtering or display — source URL, author, date, etc.
# id uniquely identifies the document in the vector store.
document_1 = Document(
    page_content="LangChain is a powerful framework for building applications with LLMs.",
    metadata={"source": "langchain-docs"},
    id="doc1",
)

document_2 = Document(
    page_content="The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees.",
    metadata={"source": "news"},
    id="doc2",
)

document_3 = Document(
    page_content="Building an exciting new project with LangChain - come check it out!",
    metadata={"source": "tweet"},
    id="doc3",
)

documents = [document_1, document_2, document_3]

# OpenAIEmbeddings calls the OpenAI API to convert text into vectors.
# text-embedding-3-large produces 3072-dimensional vectors — higher quality than
# text-embedding-3-small (1536-d) but costs more per token.
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# InMemoryVectorStore holds document vectors in RAM.
# add_documents embeds each document's page_content and stores the vector alongside
# the document id and metadata. The document id fields set above are used directly.
vector_store = InMemoryVectorStore(embeddings)
vector_store.add_documents(documents)

query = "What's the weather going to be like tomorrow?"

# similarity_search returns the top-k documents whose embeddings are closest to the
# query embedding. Closeness is measured by cosine similarity — no keyword matching.
print("=== similarity_search (top 1) ===")
results = vector_store.similarity_search(query, k=1)
for doc in results:
    print(f"id      : {doc.id}")
    print(f"source  : {doc.metadata['source']}")
    print(f"content : {doc.page_content}")

print()

# similarity_search_with_score also returns the cosine distance score.
# Lower score = more similar (0.0 = identical, 2.0 = opposite).
print("=== similarity_search_with_score (top 3) ===")
results_with_score = vector_store.similarity_search_with_score(query, k=3)
for doc, score in results_with_score:
    print(f"score: {score:.4f} | source: {doc.metadata['source']} | {doc.page_content[:60]}...")

##
## Expected output:
##   === similarity_search (top 1) ===
##   id      : doc2
##   source  : news
##   content : The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees.
##
##   === similarity_search_with_score (top 3) ===
##   score: 0.1842 | source: news   | The weather forecast for tomorrow is cloudy and overcast...
##   score: 0.6731 | source: tweet  | Building an exciting new project with LangChain - come ...
##   score: 0.7205 | source: langchain-docs | LangChain is a powerful framework for building ...
##
## Challenges:
##   1. Change the query to "What is LangChain?" and observe which document ranks first
##   2. Add a fourth document and run both queries — see how rankings shift
##   3. Filter results by metadata: after similarity_search, filter the returned list to
##      only show documents where doc.metadata["source"] == "news"
##   4. Switch the model from text-embedding-3-large to text-embedding-3-small and compare
##      the scores — notice if the ranking order changes
##   5. Replace InMemoryVectorStore with ChromaDB (see file 15) so embeddings persist
##      across runs and are not recomputed every time
##
