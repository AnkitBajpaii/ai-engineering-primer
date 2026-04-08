##
## Concept    : Feedback Processing System Using LangChain LCEL
## What it does: Takes raw customer feedback, parses and summarises it, classifies its
##               sentiment, then routes it to the appropriate response chain (thank-you,
##               apology, or request-for-details) using LangChain Expression Language (LCEL).
## What you'll learn:
##   - How to compose multi-step pipelines with the LCEL pipe operator (|):
##       PromptTemplate | LLM | OutputParser
##   - How RunnableLambda transforms data between chain steps (e.g. wrapping a string
##     into a dict so the next PromptTemplate can consume it by key name)
##   - How to implement conditional routing: inspect LLM output and return a different
##     chain depending on the result (positive → thankyou_chain, negative → apology_chain)
##   - StrOutputParser: extract plain text from an LLM response object
##   - How to build a multi-stage pipeline: parse → summarise → classify → route → respond
## Prerequisite: GROQ_API_KEY must be set in .env (free key at console.groq.com)
## Note: Uses meta-llama/llama-4-scout-17b-16e-instruct via Groq API. No OpenAI key required.
## Run: python 19.langchain_feedback_processing_system.py
##
from dotenv import load_dotenv
from langchain_classic.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

thankyou_template = PromptTemplate.from_template(template = "Given the feedback, draft a thank you message for the user and request them to leave a positive rating on our webpage:\n\n{feedback}")
thankyou_chain = thankyou_template | llm | StrOutputParser()

details_template = PromptTemplate.from_template(template = "Given the feedback, draft a message for the user and request them provide more details about their concern:\n\n{feedback}")
details_chain = details_template | llm | StrOutputParser()

apology_template = PromptTemplate.from_template(template = "Given the feedback, draft an apology message for the user and mention that their concern has been forwarded to the relevant department:\n\n{feedback}")
apology_chain = apology_template | llm | StrOutputParser()

def route(info):
    if "positive" in info['sentiment'].lower():
        return thankyou_chain
    elif "negative" in info['sentiment'].lower():
        return apology_chain
    else:
        return details_chain
    
user_feedback = "The delivery was late, and the product was damaged when it arrived. However, the customer support team was very helpful in resolving the issue quickly."

parse_template = PromptTemplate.from_template(template = "Parse and clean the following customer feedback for key information:\n\n{raw_feedback}")

format_parsed_output = RunnableLambda(lambda output: {"parsed_feedback" : output})
summary_template = PromptTemplate.from_template(template = "Summarize the following customer feedback in one sentence:\n\n{parsed_feedback}")

summary_chain = parse_template | llm | format_parsed_output | summary_template | llm | StrOutputParser()

summary = summary_chain.invoke({"raw_feedback": user_feedback})

sentiment_template = PromptTemplate.from_template(template = "Determine the sentiment of the following feedback and reply in one word as either 'Positive', 'Negative', or 'Neutral': :\n\n{feedback}")

sentiment_chain = sentiment_template | llm | StrOutputParser()

sentiment =  sentiment_chain.invoke({"feedback": summary})

print(f"The summary of the user's message is: {summary}\n")

print(f"The sentiment was classifed as: {sentiment}\n")

full_chain =  RunnableLambda(lambda x: {"feedback" : x['feedback'], "sentiment": x['sentiment']}) | RunnableLambda(route)

print(full_chain.invoke({"feedback" : summary , "sentiment": sentiment}))

##
## Expected output (content will vary per run):
##   The summary of the user's message is: The customer experienced a late delivery and
##   damaged product, but praised the support team for resolving the issue quickly.
##
##   The sentiment was classified as: Neutral
##
##   Thank you for sharing your experience with us! We're sorry to hear about the delivery
##   and packaging issues, but we're glad our support team could help resolve things quickly...
##
## Challenges:
##   1. Change user_feedback to a clearly positive or negative message and observe how the
##      route() function picks a different chain each time
##   2. Add a fourth sentiment branch (e.g. "Mixed") and a corresponding response chain
##   3. Print the intermediate summary and sentiment between pipeline steps to trace the data flow
##   4. Replace the hardcoded user_feedback with input() to process live feedback interactively
##