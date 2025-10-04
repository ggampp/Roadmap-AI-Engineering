import os
from dotenv import load_dotenv
import google.generativeai as genai

# Configure your API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('models/gemini-2.5-flash-lite') 

# Make a simple API call
prompt = "Tell me a short story about a brave knight."
response = model.generate_content(prompt)

# Print the response
print(response.text)