# services/llm_client.py
import os
from groq import Groq
import logging

logging.basicConfig(level=logging.INFO)

class LLMClient:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "llama-3.1-8b-instant"  # fast + good quality

    def generate(self, prompt: str, temperature=0.4, max_tokens=1024):
        logging.info("Sending request to Groq")

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )

        return response.choices[0].message.content.strip()
