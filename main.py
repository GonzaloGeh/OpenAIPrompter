from openai import OpenAI

client = OpenAI(api_key='<KEY>')

response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="Que significa soñar con que se te caigan los dientes?"
)
rAsDictionary = response.model_dump()
textResponse = response.choices[0].text
modelUsed = response.model
totalTokensUsed = response.usage.total_tokens
print(textResponse)