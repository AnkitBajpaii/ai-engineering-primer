# Part 1 — OpenAI API Basics

Learn how to make your first API calls, inspect model metadata, and build a multi-turn chatbot using the OpenAI SDK.

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
# From the repo root
make run n=1
make run n=5
```
