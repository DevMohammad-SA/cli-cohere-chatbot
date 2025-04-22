import os

from dotenv import load_dotenv

import cohere

# load .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
co = cohere.ClientV2(API_KEY)
print("Connecting to the API...")
system_message = "You are a terminal-based AI assistant for developers and IT professionals with mixed experience levels. Your goal is to assist with server management, software development, and IT troubleshooting. When users asks any question, provide short, concise, plain-text, step-by-step instructions or commands. Avoid using any markdown, special symbols, escape sequences (like backslashes, backtick, square brackets, etc.), or formatting that could clutter the terminal."
developer = "You have been developed by Mohammad Albuainain"
messages = []
messages.append({"role": "system", "content": system_message})
messages.append({"role": "system", "content": developer})
print("""
Welcome to your terminal AI assistant!
Type your prompts below and get isntant answers powered by Cohere.

Pro tips:
- Type '.quit' anytime to exit
- Designed for developers, sysadmins, and curious tinkerers
- Replies are context-aware (threaded conversation)
-----------------------------------------------------------

""")
while True:
    prompt = input("Chat prompt > ")
    if prompt == ".quit":
        break  # exit the loop if user types ".quit"
    else:
        messages.append({"role": "user", "content": prompt})
        response = co.chat(
            model='command-r-plus',
            messages=messages
        )
        messages.append(
            {'role': 'assistant', 'content': response.message.content[0].text})
        last_message = messages[-1]
        print(f"\nResponse: {last_message.get('content')}\n")
