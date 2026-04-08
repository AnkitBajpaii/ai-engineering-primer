##
## Concept    : Output Parsers Using LangChain
## What it does: Demonstrates four output parsing strategies — datetime, comma-separated list,
##               Pydantic-structured, and structured LLM output — to convert raw LLM text
##               responses into typed Python objects.
## What you'll learn:
##   - DatetimeOutputParser: parse an LLM text response into a Python datetime object
##   - CommaSeparatedListOutputParser: parse an LLM text response into a Python list
##   - PydanticOutputParser: use format instructions to coerce LLM output into a Pydantic model
##   - with_structured_output: ask the LLM to return structured JSON directly,
##     bypassing text parsing entirely — the most reliable approach for complex types
##   - partial_variables: bake static format instructions into a PromptTemplate at creation
##     time so they don't need to be passed on every invocation
## Prerequisite: GROQ_API_KEY must be set in .env (free key at console.groq.com)
## Note: Uncomment individual function calls in __main__ to run each example separately.
##       Uses meta-llama/llama-4-scout-17b-16e-instruct via Groq API.
## Run: python 18.langchain_output_parsers.py
##
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import DatetimeOutputParser, CommaSeparatedListOutputParser, PydanticOutputParser
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

def DateOutputParserExample():
    parser = DatetimeOutputParser()

    prompt_template = PromptTemplate.from_template(
      template="Answer the question.\n{format_instructions}\n{question}",
      partial_variables={"format_instructions": parser.get_format_instructions()},
      )

    prompt_value = prompt_template.invoke({"question": "When was iphone released?"})
    response = llm.invoke(prompt_value)
    print("Raw LLM response:", response.content)

    returned_object = parser.parse(response.content)
    print(type(returned_object))

def CommaSeparatedListOutputParserExample():
    parser = CommaSeparatedListOutputParser()
    prompt_template = PromptTemplate.from_template(
      template="Answer the question.\n{format_instructions}\n{question}",
      partial_variables={"format_instructions": parser.get_format_instructions()},
      )
    
    prompt_value = prompt_template.invoke({"question": "Name 5 programming languages."})
    response = llm.invoke(prompt_value)
    print("Raw LLM response:", response.content)

    returned_object = parser.parse(response.content)
    print(type(returned_object))

def PydanticOutputParserExample():
    
    class Author(BaseModel):
        name : str = Field(description="Name of the author")
        number : int = Field(description="Number of books written by the author")
        books : list[str] = Field(description="List of book titles written by the author")

    parser = PydanticOutputParser(pydantic_object=Author)

    prompt_pydantic = PromptTemplate.from_template(
      template="Answer the question.\n{format_instructions}\n{question}",
      partial_variables={"format_instructions": parser.get_format_instructions()},
      )

    prompt_value = prompt_pydantic.invoke({"question": "Generate the books written by James Clear"})

    response = llm.invoke(prompt_value)

    print("Raw LLM response:", response.content)

    returned_object = parser.parse(response.content)
    print(f"{returned_object.name} wrote {returned_object.number} books.")
    print(returned_object.books)

def StructuredLlmExample():
    class Author(BaseModel):
      name: str = Field(description="The name of the author as a string.")
      number: int = Field(description="The number of books as an INTEGER, not a string.")
      books: list[str] = Field(description="A JSON ARRAY of book titles (strings). Do NOT return a stringified array.")

    structured_llm = llm.with_structured_output(Author)

    # A tiny nudge in the prompt helps many models obey types without extra code.
    returned_object = structured_llm.invoke(
        "Generate the books written by James Clear."
        "Return 'number' as an integer (not a string) and 'books' as a JSON array of strings (not a quoted string)."
    )

    print(f"{returned_object.name} wrote {returned_object.number} books.")
    print(returned_object.books)

if __name__ == "__main__":

    DateOutputParserExample()

    # CommaSeparatedListOutputParserExample()

    # PydanticOutputParserExample()

    #StructuredLlmExample()

##
## Expected output (DateOutputParserExample):
##   Raw LLM response: 2007-01-09T00:00:00.000000Z
##   <class 'datetime.datetime'>
##
## Expected output (CommaSeparatedListOutputParserExample):
##   Raw LLM response: Python, JavaScript, Java, C++, Go
##   <class 'list'>
##
## Expected output (PydanticOutputParserExample / StructuredLlmExample):
##   James Clear wrote 2 books.
##   ['Atomic Habits', 'Ego is the Enemy']
##
## Challenges:
##   1. Uncomment and run each of the four examples to compare their outputs
##   2. Add a new Pydantic model (e.g. Movie with title, year, genre) and parse an LLM response
##   3. Compare PydanticOutputParserExample vs StructuredLlmExample — notice which is more
##      reliable for returning correct types (int vs str, list vs quoted string)
##   4. Try DatetimeOutputParser with a vague question like "When did the Roman Empire fall?"
##      and observe how the LLM and parser handle ambiguous dates
##