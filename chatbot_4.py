from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# 1. This will get infinetly will run untill user types exit

while True:
    user_input = input('YOU:')
    if user_input == 'exit':
        break
    result = model.invoke(user_input)  #this is static prompting
    print('AI:' , result.content)