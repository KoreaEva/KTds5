import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.azure_endpoint = os.getenv("AZURE_ENDPOINT")
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")

while True:
    subject = input("시의 주제를 입력하세요: (종료하려면 'exit' 입력): ")
    if subject.lower() == 'exit':
        print("프로그램을 종료합니다.")
        break

    content = input("시의 내용을 입력하세요: : ")


    messages = [
        {"role":"system","content":"You are a AI poem generator."},
        {"role":"user","content": "시의 주제는 '" + subject},
        {"role":"user","content": "시의 내용은 '" + content + "' 입니다."},
        {"role":"user","content": "시의 형식은 자유롭게 작성해 주세요."},
    ]

    response = openai.chat.completions.create(
                    model="dev-gpt-4.1-mini",
                    messages=messages,
                    max_tokens=1000,
                    temperature=0.9,
    )

    print(response.choices[0].message.content)