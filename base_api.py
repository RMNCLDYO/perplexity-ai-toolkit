import os
import time
import json
import requests
from loading import Loading

class BaseAPI:
    def __init__(self, api_key=None, stream=False):
        self.api_key = api_key
        self.stream = stream

        self.base_url = "https://api.perplexity.ai/"

    def get_headers(self):
        headers = {
            "authorization": f"Bearer {self.api_key}",
            "accept": "application/json",
            "content-type": "application/json"
        }
        if self.stream:
            headers["content-type"] = "text/event-stream"
        return headers

    def post(self, endpoint, payload):
        self.api_key = self.api_key if self.api_key else self.get_api_key()
        headers = self.get_headers()
        headers["content-type"] = "application/json"
        try:
            if self.stream:
                full_response = []
                session = requests.Session()
                response = session.post(f"{self.base_url}{endpoint}", headers=headers, data=json.dumps(payload), stream=True)
                data_dict = {}
                print("Assistant: ", end="", flush=True)
                for line in response.iter_lines():
                    if line:
                        json_data = line.decode('utf-8').split('data: ')[1]
                        data_dict = json.loads(json_data)
                        print(data_dict['choices'][0]['delta']['content'], end="", flush=True)
                        full_response.append(data_dict['choices'][0]['delta']['content'])
                print()
                return ''.join(full_response)
            else:
                loading = Loading()
                loading.start()
                try:
                    response = requests.post(f"{self.base_url}{endpoint}", headers=headers, json=payload)
                    response.raise_for_status()
                    response = response.json()
                    if response:
                        loading.stop()
                        if response['choices'][0]['message']['role'] == "assistant":
                            print("Assistant:", response['choices'][0]['message']['content'].strip())
                            return(response['choices'][0]['message']['content'])
                    else:
                        print("No response or an error occurred.")
                except requests.RequestException as e:
                    raise ValueError(f"\nError communicating with API: {e}")
        except requests.RequestException as e:
            raise ValueError(f"\nError communicating with API: {e}")

    @staticmethod
    def get_api_key():
        api_key = os.getenv('API_KEY')
        if not api_key:
            from dotenv import load_dotenv
            load_dotenv()
            api_key = os.getenv('API_KEY')
            if not api_key:
                raise ValueError("\nAPI key not found. Please provide your API key via the --api_key command line option, via the api_key parameter in the class, or set it as an environment variable on your system, or include it in a .env file.")
        return api_key
