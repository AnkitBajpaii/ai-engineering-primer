# AI Engineering Playground — A Hands-On Learning Path

A structured, step-by-step collection of Python scripts for learning AI engineering — from your first OpenAI API call through embeddings, fine-tuning, BERT-based NLP, and beyond. Each file introduces one focused concept, making this ideal as a personal reference or a guided learning resource for other developers.

---

## What you'll be able to build

By the end of the current learning path you'll have hands-on experience with:

| Skill | File(s) |
| --- | --- |
| Call the OpenAI API and parse responses | 1, 3 |
| Build a CLI sentiment analyzer | 4 |
| Build a multi-turn chatbot with token cost tracking | 5 |
| Generate and compare text embeddings | 6, 12 |
| Fine-tune a model on your own dataset | 7, 8 |
| Handle API errors gracefully with retry logic | 9 |
| Generate content with style-controlled prompts | 10 |
| Build a domain-specific support bot from a knowledge base | 11 |
| Generate BERT embeddings locally (no API key needed) | 13 |
| Build a semantic job search engine | 14 |
| Build a semantic job search engine with a vector database | 15 |
| Build a multi-turn chatbot with LangChain and Groq | 16 |
| Generate dynamic content using LangChain prompt templates | 17 |
| Parse LLM output into typed Python objects | 18 |
| Build a sentiment-routing feedback processing pipeline | 19 |

---

## Roadmap

- [x] **Part 1** — OpenAI API Basics (files 1–5)
- [x] **Part 2** — Embeddings (files 6, 12)
- [x] **Part 3** — Fine-Tuning (files 7–8)
- [x] **Part 4** — Error Handling & Robustness (file 9)
- [x] **Part 5** — Practical Applications (files 10–11)
- [x] **Part 6** — BERT & Local NLP (files 13–15)
- [x] **Part 7** — LangChain & Groq (files 16–19)
- [ ] **Part 8** — Function Calling & Tool Use
- [ ] **Part 9** — Streaming Responses
- [ ] **Part 10** — Structured Output (JSON mode, Pydantic)
- [ ] **Part 11** — Vision & Multimodal (GPT-4o image input)
- [ ] **Part 12** — Retrieval Augmented Generation (RAG with FAISS)
- [ ] **Part 13** — Agents & LangGraph
- [ ] **Part 14** — MCP (Model Context Protocol)

> Star the repo to get notified when new parts drop.

---

## Who this is for

- **Yourself (future reference):** Each script is self-contained. Skim the file header and the code to quickly recall the concept.
- **Other developers:** Follow the numbered files in order — each one introduces one new concept on top of the last.

---

## Prerequisites

