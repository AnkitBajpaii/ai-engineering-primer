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
