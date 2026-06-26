from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from groq import Groq

# Load variables from .env
load_dotenv()
app = FastAPI()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

# Store conversation history
messages = []

class ChatRequest(BaseModel):
    message:str
    temperature: float = 0.7
    model: str = "llama-3.3-70b-versatile"

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Save user's message
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Request streaming response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        stream=True
    )

    print("Bot: ", end="")

    # Will store the complete assistant response
    assistant_response = ""
    
    # Process chunks as they arrive
    for chunk in response:
        piece = chunk.choices[0].delta.content

        if piece is not None:
            print(piece, end="", flush=True)
            assistant_response += piece

    print()  # Move to next line after response is complete

    # Save assistant's complete response
    messages.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )


@app.post("/chat")
def chat(request: ChatRequest):
    response = client.chat.completions.create(
        messages = [
            {
                "role": "user",
                "content": request.message
            }
        ],
        temperature=request.temperature,
        model=request.model
    )
    ans = response.choices[0].message.content
    return {
        "answer":ans
    }
