##
## Concept    : Tool Calling Using LangChain and Groq
## What it does: Defines a custom tool with the @tool decorator, binds it to a Groq-hosted
##               LLM, and demonstrates the two-step manual tool calling flow: the LLM decides
##               which tool to call and with what arguments, then you execute the tool yourself.
## What you'll learn:
##   - How to define a LangChain tool using the @tool decorator — the docstring becomes
##     the tool description the LLM uses to decide when and how to call it
##   - How llm.bind_tools() makes the LLM aware of available tools without calling them
##   - The two-step manual tool calling flow:
##       1. LLM reads the prompt and returns tool_calls (a decision, not an execution)
##       2. You invoke the tool manually using result.tool_calls[0]["args"]
##   - Why result.content is empty when the LLM decides to use a tool — the model's
##     response is the tool call JSON, not a text answer
##   - The difference between manual tool calling (this file) and agents (a future topic)
##     where the loop between LLM decision and tool execution is handled automatically
## Prerequisite: GROQ_API_KEY must be set in .env (free key at console.groq.com)
## Note: Uses llama-3.1-8b-instant via Groq API. No OpenAI API key required.
## Run: python 20.langchain_tool_calling.py
##
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


# The @tool decorator turns a plain Python function into a LangChain tool.
# The function name becomes the tool name and the docstring becomes the description
# the LLM reads to decide when and how to call it — write it clearly.
#
# return_direct=True (not used here) would bypass the LLM on the return path and
# send the tool's output straight to the user. It is useful in simple pipelines but
# hides the normal flow where the tool result goes back to the LLM for a final response.
@tool("calculate_discount")
def calculate_discount(price: float, discount_percentage: float) -> float:
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percentage (float): The discount percentage (e.g., 20 for 20%).

    Returns:
        float: The final price after the discount is applied.

    Raises:
        ValueError: If the discount is not between 0 and 100.
    """
    if not (0 <= discount_percentage <= 100):
        raise ValueError("Discount must be between 0 and 100")

    return price * (1 - discount_percentage / 100)


llm = ChatGroq(model="llama-3.1-8b-instant")

# Build a name → tool registry from the same list we bind, so the dispatch
# names can't drift from what the LLM is told about. tool.name matches the
# string the LLM returns in tool_call["name"].
tools = [calculate_discount]
tools_by_name = {t.name: t for t in tools}

# bind_tools tells the LLM about the available tools and their signatures.
# The LLM does NOT call them — it only learns what tools exist and what they do.
llm_with_tools = llm.bind_tools(tools)

# When the prompt doesn't require a tool, the LLM responds normally with text.
response = llm_with_tools.invoke("Hello World")
print(f"Content: {response.content}")
print(f"Tool calls: {response.tool_calls}")  # → [] (no tool needed)

print()

# When the prompt requires a calculation, the LLM returns tool_calls instead of content.
# Step 1: LLM decides to use the tool and returns structured args — it does NOT run Python.
result = llm_with_tools.invoke("What is the price of an item that costs $100 after a 20% discount?")
print(f"Content: {result.content}")        # → "" (empty — model chose to call a tool instead)
print(f"Tool calls: {result.tool_calls}")  # → [{"name": "calculate_discount", "args": {...}}]

# Step 2: You execute the tool manually using the args the LLM decided on.
# Look the tool up by name from the registry instead of hard-coding it — this
# is what lets you bind multiple tools and let the LLM pick the right one.
# Looping over tool_calls also handles the case where the LLM requests more
# than one call in a single response.
# In an agent pattern (future topic) this step is handled automatically in a loop.
for tool_call in result.tool_calls:
    selected_tool = tools_by_name[tool_call["name"]]
    output = selected_tool.invoke(tool_call["args"])
    print(f"{tool_call['name']} → {output:.2f}")

##
## Expected output:
##   Content: Hello! How can I assist you today?
##   Tool calls: []
##
##   Content:
##   Tool calls: [{'name': 'calculate_discount', 'args': {'price': 100.0, 'discount_percentage': 20.0}, 'id': '...', 'type': 'tool_call'}]
##   calculate_discount → 80.00
##
## Challenges:
##   1. Add a second tool (e.g. calculate_tax) and bind both to the LLM — observe how the
##      LLM picks the right tool based on the prompt. The dispatch loop already handles
##      this: tools_by_name will pick up the new tool automatically.
##   2. Try a prompt that doesn't need a tool (e.g. "What is the capital of France?") and
##      confirm that tool_calls is empty and content has the answer
##   3. Pass an invalid discount (e.g. 150) and observe the ValueError raised in step 2
##   4. Try a prompt that triggers two tool calls in one response (e.g. "Apply 20% off to
##      $100 and 10% off to $50") and confirm the loop runs both
##
