1. Prompts are the input instrn or queries given to a model to guide its output.

2. Prompts are of two types :-
        a) Text based :- text - query
        b) Multimodel :- sound/image/video-query 

3. Prompts are also wo types :-
        a) Static prompts:- User writes there prompts everytime,hallicuanation may occur in this. Response depends on the prompt 
        b) Dynamic prompts:- Ideally we want a consisitent response so that we can get a very good output . ALready we are given an template just we need to give key - value for the output . 

4. flow: - write your prompt -> fetched -> llm-> gives output

5. To get the consistent output we should prepare a template 
        eg: 
            Please summarize the research paper titled "{paper_input}" with the following
            specifications:
            Explanation Style: {style_input}
            Explanation Length: {length_input}
            1. Mathematical Details:
            - Include relevant mathematical equations if present in the paper.
            - Explain the mathematical concepts using simple, intuitive code snippets
            where applicable.
            2. Analogies:
            - Use relatable analogies to simplify complex ideas.
            If certain information is not available in the paper, respond with: "Insufficient
            information available" instead of guessing.
            Ensure the summary is clear, accurate, and aligned with the provided style and
            length

6. A PromptTemplate in LangChain is a structured way to create prompts
    dynamically by inserting variables into a predefined template. Instead of hardcoding prompts, PromptTemplate allows you to define placeholders that can be filled in at runtime with different input. This makes it reusable, flexible, and easy to manage, especially when working with dynamic user inputs or automated workflows.

7. Why we dont use fstring ? and we used prompt template class ?
    Why use PromptTemplate over f strings?
        
        1) Default validation --> validate_template= true -- then we'll get a error in this and tell us that kuch etra ya km is there in the input_variavles that are not present in the prompt_template --> also this will give error in the devlepoment time not on the run time .

        2) Reusable --> template can be saved as a json file and can be called as per that so it is reuseable . prompt_generator3.py

        3) LangChain Ecosystem --> We are invoking 2 time in the last code after if so to reduce the invoke calling we can do that create a chain.  chain= template | model 
                chain.invoke({
                    dict..
                })
        4) CONCULSION : While f-strings are useful for simple scripts, PromptTemplate provides a production-grade framework. It ensures my Research Tool remains stable through input validation, stays organized via JSON-based modularity, and remains fully compatible with advanced LangChain features like LCEL and structured output parsing

8. Creating a Chatbot - console based chatbot , not ui .
    this chatbot is not stoing history. 