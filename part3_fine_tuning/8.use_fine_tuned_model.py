##
## Concept    : Fine-Tuning — Monitoring & Using a Fine-Tuned Model
## What it does: Retrieves the status of a fine-tuning job submitted in file 7, checks if
##               the model is ready, and runs a test inference using the fine-tuned model.
## What you'll learn:
##   - How to monitor a fine-tuning job with client.fine_tuning.jobs.retrieve()
##   - Job statuses: "queued", "running", "succeeded", "failed" — the model is only
##     available under fine_tuned_model once status is "succeeded"
##   - How to use your fine-tuned model exactly like any other model by passing its ID
##     to client.chat.completions.create()
##   - Defensive programming: always guard against None job_id or unfinished jobs
## Prerequisite: Run 7.submit_fine_tuning.py first and wait for the job to complete
## Run: python 8.use_fine_tuned_model.py
##
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# List 10 fine-tuning jobs
print(f"List 10 fine-tuning jobs : {client.fine_tuning.jobs.list(limit=10)}")

job_id = os.getenv("FINE_TUNING_JOB_ID")

if not job_id:
    print("Error: FINE_TUNING_JOB_ID environment variable is not set.")
    exit(1)

res = client.fine_tuning.jobs.retrieve(job_id)

print("Job ID:", res.id)
print("Status:", res.status)
print("Fine Tuned Model:", res.fine_tuned_model)

if not res.fine_tuned_model:
    print("Fine-tuned model is not ready yet. Job status:", res.status)
    exit(0)

completion = client.chat.completions.create(
    model=res.fine_tuned_model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Why is the sky blue?"}
    ]
)

print(completion.choices[0].message.content)

##
## Expected output (if job is still running):
##   List 10 fine-tuning jobs: SyncPage[FineTuningJob](...)
##   Job ID: ftjob-XXXXXXXXXXXXXXXXXXXXXXXX
##   Status: running
##   Fine Tuned Model: None
##   Fine-tuned model is not ready yet. Job status: running
##
## Expected output (if job succeeded):
##   Job ID: ftjob-XXXXXXXXXXXXXXXXXXXXXXXX
##   Status: succeeded
##   Fine Tuned Model: ft:gpt-4.1-mini:personal::XXXXXXXX
##   The sky is blue because of a phenomenon called Rayleigh scattering...
##
## Challenges:
##   1. Ask the fine-tuned model 5 different questions and compare its answers to the base model
##   2. Add a loop that polls the job status every 30 seconds until it's "succeeded" or "failed"
##   3. Test whether your fine-tuned model answers differently on the topic it was trained on
##   4. List all your fine-tuning jobs and print a summary table: ID, status, base model, created date
##