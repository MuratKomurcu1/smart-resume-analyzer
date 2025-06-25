import openai
import os
from dotenv import load_dotenv

# .env dosyasının yolunu belirt
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key is None:
    raise ValueError("❌ OPENAI_API_KEY .env dosyasından alınamadı!")
else:
    print("✅ API anahtarı yüklendi:", openai.api_key[:8])


def rewrite_experience(text, role_description):
    prompt = f"Rewrite the following experience for a job as {role_description}:\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']
