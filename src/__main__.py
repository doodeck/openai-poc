import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

response = client.completions.create(model="text-davinci-003",
prompt="Here is a simple Python script to test the OpenAI API:",
temperature=0,
max_tokens=1000)

print(response.choices[0].text)
