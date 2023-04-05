import openai


def openai_module(question):
    openai.api_key = ""
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"\nHuman:{question}\nAI:",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    return response["choices"][0]["text"]