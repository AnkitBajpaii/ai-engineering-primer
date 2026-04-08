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
