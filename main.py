import os
import requests
import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv

import pydub
import pydub.playback
import io

def play(bytesData):
    sound = pydub.AudioSegment.from_file_using_temporary_files(io.BytesIO(bytesData))
    pydub.playback.play(sound)
    return
      

def main():
    load_dotenv()

    st.set_page_config(page_title='Ask your CSV')
    st.header("Ask your CSV")

    file = st.file_uploader('upload file', type='csv')
    basePath = os.getenv("GPT_BASE")
    key = os.getenv("OPENAI_API_KEY")

    if file:
        llm = OpenAI(openai_api_key=key, openai_api_base=basePath)
        user_input = st.text_input('Question here:')
        agent = create_csv_agent(llm, file, verbose=True)
        if user_input:
            response = agent.run(user_input)
            if response:
                response_ = requests.post('https://api.pawan.krd/tts', json={'text': response, 'voice': 'adam'})
                audio_data = response_.content

                play(audio_data)

                st.write(response)

if __name__ == "__main__":
    main()
