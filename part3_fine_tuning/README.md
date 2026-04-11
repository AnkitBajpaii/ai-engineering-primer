# Part 3 — Fine-Tuning

Learn how to prepare a JSONL training dataset, upload it to OpenAI, and submit and use a fine-tuned model.

## Background

A pre-trained LLM is a generalist — it can do almost anything but excels at nothing specific. **Fine-tuning** takes that base model and continues training it on your own curated examples, nudging the model's weights toward the style, format, or domain expertise you need.

Think of it as the difference between hiring a new graduate (base model) and training them on how your company specifically writes customer emails (fine-tuned model). After fine-tuning, the model produces your format consistently without needing long instructions in every prompt — the behaviour is baked in.

**Fine-tuning is not always the right tool.** It is expensive to set up (training costs money and time), the dataset must be carefully prepared, and you can't update the model's knowledge after training is complete. For most tasks, a well-crafted system prompt gets you 80% of the way there in minutes. Consider fine-tuning when:

- You need very consistent output format and prompting alone isn't reliable enough
- Your prompts are getting very long because you keep repeating the same instructions
- Latency or cost of long prompts is a bottleneck in production

The training data format is **JSONL** — one JSON object per line, each containing a `messages` array with `system`, `user`, and `assistant` turns representing an ideal example interaction.

## Scripts

| # | File | Concept |
|---|------|---------|
| 7 | [7.submit_fine_tuning.py](7.submit_fine_tuning.py) | Validate dataset, upload files, submit fine-tuning job |
| 8 | [8.use_fine_tuned_model.py](8.use_fine_tuned_model.py) | Check job status and run inference on the fine-tuned model |

## Prerequisites

- `OPENAI_API_KEY` set in `.env` at the repo root
- `training_set.jsonl` and `validation_set.jsonl` in this directory (not included — create your own)

Each line in the JSONL files must follow this format:

```json
{"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
```

## Run

Run file 7 first, then file 8. They must be run in sequence.

```bash
make run n=7
make run n=8
```

> If you run file 8 in a new terminal session, add `FINE_TUNING_JOB_ID=<your-job-id>` to your `.env` file so it persists across sessions.

---

## Concepts

### 7. submit_fine_tuning.py — Data Validation & Job Submission

**What it does:** Validates the format of training and validation JSONL datasets, uploads them using the OpenAI Files API, and submits a fine-tuning job.

**What you'll learn:**

- The required JSONL format for fine-tuning data: each line must be a JSON object with a `"messages"` key containing a list of role/content pairs
- How to programmatically validate your dataset for common formatting errors before submitting (missing keys, wrong roles, empty content, etc.)
- How to upload files with `client.files.create(purpose="fine-tune")`
- How to submit a fine-tuning job with `client.fine_tuning.jobs.create()`
- The job ID is saved to an env variable so file 8 can retrieve the trained model

---

### 8. use_fine_tuned_model.py — Monitoring & Using a Fine-Tuned Model

**What it does:** Retrieves the status of a fine-tuning job submitted in file 7, checks if the model is ready, and runs a test inference using the fine-tuned model.

**What you'll learn:**

- How to monitor a fine-tuning job with `client.fine_tuning.jobs.retrieve()`
- Job statuses: `"queued"`, `"running"`, `"succeeded"`, `"failed"` — the model is only available once status is `"succeeded"`
- How to use your fine-tuned model exactly like any other model by passing its ID to `client.chat.completions.create()`
- Defensive programming: always guard against `None` job ID or unfinished jobs