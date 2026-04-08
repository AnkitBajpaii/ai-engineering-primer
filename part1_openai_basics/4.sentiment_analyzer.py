##
## Concept    : Prompt Engineering & Controlled Output Parsing
## What it does: An interactive CLI sentiment analyzer. The user types any text and the
##               assistant classifies it as positive, negative, or neutral.
## What you'll learn:
##   - How to craft a system prompt that constrains the model to a fixed output format
##   - How to validate and parse the model's response programmatically
##   - The interactive while-loop pattern for building simple CLI AI apps
##   - Using max_tokens to limit response length for single-word answers
## Run: python 4.sentiment_analyzer.py
##
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def analyze_sentiment(text):
    """Analyze sentiment of the given text using OpenAI API"""
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role":"system", "content":f"You are a helpful assistant that analyzes the sentiment of the following text: \"{text}\". Is it positive, negative or neutral? Please answer in one word with no punctuation."}
        ],
        max_tokens=50,
    )
    
    sentiment = response.choices[0].message.content.strip().lower()

    if sentiment not in ["positive", "negative", "neutral"]:
        return "Unable to determine sentiment. Please try again."

    return f"The sentiment of the given text is: {sentiment}"

print("Welcome to the Sentiment Analyzer bot. Enter a text to analyze its sentiment:")
while True:
    text_to_analyze = input()
    if text_to_analyze.lower() in ["exit", "quit", "bye", "tata"]:
        print("Sentiment Analyzer: Goodbye! Have a great day!")
        break
    result = analyze_sentiment(text_to_analyze)
    print(f"Sentiment Analyzer: {result}\n")

##
## Expected output (sample session):
##   Welcome to the Sentiment Analyzer bot. Enter a text to analyze its sentiment:
##   > I love this product, it works great!
##   Sentiment Analyzer: The sentiment of the given text is: positive
##
##   > This is the worst experience I've ever had.
##   Sentiment Analyzer: The sentiment of the given text is: negative
##
##   > The weather today is okay, nothing special.
##   Sentiment Analyzer: The sentiment of the given text is: neutral
##
## Challenges:
##   1. Try a sarcastic sentence like "Oh great, another Monday" — does it get the tone right?
##   2. Extend the output to include "mixed" as a fourth possible sentiment
##   3. Add a confidence score by asking the model to return "positive:0.9" and parse it
##   4. Change max_tokens=50 to max_tokens=1 and see what breaks — then fix it
##

