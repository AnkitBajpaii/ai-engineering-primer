##
## Concept    : API Error Handling
## What it does: Demonstrates how to gracefully catch and handle the three most common
##               OpenAI API errors using Python's try/except blocks.
## What you'll learn:
##   - RateLimitError (429): You've exceeded your API quota or requests-per-minute limit.
##     Best practice is exponential backoff — wait and retry with increasing delays.
##   - APIConnectionError: A network-level failure (no internet, DNS issue, timeout).
##     Log the error and inform the user to check their connection.
##   - APIError: A catch-all for other server-side errors (500s, unexpected responses).
##   - IMPORTANT: Exception order matters — always catch specific exceptions BEFORE the
##     general one, otherwise the general handler shadows the specific ones.
## Run: python 9.api_error_handling.py
##
import openai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

try:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": "This is a test prompt to demonstrate error handling in OpenAI API."}],
        max_tokens=50,
    )    
except openai.RateLimitError as e:
    #Handle rate limit error (we recommend using exponential backoff)
    print(f"OpenAI API request exceeded rate limit: {e}")
    pass
except openai.APIConnectionError as e:
    #Handle connection error here
    print(f"Failed to connect to OpenAI API: {e}")
    pass
except openai.APIError as e:
    #Handle API error here, e.g. retry or log
    print(f"OpenAI API returned an API Error: {e}")
    pass

##
## Expected output (on a successful run — no errors triggered):
##   (no output — the response is caught but not printed in this demo)
##
## To test each error handler, try these modifications:
##   RateLimitError  → set an intentionally wrong/expired API key in .env
##   APIConnectionError → disconnect from the internet and run the script
##   APIError        → pass an invalid model name like model="not-a-real-model"
##
## Challenges:
##   1. Print the successful response when no error occurs (currently silently succeeds)
##   2. Implement exponential backoff for RateLimitError:
##        retry up to 3 times with delays of 1s, 2s, 4s between attempts
##   3. Add logging to a file (errors.log) instead of just printing to the console
##   4. Swap the order of RateLimitError and APIError — run it with a bad key and see
##        which handler fires. This demonstrates why exception order matters.
##