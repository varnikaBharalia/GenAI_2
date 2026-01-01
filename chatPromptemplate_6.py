from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage , HumanMessage

chat_template = ChatPromptTemplate([
    SystemMessage(content="You are a helpful {domain} expert."),
    HumanMessage(content="Explain in simple terms , what is {topic} ?")
])

prompt = chat_template.invoke({
    'domain': 'Cricket',
    'topic': 'Duckworth Lewis Method'
})

print(prompt)

#C:\Users\HP\Desktop\LangChain_prompts>python chatPromptemplate_6.py
# messages=[SystemMessage(content='You are a helpful {domain} expert.', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain in simple terms , what is {topic} ?', additional_kwargs={}, response_metadata={})]
#  --- This is the output that we get here when we run thsi and this is not what we have expcted 
