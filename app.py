import google.generativeai as genai
from dotenv import load_dotenv
import os

'''
# Configure the API
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash')

# Generate text
response = model.generate_content("Explain quantum computing in simple terms.")
print(response.text)
'''
