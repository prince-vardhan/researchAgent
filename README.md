🤖 Agentic Research Assistant
This repository hosts my initial dive into Agentic AI, featuring an intelligent research assistant built with LangChain and Google Gemini. This project demonstrates how Large Language Models (LLMs) can be empowered with tools to autonomously gather and synthesize information from the web, delivering structured results.

It's a foundational step in my journey to explore more sophisticated autonomous AI agents.

✨ Features
Intelligent Query Processing: Understands research questions and determines the best course of action.

Web Search Integration: Utilizes DuckDuckGo Search to fetch real-time information.

Structured Output: Delivers research summaries in a clean, parseable JSON format using Pydantic.

Agentic Workflow: Employs LangChain's create_tool_calling_agent for dynamic tool invocation and reasoning.

🛠️ Technologies Used
Python: The core programming language.

LangChain: Framework for building LLM-powered applications and agent orchestration.

Google Gemini 1.5 Flash: The powerful LLM providing reasoning and tool-calling capabilities via langchain-google-genai.

DuckDuckGo Search API: For performing web searches (langchain-community).

Pydantic: For defining and validating structured data outputs.

python-dotenv: For secure management of API keys.

📂 Project Structure
.
├── main.py
├── tools.py
├── .env.example
├── requirements.txt
└── README.md

main.py: The main application script that initializes and runs the agent.

tools.py: Defines the external tools (e.g., searchWeb) that the agent can use.

.env.example: A template for environment variables (API keys).

requirements.txt: Lists all Python dependencies.

README.md: This file.

🚀 Setup & Installation
Follow these steps to get the project up and running on your local machine.

Clone the repository:

git clone https://github.com/your-username/agentic-research-assistant.git
cd agentic-research-assistant

(Remember to replace your-username with your actual GitHub username)

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Set up your API Key:

Create a .env file in the root directory of the project (same level as main.py).

Get your Google Gemini API key from Google AI Studio.

Add your API key to the .env file:

GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"

(Replace YOUR_GEMINI_API_KEY_HERE with your actual key)

💡 Usage
To run the agent and start your research:

Ensure your virtual environment is active.

Run the main.py script:

python main.py

The script will prompt you: What is the topic for your research?

Enter your research query, and the agent will process it, potentially using the web search tool, and return a structured summary.

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


## 📸 Output Example

*(You would replace this section with a screenshot of your actual terminal output, similar to the one above, showing the agent's verbose chain and the final parsed JSON output.)*

## 🔮 Future Enhancements

* **Add more specialized tools:** Integrate tools for academic paper search (e.g., ArXiv), specific databases, or calculators.
* **Implement memory:** Allow the agent to retain conversational history for multi-turn interactions.
* **User Interface:** Develop a simple web UI (e.g., using Streamlit or Flask) for a more interactive experience.
* **Advanced output parsing:** Handle more complex or nuanced output requirements.
* **Error Handling:** Implement more robust error handling for tool failures or unexpected LLM responses.

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements or find any issues, feel free to open a pull request or an issue.
