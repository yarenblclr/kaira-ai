import requests
from flask import current_app


class AIService:

    @staticmethod
    def cevapla(mesaj):
        api_key = current_app.config["GROQ_API_KEY"]
        business_context = current_app.config["BUSINESS_CONTEXT"]

        if not api_key:
            return (
                "AI servisi henüz yapılandırılmadı. "
                "Lütfen iletişim bilgilerinizi bırakarak "
                "Kaira ekibinden destek alın."
            )

        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "openai/gpt-oss-20b",
            "messages": [
                {
                    "role": "system",
                    "content": business_context
                },
                {
                    "role": "user",
                    "content": mesaj
                }
            ],
            "temperature": 0.4
        }

        try:
            response = requests.post(
                url,
                headers=headers,
                json=data,
                timeout=30
            )

            response.raise_for_status()

            sonuc = response.json()

            return sonuc["choices"][0]["message"]["content"]

        except requests.RequestException as error:
            print("GROQ HATASI:", error)

            return (
                "Şu anda yapay zeka servisine ulaşılamıyor. "
                "Lütfen daha sonra tekrar deneyin."
            )