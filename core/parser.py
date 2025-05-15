# core/parser.py
from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate(query: str) -> str:
    response = client.responses.create(
        model="gpt-4.1",

        input=(
            "You are a helpful assistant that safely converts natural language instructions "
            "into command-line commands. Your goal is to generate correct, safe, and minimal shell commands, "
            "and clearly explain what they do in plain English. Always return your answer as JSON with exactly"
            " two fields: 'command' and 'explanation'. Do not include anything else. "
            "The user's request is {query}"),
    )
    
    json_response = json.loads(response.output_text)
    #print(json_response)
    return json_response['command'], json_response['explanation']