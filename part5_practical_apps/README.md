# Part 5 — Practical Applications

Build real-world tools: a style-controlled content generator and a domain-specific support chatbot.

## Scripts

| # | File | Concept |
|---|------|---------|
| 10 | [10.ai_tweet_creator.py](10.ai_tweet_creator.py) | Temperature-controlled creative content generation |
| 11 | [11.ai_chat_support_system.py](11.ai_chat_support_system.py) | Domain-specific chatbot scoped with a system prompt |

## Prerequisites

- `OPENAI_API_KEY` set in `.env` at the repo root

## Run

```bash
make run n=10
make run n=11
```

---

## Concepts

### 10. ai_tweet_creator.py — Creative Generation & the Temperature Parameter

**What it does:** Generates a new tweet in the style of a set of sample tweets by passing the samples as context to the model.

**What you'll learn:**

- The `temperature` parameter controls creativity/randomness: `0.0` = deterministic and focused, `1.0` = creative and varied, `>1.0` = chaotic
- How to use few-shot style prompting: giving examples in the prompt so the model learns the desired tone and format without explicit instructions
- `max_tokens` limits response length — useful for short-form content like tweets
- How to wrap API calls in reusable functions with configurable parameters

---

### 11. ai_chat_support_system.py — Domain-Specific Chatbot

**What it does:** Builds a customer support chatbot for a shoe store by embedding the store's FAQ knowledge base directly into the system prompt.

**What you'll learn:**

- How to use the system message as a knowledge base to scope the chatbot's expertise
- This is a lightweight alternative to fine-tuning for domain-specific Q&A — no training needed, just well-structured context in the prompt
- The `temperature` parameter at `0.5` balances consistency with natural-sounding replies
- How to structure a chatbot with a `main()` entry point and a helper function, keeping the API logic separate from the conversation loop
- Fallback handling: when the model can't answer, redirect users to human support