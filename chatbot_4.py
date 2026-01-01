from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# 1. This will get infinetly will run untill user types exit

# 2.Chat History - so that it can gives us answer based on previous context
#  so we need to maintain the history of the conversation. we'll dfine a list to store the messages.
chat_history = []


while True:
    user_input = input('YOU:')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)  
    chat_history.append(result.content)
    print('AI:' , result.content)

print("Chat History:" , chat_history)  # this gives us the chathistory : -
# Chat History: ['which one is greater 2 or 0', '2 is greater than 0.', 'now multiply this by 10', '2 * 10 = 20.', 'exit']
# this doesnt gives us that which one is by you and which one is by AI.
# so we can improve this by storing the messages as dict with role and content.

# This problem was solved by langChain internally 