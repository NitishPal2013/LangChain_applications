import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()
API = os.environ["GEMINI_API_KEY"]

from langchain.schema.messages import HumanMessage, SystemMessage

model = ChatGoogleGenerativeAI(model = "gemini-pro", convert_system_message_to_human=True, google_api_key=API)

def get_answer(question, length_of_answer = 30):
    return model([
        SystemMessage(content=f"Answer with in {length_of_answer} words regarding crypto realed queries only."),
        HumanMessage(content=question)
    ])

def welcome():
    print("""
    Welcome, I am Cryptoni, I can answer your questions about Crypto. Feel free to ask me anything
    To end session type "quit".
""", '-'*60)
    
def main():
    welcome()
    question = ""
    while True:
        question = input("You: ")
        if question.lower() == 'quit':
            break
        answer = get_answer(question=question)
        print("Cryptoni: ", answer.content)

if __name__ == '__main__' :
    main()