##
## Concept    : Multi-Turn Chatbot Using LangChain and Groq
## What it does: Builds an interactive CLI chatbot that maintains full conversation history
##               across turns using LangChain message types and a Groq-hosted LLM.
## What you'll learn:
##   - How to represent conversation turns with SystemMessage, HumanMessage, and AIMessage
##   - How a growing message list gives the LLM context across multiple turns
##     (same concept as file 5, now using LangChain instead of raw OpenAI SDK)
##   - How ChatGroq wraps a Groq-hosted model behind LangChain's standard LLM interface,
##     making it easy to swap models without changing any other code
## Prerequisite: GROQ_API_KEY must be set in .env (free key at console.groq.com)
## Note: Uses llama-3.3-70b-versatile via Groq API. No OpenAI API key required.
## Run: python 16.langchain_multi_turn_chatbot.py
##
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

messages=[SystemMessage(content="You are a programming expert. Answer questions about programming languages. Keep responses short, concise and to the point.")]

print("Welcome to the Programming Help chatbot. Ask me a question!")
while True:
    user_question = input("You: ")
    if user_question.lower() in ["exit", "quit", "bye", "tata"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    user_message = HumanMessage(content=user_question)

    messages.append(user_message)

    reponse = llm.invoke(messages)
    
    assistant_reply = reponse.content.strip()

    print("Chat Assistant: ", assistant_reply, "\n")

    assistent_message = AIMessage(content=assistant_reply)

    messages.append(assistent_message)

##
## Expected output:
##   Welcome to the Programming Help chatbot. Ask me a question!
##   You: what is a list in python?
##   Chat Assistant: A list in Python is an ordered, mutable collection of items...
##   You: how is it different from a tuple?
##   Chat Assistant: Unlike lists, tuples are immutable — once created, they cannot be changed...
##   You: exit
##   Chatbot: Goodbye! Have a great day!
##
## Challenges:
##   1. Change the system prompt topic from programming to something else (e.g. cooking, history)
##   2. Add a message counter and print how many turns the conversation has had
##   3. Cap the history to the last N messages to avoid hitting token limits on long sessions
##   4. Print the full message history at the end of the session to see how context accumulates
##