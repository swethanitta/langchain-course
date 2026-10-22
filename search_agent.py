from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_tavily import TavilyClient

load_dotenv()

tavily = TavilyClient() 

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


llm = ChatOllama(temperature=0, model="llama3.3")
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content = "What is the weather in Tokyo")})
    print(result)


if __name__ == "__main__":
    main()