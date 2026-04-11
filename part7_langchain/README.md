# Part 7 — LangChain & Groq

Learn the LangChain framework: prompt templates, output parsers, multi-turn chat, composing multi-step pipelines with LCEL, tool calling, and vector search.

## Scripts

| # | File | Concept |
|---|------|---------|
| 16 | [16.langchain_multi_turn_chatbot.py](16.langchain_multi_turn_chatbot.py) | Multi-turn chatbot with `SystemMessage`, `HumanMessage`, `AIMessage` |
| 17 | [17.langchain_prompt_template.py](17.langchain_prompt_template.py) | Reusable `PromptTemplate` with multiple input variables |
| 18 | [18.langchain_output_parsers.py](18.langchain_output_parsers.py) | Parse LLM output into `datetime`, `list`, and Pydantic objects |
| 19 | [19.langchain_feedback_processing_system.py](19.langchain_feedback_processing_system.py) | Multi-step LCEL pipeline with sentiment-based routing |
| 20 | [20.langchain_tool_calling.py](20.langchain_tool_calling.py) | Define tools with `@tool`, bind to LLM, manual two-step tool calling flow |
| 21 | [21.langchain_embedding.py](21.langchain_embedding.py) | Embed documents with `OpenAIEmbeddings`, store in `InMemoryVectorStore`, semantic similarity search |

## Prerequisites

- `GROQ_API_KEY` set in `.env` at the repo root (free key at [console.groq.com](https://console.groq.com)) — required for files 16–20
- `OPENAI_API_KEY` set in `.env` at the repo root — required for file 21
- No local model downloads — inference runs on hosted infrastructure

## Run

```bash
make run n=16
make run n=17
make run n=18
make run n=19
make run n=20
make run n=21
```

> For file 18, uncomment individual function calls in `__main__` to run each output parser example separately.

---

## Concepts

### 16. langchain_multi_turn_chatbot.py — Multi-Turn Chatbot

**What it does:** Builds an interactive CLI chatbot that maintains full conversation history across turns using LangChain message types and a Groq-hosted LLM.

**What you'll learn:**

- How to represent conversation turns with `SystemMessage`, `HumanMessage`, and `AIMessage`
- How a growing message list gives the LLM context across multiple turns (same concept as file 5, now using LangChain instead of the raw OpenAI SDK)
- How `ChatGroq` wraps a Groq-hosted model behind LangChain's standard LLM interface, making it easy to swap models without changing any other code

---

### 17. langchain_prompt_template.py — Prompt Templates

**What it does:** Creates a reusable `PromptTemplate` with multiple placeholders and uses it to generate a customised invitation email via a Groq-hosted LLM.

**What you'll learn:**

- How to define a `PromptTemplate` with named input variables using `from_template()`
- How to invoke a template with a dict of values to produce a fully formatted prompt
- How prompt templates separate prompt structure from data, enabling reuse across different inputs without duplicating the prompt string
- How the formatted prompt is passed directly to the LLM via `llm.invoke()`

---

### 18. langchain_output_parsers.py — Output Parsers

**What it does:** Demonstrates four output parsing strategies — datetime, comma-separated list, Pydantic-structured, and structured LLM output — to convert raw LLM text responses into typed Python objects.

**What you'll learn:**

- `DatetimeOutputParser`: parse an LLM text response into a Python `datetime` object
- `CommaSeparatedListOutputParser`: parse an LLM text response into a Python `list`
- `PydanticOutputParser`: use format instructions to coerce LLM output into a Pydantic model
- `with_structured_output`: ask the LLM to return structured JSON directly, bypassing text parsing — the most reliable approach for complex types
- `partial_variables`: bake static format instructions into a `PromptTemplate` at creation time so they don't need to be passed on every invocation

---

### 19. langchain_feedback_processing_system.py — LCEL Feedback Pipeline

**What it does:** Takes raw customer feedback, parses and summarises it, classifies its sentiment, then routes it to the appropriate response chain using LangChain Expression Language (LCEL).

**What you'll learn:**

- How to compose multi-step pipelines with the LCEL pipe operator (`|`): `PromptTemplate | LLM | OutputParser`
- How `RunnableLambda` transforms data between chain steps (e.g. wrapping a string into a dict so the next `PromptTemplate` can consume it by key name)
- How to implement conditional routing: inspect LLM output and return a different chain depending on the result
- `StrOutputParser`: extract plain text from an LLM response object
- How to build a multi-stage pipeline: parse → summarise → classify → route → respond

---

### 20. langchain_tool_calling.py — Tool Calling

**What it does:** Defines a custom tool with the `@tool` decorator, binds it to a Groq-hosted LLM, and demonstrates the two-step manual tool calling flow.

**What you'll learn:**

- How to define a LangChain tool using `@tool` — the docstring becomes the tool description the LLM uses to decide when and how to call it
- How `llm.bind_tools()` makes the LLM aware of available tools without calling them
- The two-step manual tool calling flow: LLM returns `tool_calls` (decision) → you invoke the tool (execution)
- Why `result.content` is empty when the LLM decides to use a tool — the response is the tool call JSON, not a text answer
- The difference between manual tool calling (this file) and agents (a future topic) where the loop is handled automatically

---

### 21. langchain_embedding.py — Embeddings & Vector Search

**What it does:** Creates a set of documents, embeds them using OpenAI's embedding model, stores them in an in-memory vector store, and runs semantic similarity searches to find the most relevant documents for a given query.

**What you'll learn:**

- The `Document` abstraction: how LangChain wraps text with `page_content` and `metadata`
- How `OpenAIEmbeddings` converts text into high-dimensional vectors that capture meaning
- How `InMemoryVectorStore` indexes those vectors for fast similarity lookup
- `similarity_search`: retrieve the top-k most semantically similar documents to a query
- `similarity_search_with_score`: same but also returns the relevance score (lower cosine distance = higher similarity)
- Why semantic search beats keyword search: a query about "tomorrow's weather" matches a document about "forecast" even with no words in common