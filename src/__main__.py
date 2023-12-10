import openai

openai.api_key = 'your api key'

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Here is a simple Python script to test the OpenAI API:",
  temperature=0,
  max_tokens=1000
)

print(response.choices[0].text)
