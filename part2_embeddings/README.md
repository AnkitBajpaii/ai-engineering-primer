# Part 2 — Embeddings

Learn how to generate text embeddings with the OpenAI API and compare vectors using different similarity metrics.

## Background

Text is strings — but math works on numbers. An **embedding** converts a piece of text into a fixed-length array of floating-point numbers (a *vector*) that captures its meaning. Words or phrases with similar meanings end up as vectors that point in similar directions in high-dimensional space — "dog" and "puppy" will be close; "dog" and "invoice" will be far apart.

This numeric representation unlocks powerful capabilities that pure string matching can't do: you can measure how similar two pieces of text are, find documents that match a query even with no words in common, cluster related content, and power recommendation systems — all using basic linear algebra.

**Cosine similarity** is the standard metric for comparing text embeddings. It measures the *angle* between two vectors, not the distance between their tips. A score of `1.0` means the vectors point in exactly the same direction (same meaning); `0.0` means perpendicular (unrelated). Cosine is preferred over raw euclidean distance because longer documents produce larger vectors — cosine normalises that out, so a short tweet and a long article on the same topic still score as similar.

The embeddings in this folder come from OpenAI's `text-embedding-3-small` model, which maps any text input into a 1536-dimensional vector. You never see or manipulate those 1536 numbers directly — you just compare them.

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

---

## Concepts

### 6. embedding_sample.py — Text Embeddings & Cosine Similarity

**What it does:** Generates vector embeddings for pairs of words/phrases using OpenAI's `text-embedding-3-small` model, then computes cosine similarity to measure how semantically related each pair is.

**What you'll learn:**

- What embeddings are: fixed-size numerical vectors that represent the meaning of text
- How to call `client.embeddings.create()` and extract the embedding vectors
- How cosine similarity works: a score of 1.0 = identical meaning, 0.0 = unrelated
- Why "mango shake" and "mango" score higher similarity than "phone" and "car"
- The foundation for semantic search, clustering, and recommendation systems

---

### 12. embedding_similarity.py — Similarity Metrics

**What it does:** Computes three different mathematical similarity/distance measures between two fixed 3-dimensional vectors, demonstrating how each metric behaves.

**What you'll learn:**

- **Euclidean distance:** straight-line distance between two points in vector space — lower = more similar, sensitive to vector magnitude
- **Cosine similarity:** measures the angle between two vectors, not their magnitude — ranges from -1 to 1, higher = more similar, most common metric for text embeddings
- **Dot product:** related to cosine similarity but also influenced by vector magnitude — used in many neural network attention mechanisms
- Why cosine similarity is preferred for text: two documents with the same words but different lengths should still be "similar" — cosine handles this, euclidean doesn't

> This file uses fixed vectors (no API call) — great for understanding the math in isolation.