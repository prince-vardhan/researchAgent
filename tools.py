from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

search = DuckDuckGoSearchRun()
searchTools = Tool(
    name = "searchWeb",
    func = search.run,
    description = "TO BE USED ONLY WHEN GOOGLE DATABASE INFORMATION IS NOT SUFFICIENT. search the web for the required subject"
)