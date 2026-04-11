# Part 6 — BERT & Local NLP (No OpenAI)

Learn how to generate embeddings and build a semantic search engine locally using open-source models — no API key required.

## Scripts

| # | File | Concept |
|---|------|---------|
| 13 | [13.bert_sample.py](13.bert_sample.py) | Text preprocessing and BERT CLS embeddings via HuggingFace |
| 14 | [14.find_matching_jobs.py](14.find_matching_jobs.py) | Semantic job search with manual BERT embeddings + cosine similarity |
| 15 | [15.semantic_job_search_using_chromadb.py](15.semantic_job_search_using_chromadb.py) | Semantic job search using ChromaDB vector database |

## Prerequisites

- No API key required
- Dataset CSV in `data/job_title_des.csv` with columns `Job Title` and `Job Description` (included)
- NLTK corpora downloaded once (files 13 and 14 only):

```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
```

## Notes

- First run downloads ~440MB for BERT (files 13–14) or ~80MB for SentenceTransformer (file 15)
- File 15 does not require NLTK

## Run

```bash
make run n=13
make run n=14
make run n=15
```

---

## Concepts

### 13. bert_sample.py — NLP Text Preprocessing & BERT Embeddings

**What it does:** Preprocesses two sentences using classic NLP techniques (tokenization, stop word removal, lemmatization), then generates BERT embeddings for each using HuggingFace Transformers and PyTorch.

**What you'll learn:**

- Text preprocessing pipeline: tokenization → stop word removal → lemmatization
- How BERT tokenizes text differently from simple word splitting (wordpiece tokenization)
- The CLS token: BERT adds a special `[CLS]` token at the start of every input — its embedding from the last hidden layer represents the entire sequence
- `torch.no_grad()`: disables gradient computation during inference to save memory

---

### 14. find_matching_jobs.py — Semantic Job Search with BERT

**What it does:** Loads a CSV of job descriptions, preprocesses the text, generates BERT embeddings for each job, then ranks jobs by semantic similarity to a query.

**What you'll learn:**

- End-to-end semantic search pipeline: load & preprocess → embed all documents → embed query → rank by cosine similarity
- Performance optimization: pre-compute all job embeddings once at startup so each search query only requires one embedding call, not N calls
- Truncation in BERT tokenization: BERT has a 512-token limit — long descriptions must be truncated to avoid index errors
- How semantic search differs from keyword search: a query for "python developer" can match "software engineer" if the embeddings are close

---

### 15. semantic_job_search_using_chromadb.py — Semantic Job Search with ChromaDB

**What it does:** Loads a CSV of job descriptions, stores them as embeddings in a ChromaDB vector collection, then queries the collection to find semantically similar jobs for a given search query.

**What you'll learn:**

- How to use ChromaDB as a vector database: create a collection, auto-generate embeddings via `SentenceTransformerEmbeddingFunction`, add documents with metadata, and query with natural language
- How ChromaDB differs from the manual BERT approach in file 14: no manual embedding loop, no manual cosine similarity loop, scales to millions of documents via HNSW index
- Why SentenceTransformer needs no text preprocessing: unlike raw BERT, it was fine-tuned on full sentences — stop words carry meaning
- ChromaDB distance vs similarity: query returns cosine distance (0 = identical), so similarity = 1 − distance