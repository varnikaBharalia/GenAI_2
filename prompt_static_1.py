# Normal Reserch tool in this we are having a simple input box to enter the prompt and get the response from the model.
# Disadvantage: No structured prompt, no specific instructions to the model.So the model doesnt give answer in the desired format.
# Also the out wholly depnend on the input prompt if two person asking for the msame thing but there is chnage in prompts and any error then the output will be different.

import os
import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
# FIX 1: Import the message schema
from langchain_core.messages import HumanMessage

os.environ["HF_HOME"] = "D:/huggingface_cache"

# Note: This will reload the model on every click unless st.cache_resource is used
llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 1024, "return_full_text": False},
)

model = ChatHuggingFace(llm=llm)

st.header("Research tools")
user_input = st.text_input('Enter your prompt here')

if st.button('Submit'):
    # FIX 2: Wrap user_input in a HumanMessage list
    response = model.invoke([HumanMessage(content=user_input)])
    st.write(response.content)