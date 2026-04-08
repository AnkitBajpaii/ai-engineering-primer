##
## Concept    : Completion Metadata, JSON Mode & Seed for Reproducibility
## What it does: Makes a chat completion request asking for a Python code snippet returned
##               as JSON, then prints detailed metadata about the response.
## What you'll learn:
##   - How to use response_format={"type": "json_object"} to get structured JSON output
##   - The seed parameter — setting it makes responses deterministic/reproducible
##   - How to inspect usage stats: prompt_tokens, completion_tokens, total_tokens
##   - finish_reason tells you why the model stopped (e.g. "stop" vs "length")
##   - system_fingerprint identifies the exact model configuration used
## Run: python 3.print_completion_stats.py
##
from openai import OpenAI
from dotenv import load_dotenv

def print_stats(completion_obj):
    print(f"Completion Stats below:")
    print(f"Completion ID: {completion_obj.id}")
    print(f"Model used: {completion_obj.model}")
    print(f"Total tokens: {completion_obj.usage.total_tokens}")
    print(f"Prompt tokens: {completion_obj.usage.prompt_tokens}")
    print(f"Completion tokens: {completion_obj.usage.completion_tokens}")
    print(f"Finish reason: {completion_obj.choices[0].finish_reason}")
    print(f"System fingerprint: {completion_obj.system_fingerprint}")

load_dotenv()

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4.1-mini",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "You are a helpful coding assistant that solves coding problems and provides code snippets in python."},
        {"role": "user", "content": "Write a python function that takes a list of numbers as input and returns the sum of all the even numbers in the list. Please provide only the code snippet in your response with no explanations as JSON"}
    ],
    seed=1234)

print(completion.choices[0].message.content)

print_stats(completion)

##
## Expected output (approximate — JSON and IDs will vary):
##   {"code": "def sum_even_numbers(numbers):\n    return sum(n for n in numbers if n % 2 == 0)"}
##
##   Completion Stats below:
##   Completion ID: chatcmpl-XXXXXXXXXXXXXXXXXXXXXXXX
##   Model used: gpt-4.1-mini-2025-04-14
##   Total tokens: 71
##   Prompt tokens: 49
##   Completion tokens: 22
##   Finish reason: stop
##   System fingerprint: fp_XXXXXXXXXX
##
## Challenges:
##   1. Run the script twice with the same seed=1234 — the code snippet should be identical
##   2. Change seed to a different number and observe whether the output changes
##   3. Remove response_format and observe the model now wraps the code in markdown fences
##   4. Ask for a different function and compare the token counts — longer code = more tokens
##