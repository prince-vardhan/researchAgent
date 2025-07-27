 Agentic Research Assistant
Hey there! This repository is where I've put my first real dive into Agentic AI. It's an intelligent research assistant I built using LangChain and Google Gemini, and it's been pretty cool seeing how Large Language Models (LLMs) can actually use tools to go out and find information themselves, then pull it all together in a neat, structured way.

For me, this feels like a big foundational step in exploring more advanced, autonomous AI agents. I'm really excited about where this journey could go!

✨ Features
Intelligent Query Processing: It tries to understand what you're asking and figures out the best way to get the answers.

Web Search Integration: I hooked it up to DuckDuckGo Search so it can grab real-time info from the web.

Structured Output: All the research summaries come out in a clean, easy-to-read JSON format, thanks to Pydantic.

Agentic Workflow: It uses LangChain's create_tool_calling_agent to dynamically decide when and how to use its tools.

🛠️ Technologies Used
Python: My go-to language for this project.

LangChain: Super helpful framework for building LLM-powered apps and getting agents to work together.

Google Gemini 1.5 Flash: This is the powerful LLM doing the heavy lifting for reasoning and tool-calling.

DuckDuckGo Search API: The engine behind the web searches.

Pydantic: Great for making sure the data it outputs is structured and valid.

python-dotenv: Keeps my API keys safe and out of sight.

📂 Project Structure
.
├── main.py
├── tools.py
├── .env.example
├── requirements.txt
└── README.md

main.py: This is the main script that gets the agent up and running.

tools.py: Where I've defined the external tools, like the searchWeb function, that the agent can use.

.env.example: A little template for setting up your environment variables (like API keys).

requirements.txt: All the Python libraries you'll need to install.

README.md: Well, that's this file you're reading!

🚀 Setup & Installation
Want to try it out? Here’s how to get it running on your machine:

Clone the repository:

git clone https://github.com/your-username/agentic-research-assistant.git
cd agentic-research-assistant

Create a virtual environment (good practice!):

python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Set up your API Key:

Grab your Google Gemini API key from Google AI Studio.

Create a .env file right in the main project directory (where main.py is).

Add your API key to it like this:

GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"

💡 Usage
Ready to ask it something?

Make sure your virtual environment is active.

Run the main.py script:

python main.py

It'll ask you: What is the topic for your research?

Type in your research query, and watch it go! The agent will process it, maybe use the web search tool, and then give you a structured summary.

Example Interaction & Output
What is the topic for your research? Tell me about the current prime minister of India and their political party.

> Entering new AgentExecutor chain...
Thought: The user is asking for information about the current prime minister of India and their political party. This is a factual question that can be answered by searching the web. I should use the `searchWeb` tool.
Action: searchWeb
Action Input: current prime minister of India and their political party
Observation: The current Prime Minister of India is Narendra Modi. He is a member of the Bharatiya Janata Party (BJP). He assumed office on 26 May 2014.
Thought: I have found the current Prime Minister of India and their political party. I can now synthesize this information into the required JSON format.
Final Answer: ```json
{
  "topic": "Current Prime Minister of India and their Political Party",
  "summary": "Narendra Modi is the current Prime Minister of India, serving since May 26, 2014. He is a prominent leader of the Bharatiya Janata Party (BJP), which is one of the two major political parties in India.",
  "authors": [],
  "tools": ["searchWeb"]
}


Finished chain.

📸 Output Example
<img width="1630" height="789" alt="image" src="https://github.com/user-attachments/assets/c4428218-1533-420c-86f0-576410ba5f5e" />


🔮 Future Enhancements
I've got a few ideas brewing for what's next:

More specialized tools: Thinking about adding tools for academic paper searches (like ArXiv), specific databases, or even a calculator.

Memory: It would be cool if the agent could remember previous conversations for multi-turn interactions.

User Interface: A simple web UI (maybe with Streamlit or Flask) could make it much more interactive.

Advanced output parsing: Exploring ways to handle even more complex or nuanced output requirements.

Better Error Handling: Making it more robust when tools fail or the LLM gives unexpected responses.

🤝 Contributing
If you have any ideas for improvements or spot any issues, please feel free to open a pull request or an issue! I'd love to collaborate.
