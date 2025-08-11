import openai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.azure_endpoint = os.getenv("AZURE_ENDPOINT")
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")

st.title("AI 시인 시몬")
st.write("시를 생성해주는 AI 시인 시몬입니다. 주제와 내용을 입력하면 시를 만들어 드립니다.")


subject = st.text_input("시의 주제를 입력하세요: ")
content = st.text_area("시의 내용을 입력하세요: ")

button_click = st.button("시 생성")

if button_click:
    messages = [
        {"role":"system","content":"You are a AI poem generator."},
        {"role":"user","content": "시의 주제는 '" + subject},
        {"role":"user","content": "시의 내용은 '" + content + "' 입니다."},
        {"role":"user","content": "시의 형식은 자유롭게 작성해 주세요."},
    ]

    with st.spinner("Wait for it...", show_time=True):
        response = openai.chat.completions.create(
                        model="dev-gpt-4.1-mini",
                        messages=messages,
                        max_tokens=1000,
                        temperature=0.9,
        )
        
        st.success("Done!")

    st.write(response.choices[0].message.content)