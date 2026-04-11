# Part 4 — Error Handling & Robustness

Learn how to catch and handle OpenAI API errors gracefully with proper exception ordering and retry logic.

## Scripts

| # | File | Concept |
|---|------|---------|
| 9 | [9.api_error_handling.py](9.api_error_handling.py) | Catch `RateLimitError`, `APIConnectionError`, and `APIError` in the correct order |

## Prerequisites

- `OPENAI_API_KEY` set in `.env` at the repo root

## Run

```bash
make run n=9
```

---

## Concepts

### 9. api_error_handling.py — API Error Handling

**What it does:** Demonstrates how to gracefully catch and handle the three most common OpenAI API errors using Python's try/except blocks.

**What you'll learn:**

- `RateLimitError` (429): You've exceeded your API quota or requests-per-minute limit. Best practice is exponential backoff — wait and retry with increasing delays.
- `APIConnectionError`: A network-level failure (no internet, DNS issue, timeout). Log the error and inform the user to check their connection.
- `APIError`: A catch-all for other server-side errors (500s, unexpected responses).
- IMPORTANT: Exception order matters — always catch specific exceptions BEFORE the general one, otherwise the general handler shadows the specific ones.