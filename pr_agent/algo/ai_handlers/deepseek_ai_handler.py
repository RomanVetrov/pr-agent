import requests
from pr_agent.algo.ai_handlers.base_ai_handler import BaseAIHandler

class DeepSeekAIHandler(BaseAIHandler):
    def __init__(self, config):
        super().__init__(config)
        self.api_key = config.get("deepseek_api_key")
        self.api_url = "https://api.deepseek.com/v1/chat/completions"

    def chat(self, messages, functions=None):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        body = {
            "model": "deepseek-chat",
            "messages": messages,
            "temperature": 0.7,
        }

        response = requests.post(self.api_url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]