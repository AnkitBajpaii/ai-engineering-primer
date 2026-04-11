# Part 1 — OpenAI API Basics

Learn how to make your first API calls, inspect model metadata, and build a multi-turn chatbot using the OpenAI SDK.

## Background

An **LLM (Large Language Model)** is a neural network trained on enormous amounts of text. It doesn't retrieve facts from a database — it predicts the most likely next token given everything before it. The OpenAI API gives you access to these models without running any hardware yourself; you send a request and get a response back.

Every request is **stateless** — the model has no memory of previous conversations. That's why you pass the entire conversation history on every call. Managing that history is your responsibility as the developer.

The core building block is the **chat completion**: you send a list of messages and the model generates the next assistant message. There are three message roles: `system` (sets the model's persona and constraints — the model treats this as standing instructions), `user` (the human's input), and `assistant` (the model's previous replies, included to give it context).

**Tokens** are the unit of text the model processes — roughly 3–4 characters each, or about ¾ of a word. You pay per token, and models have a maximum context window (e.g. 128k tokens for GPT-4o). A prompt that grows too large gets truncated or rejected, and costs accumulate fast — understanding tokens early saves you from surprises in production.

## Scripts

| # | File | Concept |
|---|------|---------|
| 1 | [1.hello_world.py](1.hello_world.py) | First API call |
| 2 | [2.model_list.py](2.model_list.py) | List available models |
| 3 | [3.print_completion_stats.py](3.print_completion_stats.py) | Token usage and completion metadata |
| 4 | [4.sentiment_analyzer.py](4.sentiment_analyzer.py) | Prompt engineering — CLI sentiment analyzer |
| 5 | [5.multi_turn_chatbot.py](5.multi_turn_chatbot.py) | Conversation history — multi-turn chatbot |

## Prerequisites

- `OPENAI_API_KEY` set in `.env` at the repo root

## Run

```bash
make run n=1
make run n=5
```

---

## Concepts

### 1. hello_world.py — First OpenAI API Call

**What it does:** Sends a simple chat request to the OpenAI API and prints the response. Uses a system message to set the assistant's role (English-to-Hindi translator) and a user message with the text to translate.

**What you'll learn:**

- How to authenticate with the OpenAI API using an API key from a `.env` file
- The structure of the messages list: system role vs user role
- How to call `client.chat.completions.create()` and read the response
- The difference between the `model` parameter and the `messages` parameter

---

### 2. model_list.py — Exploring Available Models

**What it does:** Fetches and prints all AI models available to your OpenAI API key, sorted by creation date (newest first).

**What you'll learn:**

- How to use `client.models.list()` to discover available models
- The structure of the model list response (model IDs, created timestamps)
- How to convert a Unix timestamp to a readable date with `datetime.fromtimestamp()`
- Useful for knowing which models you have access to before building with them

---

### 3. print_completion_stats.py — Completion Metadata, JSON Mode & Seed

**What it does:** Makes a chat completion request asking for a Python code snippet returned as JSON, then prints detailed metadata about the response.

**What you'll learn:**

- How to use `response_format={"type": "json_object"}` to get structured JSON output
- The `seed` parameter — setting it makes responses deterministic and reproducible
- How to inspect usage stats: `prompt_tokens`, `completion_tokens`, `total_tokens`
- `finish_reason` tells you why the model stopped (e.g. `"stop"` vs `"length"`)
- `system_fingerprint` identifies the exact model configuration used

---

### 4. sentiment_analyzer.py — Prompt Engineering & Controlled Output Parsing

**What it does:** An interactive CLI sentiment analyzer. The user types any text and the assistant classifies it as positive, negative, or neutral.

**What you'll learn:**

- How to craft a system prompt that constrains the model to a fixed output format
- How to validate and parse the model's response programmatically
- The interactive `while`-loop pattern for building simple CLI AI apps
- Using `max_tokens` to limit response length for single-word answers

---

### 5. multi_turn_chatbot.py — Multi-Turn Conversations & Token Tracking

**What it does:** An interactive programming help chatbot that remembers the full conversation history across multiple turns and tracks cumulative token usage.

**What you'll learn:**

- Why conversation history matters: the API is stateless, so you must send all previous messages on every request to give the model context
- How to grow the `messages` list by appending both user and assistant messages each turn
- How token usage accumulates over a long conversation (important for cost awareness)
- Token breakdown per turn: `prompt_tokens` grows as history grows; `completion_tokens` is only the new tokens generated