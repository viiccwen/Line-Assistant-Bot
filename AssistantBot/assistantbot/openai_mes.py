import openai

openai.api_key = ""

def openai_module(question):
    
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=1000,
    temperature=0.5,
    messages=[
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content