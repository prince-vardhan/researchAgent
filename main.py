from dotenv import load_dotenv
from pydantic import BaseModel
from google import genai
import os
from google.genai import types 
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import searchTools

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    authors: list[str]
    tools: list[str]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))
parser = PydanticOutputParser(pydantic_object = ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a very skillful researcher that is there to help college students with their research papers. 
                You will use the necessary tools and also mention the articles that you refer and their author's in the author list.
                You will follow the format instructions and no other text should be present in the answer.\n{format_instructions}
                """,
        ),
        ("placeholder","{chat_history}" ),
        ("human","{query}"),
        ("placeholder","{agent_scratchpad}")
    ]
).partial(format_instructions = parser.get_format_instructions())
tools = [searchTools]
agent = create_tool_calling_agent(
    llm = llm,
    prompt = prompt,
    tools = tools
)
agent_executor = AgentExecutor(agent=agent,tools=tools,verbose = True)
query = input("What is the topic for your research?")
rawResponse = agent_executor.invoke({"query":query})

structuredResponse = parser.parse(rawResponse["output"])
print(structuredResponse)


