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
