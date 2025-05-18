# OpenAI Chat Completion 

import os
import openai
from dotenv import load_dotenv

# .envからAPIキーを読み込む
load_dotenv()

def chat(prompt):
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # モデルを指定してChatCompletionを作成
    # ここではgpt-4oを使用
    # モデルは適宜変更してください
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        q = input("質問を入力してください (終了するには 'exit' と入力): ")
        if q.lower() in {"exit","quit"}:
            break
        print("Bot",chat(q))

