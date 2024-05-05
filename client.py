import json
import requests
from config import load_config
from loading import Loading

print("------------------------------------------------------------------\n")
print("                      Perplexity AI Toolkit                       \n")     
print("               API Wrapper & Command-line Interface               \n")   
print("                       [v1.2.2] by @rmncldyo                      \n")  
print("------------------------------------------------------------------\n")

class Client:
    def __init__(self, api_key=None):
        self.config = load_config(api_key=api_key)
        self.api_key = api_key if api_key else self.config.get('api_key')
        self.base_url = self.config.get('base_url')
        self.headers = {
            "authorization": f"Bearer {self.api_key}",
            "accept": "application/json",
            "content-type": "application/json"
        }
    
    def post(self, endpoint, data):
        loading = Loading()
        url = f"{self.base_url}/{endpoint}"
        try:
            loading.start()
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            response = response.json()
            loading.stop()
            try:
                if response and response['choices'][0]['message']['role'] == "assistant":
                    return response['choices'][0]['message']['content']
            except:
                return "Error: We encountered an error while retrieving the response. Please try again later."
        except Exception as e:
            loading.stop()
            print(f"HTTP Error: {e}")
            raise
        finally:
            loading.stop()

    def stream_post(self, endpoint, data):
        loading = Loading()
        url = f"{self.base_url}/{endpoint}"
        full_response = []
        try:
            loading.start()
            response = requests.post(url, json=data, headers=self.headers, stream=True)
            response.raise_for_status()
            loading.stop()
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
        except Exception as e:
            loading.stop()
            print(f"Stream HTTP Error: {e}")
            raise
        finally:
            loading.stop()