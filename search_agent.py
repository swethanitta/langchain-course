from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
#from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()

class Source(BaseModel):
    """Schema for a source used by the agent"""

    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer:str = Field(description="The Agnet answer to the query")
    sources:List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")

#tavily = TavilyClient() 
'''
@tool
def search(query: str) -> str:
    """
    Tool that search over internet
    Args:
        query: The query to search for
    return:
         The search result
    """
    print(f"Searching for {query}")
    #return "Tokyo weather is sunny"
    return tavily.search(query=query)
'''
# cmd 7, 11, 12 to 24 : This is the custom tool call with Tavily SDK


llm = ChatOllama(temperature=0, model="llama3.3")
#tools = [search]
tools = [TavilySearch()]
#agent = create_agent(model=llm, tools=tools)
agent = create_agent(model=llm, tools=tools,response_format=AgentResponse)


def main():
    print("Hello from langchain-course!")
    #result = agent.invoke({"messages": HumanMessage(content = "What is the weather in Tokyo")})
    result = agent.invoke({"messages": HumanMessage(content = "Search for 3 job posting for an AI Enginner in Banglore location in Linkedin and return the details")})
    print(result)


if __name__ == "__main__":
    main()