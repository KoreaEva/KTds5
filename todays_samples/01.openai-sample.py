import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.azure_endpoint = os.getenv("AZURE_ENDPOINT")
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")

while True:
    question = input("궁금한 것을 물어보세요: (종료하려면 'exit' 입력): ")

    if question.lower() == 'exit':
        print("프로그램을 종료합니다.")
        break

    messages = [
        {"role":"system","content":"You are a helpful assistant."},
        {"role":"user","content": question},
    ]

    response = openai.chat.completions.create(
                    model="dev-gpt-4.1-mini",
                    messages=messages,
                    max_tokens=1000,
                    temperature=0.7,
    )

    print(response.choices[0].message.content)