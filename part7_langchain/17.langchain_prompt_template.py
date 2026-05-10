##
## Concept    : Prompt Templates Using LangChain
## What it does: Creates a reusable PromptTemplate with multiple placeholders and uses it
##               to generate a customised invitation email via a Groq-hosted LLM.
## What you'll learn:
##   - How to define a PromptTemplate with named input variables using from_template()
##   - How to invoke a template with a dict of values to produce a fully formatted prompt
##   - How prompt templates separate prompt structure from data, enabling reuse across
##     different inputs without duplicating the prompt string
##   - How the formatted prompt is passed directly to the LLM via llm.invoke()
## Prerequisite: GROQ_API_KEY must be set in .env (free key at console.groq.com)
## Note: Uses meta-llama/llama-4-scout-17b-16e-instruct via Groq API. No OpenAI key required.
## Run: python 17.langchain_prompt_template.py
##

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

email_template = PromptTemplate.from_template("Create an invitation email to the recipient that is {recipient_name}\
for an event that is {event_type}\
in a language that is {language}\
Mention the event location that is {event_location}\
and event date that is {event_date}.\
Also write few sentences about the event description that is {event_description}\
in style that is {style}.")

details = {
  "recipient_name":"John",
  "event_type":"product launch",
  "language": "American english",
  "event_location":"Grand Ballroom, City Center Hotel",
  "event_date":"11 AM, January 15, 2024",
  "event_description":"an exciting unveiling of our latest GenAI product",
  "style":"enthusiastic tone"
}

prompt_value = email_template.invoke(details)

response = llm.invoke(prompt_value)

print(response.content)

##
## Expected output (content will vary per run):
##   Subject: You're Invited to Our Exclusive Product Launch!
##   Dear John,
##   We are thrilled to invite you to an exciting unveiling of our latest GenAI product...
##   Join us at the Grand Ballroom, City Center Hotel on January 15, 2024 at 11 AM...
##
## Challenges:
##   1. Change the style from "enthusiastic tone" to "formal" or "humorous" and compare outputs
##   2. Add a new placeholder {dress_code} to the template and pass a value for it
##   3. Create a second template for a different use case — e.g. a job offer letter or meeting invite
##   4. Invoke the same template twice with different details dicts and compare the two emails
##