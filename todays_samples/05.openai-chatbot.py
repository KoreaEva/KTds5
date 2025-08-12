import openai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.azure_endpoint = os.getenv("AZURE_ENDPOINT")
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")

# LLM 응답을 가져오는 함수
def get_LLM_response(messages):
    response = openai.chat.completions.create(
                    model="dev-gpt-4.1-mini",
                    messages=messages,
                    max_tokens=1000,
                    temperature=0.7,
    )

    return response.choices[0].message.content

# Streamlit 앱 설정
st.title("Azure OpenAI Chatbot")
st.write("궁금한 것을 물어보세요!")

# 채팅 기록의 초기화
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 채팅 기록의 표시 
for message in st.session_state.messages:
    st.chat_message(message['role']).write(message['content'])

if user_input := st.chat_input("메시지를 입력하세요"):

    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # LLM 응답을 가져오기
    with st.spinner("응답을 기다리는 중..."):
        assistant_response = get_LLM_response(st.session_state.messages)

    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    st.chat_message("assistant").write(assistant_response)