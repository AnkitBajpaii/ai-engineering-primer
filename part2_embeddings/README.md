# Part 2 — Embeddings

Learn how to generate text embeddings with the OpenAI API and compare vectors using different similarity metrics.

## Scripts

| # | File | Concept |
|---|------|---------|
| 6 | [6.embedding_sample.py](6.embedding_sample.py) | Generate embeddings and compute cosine similarity |
| 12 | [12.embedding_similarity.py](12.embedding_similarity.py) | Compare euclidean distance, cosine similarity, and dot product |

> **Note on ordering:** File 12 is studied here alongside file 6 because both cover embeddings and similarity — even though it is numbered after file 11. Study 6 first, then 12.

## Prerequisites

- `OPENAI_API_KEY` set in `.env` at the repo root

## Run

```bash
make run n=6
make run n=12
```
