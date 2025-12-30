# 3 or more drop downs to take user inputs for different aspects of the research paper summary.
# And will going to use dynamic prompt and put the inputs in the prompt template and get the response from the model. And this doesnt hallucinate as we are giving specific instructions to the model in the prompt.
# DYNAMIC PROMPTING - we should prepare a template with placeholders for user inputs.

# But the code is too big so we will break it into like that template creation part and main app part.

import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv

# 1. Setup Environment
load_dotenv()

# 2. Initialize the Model
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

st.header("Research Tools")

# 3. UI Inputs
paper_input = st.selectbox("Select Research Paper Name", [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers", 
    "GPT-3: Language Models are Few-Shot Learners", 
    "Diffusion Models Beat GANs on Image Synthesis"
])

style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

# 4. Define the Template
template = load_prompt('template.json')

# 5. Execute using .invoke()
if st.button('Submit'):
    # We pass the dictionary directly to template.invoke()
    # This returns a PromptValue object
    prompt_value = template.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })
    
    # We pass the PromptValue object directly to the model
    response = llm.invoke(prompt_value)
    
    # Display the result
    st.subheader("Paper Summary")
    st.write(response.content)