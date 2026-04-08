##
## Concept    : Exploring Available Models
## What it does: Fetches and prints all AI models available to your OpenAI API key.
## What you'll learn:
##   - How to use client.models.list() to discover available models
##   - The structure of the model list response (model IDs, types)
##   - Useful for knowing which models you have access to before building with them
## Run: python 2.model_list.py
##
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

model_list = client.models.list()

print(f"Total models available: {len(model_list.data)}")

for model in model_list.data:
    print(model.id)

##
## Expected output (actual list depends on your API key access):
##   Total models available: 67
##   gpt-4.1-mini
##   gpt-4.1
##   gpt-4o
##   gpt-4o-mini
##   text-embedding-3-small
##   text-embedding-3-large
##   ... (more models)
##
## Challenges:
##   1. Filter and print only models whose ID contains "gpt" using a list comprehension
##   2. Sort the model list alphabetically before printing
##   3. Count how many models are embedding models vs chat models
##   4. Print each model's `created` timestamp alongside its ID to see which are newest
##