import os
import openai
from decouple import config

openai.api_key = config("OPENAI_API_KEY")

while True:
    question = input("\033[34mWhat is your question?\n\033[0m")

    if question.lower() == "exit":
        print("\033[31mGoodbye!\n\033[0m")
        break

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
              "role": "system",
              "content": "You are an assistant. Answer the given question."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    print("\033[32m" + completion.choices[0].message.content + "\n")
