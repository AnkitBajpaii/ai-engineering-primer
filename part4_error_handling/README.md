# Part 4 — Error Handling & Robustness

Learn how to catch and handle OpenAI API errors gracefully with proper exception ordering and retry logic.

## Background

APIs fail. Networks drop, rate limits get hit, servers return 500s. Production AI code that doesn't handle errors will crash in front of users at the worst possible time.

The OpenAI SDK maps HTTP status codes to typed Python exceptions so you can handle each failure mode differently:

- **`RateLimitError` (HTTP 429):** You've hit your API quota or requests-per-minute ceiling. The correct response is *exponential backoff* — wait a few seconds, retry, wait longer if it fails again. Don't hammer the API in a tight loop.
- **`APIConnectionError`:** A network-level failure — no internet, DNS timeout, connection refused. No point retrying immediately; log the error and tell the user to check their connection.
- **`APIError`:** A catch-all for other server-side errors (500s, unexpected responses). Log it and surface it; these usually resolve on their own.

**Exception order matters** in Python's `except` chain. Python evaluates handlers top-to-bottom and stops at the first match. `RateLimitError` is a subclass of `APIError` — if you put `APIError` first, it catches everything and your specific handlers never run. Always catch the *most specific* exception first, the most *general* last.

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