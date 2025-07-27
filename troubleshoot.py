import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI


load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
print(f"Loaded Google API Key: {'*' * len(google_api_key) if google_api_key else 'None'}") # Prints stars for security
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables. Please check your .env file.")

# ... rest of your code using google_api_key
llm = GoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=google_api_key)