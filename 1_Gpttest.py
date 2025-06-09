import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key = os.getenv('API_KEY')
)

response = client.chat.completions.create(
    model='gpt-4.1-2025-04-14',
    messages=[
        {"role":'user', 'content':'인기 많은 중세 판타지 웹툰, 혹은 무협웹툰 추천해줘. 100회 이상 나온것으로'}
    ],
    temperature=0.1
)

print(response.choices[0].message.content)