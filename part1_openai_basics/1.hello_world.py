##
## Concept    : First OpenAI API Call — Chat Completions
## What it does: Sends a simple chat request to the OpenAI API and prints the response.
##               Uses a system message to set the assistant's role (English-to-Hindi translator)
##               and a user message with the text to translate.
## What you'll learn:
##   - How to authenticate with the OpenAI API using an API key from a .env file
##   - The structure of the messages list: system role vs user role
##   - How to call client.chat.completions.create() and read the response
##   - The difference between the model parameter and the messages parameter
## Run: python 1.hello_world.py
##
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

client = OpenAI()

messages = [
    {"role" : "system", "content" : "You are a helpful assistant that translates English to Hindi."},
    {"role" : "user", "content" : "Translate the following English text to Hindi: 'Hello, how are you?'"}
]

model="gpt-4.1-mini"

completion = client.chat.completions.create(
    model=model,
    messages=messages
)

print(completion.choices[0].message.content)

##
## Expected output (exact wording varies):
##   नमस्ते, आप कैसे हैं?
##
## Challenges:
##   1. Change the target language to French, Spanish, or Japanese — just update the system prompt
##   2. Translate multiple sentences by changing the user message to a paragraph
##   3. Remove the system message entirely and see how the model responds differently
##   4. Add a second user message asking it to now translate the Hindi back to English
##