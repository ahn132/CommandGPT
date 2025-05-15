# core/parser.py
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate(query: str) -> str:
    response = client.responses.create(
        model="gpt-4.1",
        instructions="Convert the following request into a safe shell command",
        input=query
    )
    return response.output_text