import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Check available models for your account
models = client.models.list()
print("Available models in your Groq account:")
for m in models.data:
    print("-", m.id)