- Python 3.9+
- An [OpenAI API key](https://platform.openai.com/api-keys) — required for files 1–11
- A [Groq API key](https://console.groq.com) — required for files 16–19 (free tier available)
- Basic Python knowledge

---

## Setup

**Option A — one command (recommended):**

```bash
git clone https://github.com/AnkitBajpaii/ai-engineering-playground.git
cd ai-engineering-playground
make setup
# Open .env and add your OPENAI_API_KEY, then:
make run n=1
```

**Option B — manual:**

```bash
# 1. Clone the repo
git clone https://github.com/AnkitBajpaii/ai-engineering-playground.git
cd ai-engineering-playground

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your API key
cp .env.example .env
# Open .env and replace the placeholder with your actual OpenAI API key
```

> The `.env` file is loaded automatically by `python-dotenv` in every script. Never commit it to version control — it is listed in `.gitignore`.

### NLTK Data (required for files 13 and 14)

Files 13 and 14 use NLTK corpora that must be downloaded once before running. File 15 does not require NLTK.

```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
```

Run the above in a Python shell after installing requirements, or add it temporarily at the top of the script on first run.

---

## Learning Path

The scripts are numbered in the order they should be studied. Each one introduces a focused concept.

> **Note on ordering:** File 12 (`embedding_similarity.py`) is grouped under Part 2 — Embeddings alongside file 6 because it covers the same conceptual topic (similarity metrics), even though it is numbered after file 11. Study it after file 6 for the best flow.

### Part 1 — OpenAI API Basics

| # | File | Concept | Key Takeaway |
|---|------|---------|--------------|
| 1 | [1.hello_world.py](1.hello_world.py) | First API call | How to call `chat.completions.create`, pass a system + user message, and read the response |
| 2 | [2.model_list.py](2.model_list.py) | Available models | How to list all models available to your API key |
| 3 | [3.print_completion_stats.py](3.print_completion_stats.py) | Completion metadata | Token usage, finish reason, system fingerprint, JSON response format, and the `seed` parameter for reproducibility |
| 4 | [4.sentiment_analyzer.py](4.sentiment_analyzer.py) | Prompt engineering | How to frame a task in the system prompt and parse a controlled single-word response; interactive CLI loop pattern |
| 5 | [5.multi_turn_chatbot.py](5.multi_turn_chatbot.py) | Conversation history | How to maintain a growing message list for multi-turn dialogue; tracking cumulative token usage |

### Part 2 — Embeddings

| # | File | Concept | Key Takeaway |
|---|------|---------|--------------|
| 6 | [6.embedding_sample.py](6.embedding_sample.py) | OpenAI Embeddings API | How to generate embeddings for text pairs and compute cosine similarity using `text-embedding-3-small` |
| 12 | [12.embedding_similarity.py](12.embedding_similarity.py) | Similarity metrics | Manual comparison of euclidean distance, cosine similarity, and dot product on fixed vectors using `scikit-learn` and `numpy` |

### Part 3 — Fine-Tuning

| # | File | Concept | Key Takeaway |
|---|------|---------|--------------|
| 7 | [7.submit_fine_tuning.py](7.submit_fine_tuning.py) | Fine-tuning pipeline | Validating a JSONL training dataset, uploading files via the Files API, and submitting a fine-tuning job |
| 8 | [8.use_fine_tuned_model.py](8.use_fine_tuned_model.py) | Using a fine-tuned model | Retrieving job status, checking if the model is ready, and running inference on the fine-tuned model |

### Part 4 — Error Handling & Robustness

| # | File | Concept | Key Takeaway |
|---|------|---------|--------------|
| 9 | [9.api_error_handling.py](9.api_error_handling.py) | API error handling | Catching `RateLimitError`, `APIConnectionError`, and `APIError` in the correct order (specific before general) |

### Part 5 — Practical Applications

| # | File | Concept | Key Takeaway |
|---|------|---------|--------------|
| 10 | [10.ai_tweet_creator.py](10.ai_tweet_creator.py) | Creative generation | Using the `temperature` parameter to control creativity; style-guided content generation |
| 11 | [11.ai_chat_support_system.py](11.ai_chat_support_system.py) | Domain-specific chatbot | Embedding business knowledge in the system prompt to build a scoped support bot |

### Part 6 — BERT & Local NLP (No OpenAI)

| # | File | Concept | Key Takeaway |
|---|------|---------|--------------|
| 13 | [13.bert_sample.py](13.bert_sample.py) | BERT embeddings | Text preprocessing (tokenization, stop word removal, lemmatization) and generating BERT CLS embeddings using HuggingFace Transformers |
| 14 | [14.find_matching_jobs.py](14.find_matching_jobs.py) | Semantic search | Building a semantic job search engine: pre-computing BERT embeddings for a dataset and ranking results by cosine similarity |
| 15 | [15.semantic_job_search_using_chromadb.py](15.semantic_job_search_using_chromadb.py) | Vector database | Replacing the manual BERT + cosine loop with ChromaDB: auto-embedding via SentenceTransformer, HNSW index for fast search, and metadata-aware querying |

### Part 7 — LangChain & Groq

| # | File | Concept | Key Takeaway |
|---|------|---------|--------------|
| 16 | [16.langchain_multi_turn_chatbot.py](16.langchain_multi_turn_chatbot.py) | Multi-turn chatbot | How to maintain conversation history with `SystemMessage`, `HumanMessage`, `AIMessage` using LangChain + Groq instead of the raw OpenAI SDK |
| 17 | [17.langchain_prompt_template.py](17.langchain_prompt_template.py) | Prompt templates | How `PromptTemplate` separates prompt structure from data — define once, invoke with different inputs |
| 18 | [18.langchain_output_parsers.py](18.langchain_output_parsers.py) | Output parsers | Parsing raw LLM text into typed Python objects: `datetime`, `list`, Pydantic model, and `with_structured_output` |
| 19 | [19.langchain_feedback_processing_system.py](19.langchain_feedback_processing_system.py) | LCEL chains | Composing multi-step pipelines with the `\|` operator and `RunnableLambda`; conditional routing based on LLM-classified sentiment |

---

## Adding a New Script

1. Name it `<next-number>.<short_description>.py` (e.g., `15.function_calling.py`)
2. Add the standard file header at the top (see convention below)
3. Add a row for it in the appropriate section of this README table

### Standard file header convention

Every script should start with a comment block in this format — matching the style used across all existing files:

```python
##
## Concept    : <one-line concept name, e.g., "Function Calling">
## What it does: <one or two sentences describing what the script demonstrates>
## What you'll learn:
##   - <key lesson 1>
##   - <key lesson 2>
##   - <key lesson 3>
## Prerequisite: <any files to run first, or data files needed — omit if none>
## Note: <any important runtime notes, e.g., model downloads — omit if none>
## Run: python <filename>.py
##
```

This makes it easy to understand any file at a glance without opening the full README.

---

## Project Structure

```
.
├── .env                        # Your API keys — never commit this
├── .env.example                # Safe template — commit this, fill in .env from it
├── .gitignore                  # Excludes .env, .venv/, __pycache__, IDE folders
├── requirements.txt            # All dependencies
├── README.md                   # This file
├── 1.hello_world.py
├── 2.model_list.py
├── 3.print_completion_stats.py
├── 4.sentiment_analyzer.py
├── 5.multi_turn_chatbot.py
├── 6.embedding_sample.py
├── 7.submit_fine_tuning.py
├── 8.use_fine_tuned_model.py
├── 9.api_error_handling.py
├── 10.ai_tweet_creator.py
├── 11.ai_chat_support_system.py
├── 12.embedding_similarity.py
├── 13.bert_sample.py                          # Requires: NLTK downloads, transformers, torch
├── 14.find_matching_jobs.py                   # Requires: job_title_des.csv or job_descriptions.csv
├── 15.semantic_job_search_using_chromadb.py   # Requires: job_title_des.csv or job_descriptions.csv
├── 16.langchain_multi_turn_chatbot.py         # Requires: GROQ_API_KEY in .env
├── 17.langchain_prompt_template.py            # Requires: GROQ_API_KEY in .env
├── 18.langchain_output_parsers.py             # Requires: GROQ_API_KEY in .env
├── 19.langchain_feedback_processing_system.py # Requires: GROQ_API_KEY in .env
├── training_set.jsonl          # Required for file 7 (fine-tuning) — not included
└── validation_set.jsonl        # Required for file 7 (fine-tuning) — not included
```

---

## Dependencies

See [requirements.txt](requirements.txt) for the full list. Key packages:

| Package | Used for |
|---------|----------|
| `openai` | OpenAI API (files 1–11) |
| `openai[datalib]` | Extra OpenAI utilities (numpy integration for embeddings) |
| `python-dotenv` | Loading `.env` API keys |
| `numpy` | Vector math for embeddings |
| `pandas` | Loading CSV datasets (file 14) |
| `scikit-learn` | Cosine similarity, euclidean distance (files 12, 14) |
| `nltk` | Tokenization, stop words, lemmatization (files 13, 14) |
| `transformers` | BERT tokenizer and model (files 13, 14) |
| `torch` | PyTorch backend for BERT inference (files 13, 14) |
| `chromadb` | Vector database for storing and querying embeddings (file 15) |
| `sentence-transformers` | Lightweight sentence embedding model via ChromaDB (file 15) |
| `langchain` | Core LangChain framework — chains, prompts, message types (files 16–19) |
| `langchain-core` | Base abstractions — `PromptTemplate`, `StrOutputParser`, `RunnableLambda` (files 16–19) |
| `langchain-groq` | `ChatGroq` integration for Groq-hosted LLMs (files 16–19) |
| `langchain-community` | Third-party output parsers and integrations (file 18) |
| `langchain-classic` | Legacy output parsers — `DatetimeOutputParser`, `PydanticOutputParser` (file 18) |

---

## Notes

- Files 13, 14, and 15 do **not** use the OpenAI API — they demonstrate local NLP using open-source models. First run downloads ~440MB for BERT (files 13–14) or ~80MB for SentenceTransformer (file 15).
- Files 13 and 14 require NLTK data to be downloaded first — see the [NLTK Data](#nltk-data-required-for-files-13-and-14) section above. File 15 does not require NLTK.
- Files 14 and 15 require a CSV file (`job_title_des.csv` or `job_descriptions.csv`) with columns `Job Title` and `Job Description`.
- File 15 uses `chromadb.EphemeralClient()` — the collection is in-memory and is rebuilt on every run. To persist embeddings across runs, switch to `chromadb.PersistentClient(path="./chroma_db")`.
- Files 16–19 use the **Groq API** instead of OpenAI — get a free key at [console.groq.com](https://console.groq.com). Add `GROQ_API_KEY=your_key` to your `.env` file.
- Files 16–19 do not require any local model downloads — inference runs on Groq's hosted infrastructure.
- Files 7 and 8 require `training_set.jsonl` and `validation_set.jsonl` for fine-tuning. These are not included in the repo as they are user-specific training data.
- Files 7 and 8 are meant to be run in sequence. File 7 sets `FINE_TUNING_JOB_ID` in the current process environment. If you run file 8 in a new terminal session, add `FINE_TUNING_JOB_ID=<your-job-id>` to your `.env` file manually so it persists.
