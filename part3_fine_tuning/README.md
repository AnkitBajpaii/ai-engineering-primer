# Part 3 — Fine-Tuning

Learn how to prepare a JSONL training dataset, upload it to OpenAI, and submit and use a fine-tuned model.

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