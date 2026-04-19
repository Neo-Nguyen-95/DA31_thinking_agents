#%% LIB
from openai import OpenAI
from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END

from dotenv import load_dotenv
import os
load_dotenv()

#%% CONFIG
api_key = os.getenv("OPENAI_API_KEY")
llm_model = "gpt-5-nano"
client = OpenAI()

response = client.responses.create(
    model=llm_model,
    input="Tell a joke"
    )



#%% MAIN
class AgentState(TypedDict):
    message: list
    action: Literal["search", "answer"]
    
def decide_node(state: AgentState):
    messages = state["message"]
    
    prompt = """
    You are a decision-making agent.

    Decide whether the question requires external information.
    
    Use:
    - "search" → if the question depends on up-to-date, specific, or unknown information
    - "answer" → if the question can be answered directly from general knowledge
    
    When unsure, choose "search".
    
    Respond with ONLY one word:
    search or answer
    """
    
    user_question = messages[-1]['content']
    
    action = ...
    
    if action not in {"search", "answer"}:
        action = "search"
        
    return {
        **state,
        "action": action
        }
    
    