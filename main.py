from dotenv import load_dotenv
import os
from groq import Groq


load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key = api_key)

messages = []

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Who are you?"
        }
    ]
)
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":user_input
            }
        ]
    )

    answer = response.choices[0].message.content

    print("Bot:", answer)

    messages.append({"role":"user", "content": user_input})
    