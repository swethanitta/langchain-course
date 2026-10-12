from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
import os

load_dotenv()

def main():
    print("Hello from langchain-course!")
    information = """
    Bengaluru, also known as Bangalore (its official name until 1 November 2014), is the capital and largest city of the southern Indian state of Karnataka.
    Bengaluru is one of the fastest-growing metropolises in India. As of 2024, the metropolitan area had an estimated GDP of $590.4 billion, and is one of the most productive metro areas of India. The city is a major centre for information technology (IT), and is consistently ranked amongst the world's fastest growing technology hubs. As the largest hub and exporter of IT services in the country, it is regarded as the "Silicon Valley of India". 
    """

    summary_template = """
        Given the information {information} about a place I want you to create:
        1. short summary in 2 bullet points
    """

    summary_prompt_template = PromptTemplate(
       input_variables=["information"], template=summary_template
    )

    #llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    llm = ChatOllama(temperature=0, model="gemma3:270m")

    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
