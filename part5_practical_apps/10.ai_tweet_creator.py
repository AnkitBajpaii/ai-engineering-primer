##
## Concept    : Creative Generation & the Temperature Parameter
## What it does: Generates a new tweet in the style of a set of sample tweets by passing
##               the samples as context to the model.
## What you'll learn:
##   - The temperature parameter controls creativity/randomness:
##       0.0 = deterministic and focused, 1.0 = creative and varied, >1.0 = chaotic
##   - How to use few-shot style prompting: giving examples in the prompt so the model
##     learns the desired tone and format without explicit instructions
##   - max_tokens limits response length — useful for short-form content like tweets
##   - How to wrap API calls in reusable functions with configurable parameters
## Run: python 10.ai_tweet_creator.py
##
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

recent_tweets = """
Tweet 1: Just had an amazing coffee at the new cafe in town!
Tweet 2: Exploring the wonders of AI - it's more accessible than ever before.
Tweet 3: Coding late into the night. The life of a developer.
"""

def generate_tweet(style_sample, temperature=0.7, max_tokens=50):
    messages = [
        {"role": "system", "content": "You are a creative assistant that generates tweets in the style of the provided samples."},
        {"role": "user", "content": f"Write a creative tweet based on the following style: {style_sample}"}
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",        
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature
    )

    tweet = response.choices[0].message.content.strip()

    return tweet
    
new_tweet = generate_tweet(recent_tweets)

print("Generated Tweet:", new_tweet)

##
## Expected output (exact tweet will vary due to temperature):
##   Generated Tweet: Fueling creativity with coffee and code — the perfect duo for a dev's day! ☕💻
##
## Challenges:
##   1. Generate 5 tweets with temperature=0.2 and 5 with temperature=1.5 — compare the results
##   2. Add a `topic` parameter to generate_tweet() so callers can say "write a tweet about AI"
##   3. Add a `require_hashtags=True` parameter that appends an instruction to include hashtags
##   4. Replace recent_tweets with tweets in a different style (formal, technical, funny)
##      and see how the model adapts
##