from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# 1. Human Messages - mainly the messages that user send to LLM
# 2. AI Messages - mainly the responses that LLM sends back to user
# 3. System Messages - these are the system level instructions that we give to the model to set the behavior of the model.
#   For example, if we want the model to behave like a helpful assistant, we can give the system message as "You are a helpful assistant".
#   These messages help in setting the context for the conversation and guide the model's responses.
#   maily we send these in the begining of the conversation.

# act as our hstory 
messages = [
    SystemMessage(content = "You are a helpful assistant."),
    HumanMessage(content = "Tell me about langchain")
]

result = model.invoke(messages) 

messages.append(AIMessage(content = result.content))
print(messages)     # this gives us the chathistory with roles : -
# list  of messages with roles and also some additional metadata
# [SystemMessage(content='You are a helpful assistant.', additional_kwargs={}), 
#   HumanMessage(content='Tell me about langchain', additional_kwargs={}), 
#   AIMessage(content='LangChain is an open-source framework..', additional_kwargs={}) ]

