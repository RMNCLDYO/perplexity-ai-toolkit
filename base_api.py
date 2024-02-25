import os
import sys
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
        loading = Loading()
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
                loading.start()
                response = requests.post(f"{self.base_url}{endpoint}", headers=headers, json=payload)
                if response.ok:
                    response.raise_for_status()
                    response = response.json()
                    if response and response['choices'][0]['message']['role'] == "assistant":
                            loading.stop()
                            print("Assistant:", response['choices'][0]['message']['content'].strip())
                            return(response['choices'][0]['message']['content'])
                    else:
                        print("No response or an error occurred.")
                else:
                    try:
                        error_message = response.json().get('error', {}).get('message', 'An unknown error occurred.')
                    except ValueError:
                        error_message = response.text or 'An unknown error occurred.'
                    raise requests.RequestException(f"- \u001b[33m(Status Code: {response.status_code})\u001b[0m\n\u001b[1m{error_message}\u001b[0m")
        except requests.RequestException as e:
            loading.stop()
            os.system("clear" if os.name == "posix" else "cls")
            print("\u001b[1m\u001b[31m[ ERROR ]\u001b[0m\u001b[0m", e, "\n")
            sys.exit(1)
        finally:
            loading.stop()

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
