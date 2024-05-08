from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

KEY = os.getenv("OPENAI_API_KEY")
SEED = int(os.getenv("SEED"))


class API:
    def __init__(self, model="gpt-4"):
        self.client = OpenAI(api_key=KEY)
        self.model = model

    def send_message(self, message):
        self.completion = self.client.chat.completions.create(
            model=self.model, messages=message, seed=SEED
        )

    def get_response(self):
        output = self.completion.choices[0].message.content
        return output
