# Part 7 — LangChain & Groq

Learn the LangChain framework: prompt templates, output parsers, multi-turn chat, and composing multi-step pipelines with LCEL.

## Scripts

| # | File | Concept |
|---|------|---------|
| 16 | [16.langchain_multi_turn_chatbot.py](16.langchain_multi_turn_chatbot.py) | Multi-turn chatbot with `SystemMessage`, `HumanMessage`, `AIMessage` |
| 17 | [17.langchain_prompt_template.py](17.langchain_prompt_template.py) | Reusable `PromptTemplate` with multiple input variables |
| 18 | [18.langchain_output_parsers.py](18.langchain_output_parsers.py) | Parse LLM output into `datetime`, `list`, and Pydantic objects |
| 19 | [19.langchain_feedback_processing_system.py](19.langchain_feedback_processing_system.py) | Multi-step LCEL pipeline with sentiment-based routing |

## Prerequisites

- `GROQ_API_KEY` set in `.env` at the repo root (free key at [console.groq.com](https://console.groq.com))
- No local model downloads — inference runs on Groq's hosted infrastructure

## Run

```bash
make run n=16
make run n=17
make run n=18
make run n=19
```

> For file 18, uncomment individual function calls in `__main__` to run each output parser example separately.
