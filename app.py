import os
import requests
import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv

      
def main():
    load_dotenv()

    st.set_page_config(page_title='Ask your CSV')
    st.header("Ask your CSV")

    file = st.file_uploader('upload file', type='csv')
    # basePath = os.getenv("GPT_BASE")
    # key = os.getenv("OPENAI_API_KEY")

    if file:
        llm = OpenAI(temperature=0)
        user_input = st.text_input('Question here:')

        agent = create_csv_agent(llm, file, verbose=True)
        if user_input:
            response = agent.run(user_input)
            st.write(response)


if __name__ == "__main__":
    main()
