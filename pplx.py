import os
import json
import requests
import argparse

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

class PerplexityAPI:
    def __init__(self, api_key=None, cli_mode=False):
        print("---------------------------------------------------------------------")
        print("\n                            Perplexity.AI                            ")
        print("               API Wrapper & Command-line Interface                \n")
        print("                         [v1.0] by @rmncldyo                         \n")
        print("---------------------------------------------------------------------\n")
        self.api_key = api_key if api_key else os.getenv('API_KEY')
        self._validate_api_key()
        self.base_url = "https://api.perplexity.ai/chat/completions"
        self.chat_history = []
        self.cli_mode = cli_mode

    def _validate_api_key(self):
        if not self.api_key:
            raise ValueError("API key not found. Set the API_KEY environment variable.")
        
    def _cli_input(self, prompt):
        if self.cli_mode:
            return input(prompt)
        return None
    
    def _get_available_models(self):
        try:
            with open('models.json') as json_file:
                models = json.load(json_file)
            return models
        except FileNotFoundError:
            raise FileNotFoundError("Unable to load models.json file.")

    def _validate_input(self, model, user_input, max_tokens, temperature, top_p, top_k, stream, presence_penalty, frequency_penalty):
        if not user_input:
            raise ValueError("User input not found. Check your input and try again.")
        if model not in self._get_available_models():
            raise ValueError("Model not found. Check your input and try again.")
        if max_tokens and (max_tokens > self._get_available_models()[model]['context_length']):
            raise ValueError(f"Max tokens must be a number between 0 and {self._get_available_models()[model]['context_length']}.")
        if temperature and (temperature < 0 or temperature > 2):
            raise ValueError("Temperature must be a number between 0 and 2.")
        if top_p and (top_p < 0 or top_p > 1):
            raise ValueError("Top p must be a number between 0 and 1.")
        if top_k and (top_k < 0 or top_k > 2048):
            raise ValueError("Top k must be a number between 0 and 2048.")
        if stream and stream not in [True, False]:
            raise ValueError("Stream must be a either True or False.")
        if presence_penalty and (presence_penalty < -2.0 or presence_penalty > 2.0):
            raise ValueError("Presence penalty must be a number between -2.0 and 2.0.")
        if frequency_penalty and (frequency_penalty < 0.0 or frequency_penalty > 1.0):
            raise ValueError("Frequency penalty must be a number between 0.0 and 1.0.")
        
    def _make_headers(self, stream=None):
        headers = {
            "authorization": f"Bearer {self.api_key}",
            "accept": "application/json",
            "content-type": "application/json"
        }
        if stream == True:
            headers["content-type"] = "text/event-stream"
        return headers

    def _make_data(self, model, system_prompt, user_input, max_tokens, temperature, top_p, top_k, stream, presence_penalty, frequency_penalty):
        messages = [{"content": system_prompt, "role": "system"}] + self.chat_history
        if user_input:
            messages.append({"content": user_input, "role": "user"})
        data = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
            "stream": stream,
            "presence_penalty": presence_penalty,
            "frequency_penalty": frequency_penalty
        }
        data = { key: value for key, value in data.items() if value is not None }
        return data

    def _make_request(self, model, system_prompt, user_input, max_tokens, temperature, top_p, top_k, stream, presence_penalty, frequency_penalty):
        response = requests.post(self.base_url, headers=self._make_headers(stream), json=self._make_data(model, system_prompt, user_input, max_tokens, temperature, top_p, top_k, stream, presence_penalty, frequency_penalty))
        response.raise_for_status()
        if response.status_code == 200:
            response = response.json()
            return self._parse_response(response)
        elif response.status_code == 422:
            raise Exception("[422] - Validation Error: The API call failed because the request body was invalid.")
        else:
            raise Exception(f"API call failed with status code {response.status_code}.")
    
    def _parse_response(self, response):
        try:
            if response['choices'][0]['message']['role'] == "assistant":
                return response['choices'][0]['message']['content']
            return "The assistant failed to respond"
        except KeyError as e:
            raise KeyError(f"Error while parsing the assistants response: {e}")
        
    def search(self, model="pplx-70b-online", system_prompt="You are an advanced AI assistant.", user_input=None, max_tokens=None, temperature=None, top_p=None, top_k=None, stream=None, presence_penalty=None, frequency_penalty=None):
        print("Ask anything...\n")
        if self.cli_mode:
            user_input = self._cli_input("User: ")
        else:
            user_input = input("User: ")
        self._validate_input(model, user_input, max_tokens, temperature, top_p, top_k, stream, presence_penalty, frequency_penalty)
        response = self._make_request(model, system_prompt, user_input, max_tokens, temperature, top_p, top_k, stream, presence_penalty, frequency_penalty)
        print("Assistant: ", response.strip())
        user_input = input("Do you have another question? (y/n): ")
        if user_input == "y":
            print()
            self.search(model, system_prompt, user_input, max_tokens, temperature, top_p, top_k, stream, presence_penalty, frequency_penalty)
        else:
            print("\nThank you for using the Perplexity.AI API Wrapper & Command-line Interface by @rmncldyo. Have a great day!\n")

    def chat(self, model="pplx-70b-chat", system_prompt="You are an advanced AI chatbot.", user_input=None, max_tokens=None, temperature=None, top_p=None, top_k=None, stream=None, presence_penalty=None, frequency_penalty=None):
        print("Assistant: Hello, how can I assist you today?")
        while True:
            if self.cli_mode:
                user_input = self._cli_input("User: ")
            else:
                user_input = input("User: ")
            if user_input.lower() == 'quit' or user_input.lower() == 'exit':
                print("\nThank you for using the Perplexity.AI API Wrapper & Command-line Interface by @rmncldyo. Have a great day!\n")
                break
            self._validate_input(model, user_input, max_tokens, temperature, top_p, top_k, stream, presence_penalty, frequency_penalty)
            response = self._make_request(model, system_prompt, user_input, max_tokens, temperature, top_p, top_k, stream, presence_penalty, frequency_penalty)
            self.chat_history.append({"content": user_input, "role": "user"})
            if response:
                print("Assistant: ", response.strip())
                self.chat_history.append({"content": response, "role": "assistant"})

def cli_main():
    parser = argparse.ArgumentParser(
                    prog='Perplexity.AI API Wrapper & Command-line Interface (CLI)',
                    description='A simple wrapper and command-line interface for the Perplexity API.',
                    epilog='For more information, visit https://github.com/rmncldyo/perplexity-ai-api-python-wrapper-and-cli')
    
    parser.add_argument('-a',  '--api-key',           type=str,   help='Your Perplexity API key')
    parser.add_argument('-c',  '--chat',                          help='Start a new chat session',          action='store_true')
    parser.add_argument('-s',  '--search',                        help='Start a new search session',        action='store_true')
    parser.add_argument('-st', '--stream',                        help='Enable stream mode',                action='store_true')
    parser.add_argument('-m',  '--model' ,            type=str,   help='Model name',                        default='pplx-70b-chat')
    parser.add_argument('-sp', '--system-prompt',     type=str,   help='System prompt',                     default='You are an advanced AI chatbot.')
    parser.add_argument('-mt', '--max-tokens',        type=int,   help='Maximum number of tokens')
    parser.add_argument('-t',  '--temperature',       type=float, help='Temperature for randomness')
    parser.add_argument('-tp', '--top-p',             type=float, help='Top P for nucleus sampling')
    parser.add_argument('-tk', '--top-k',             type=int,   help='Top K for filtering')
    parser.add_argument('-pp', '--presence-penalty',  type=float, help='Presence penalty value')
    parser.add_argument('-fp', '--frequency-penalty', type=float, help='Frequency penalty value')
    
    args = parser.parse_args()
    api = PerplexityAPI(api_key=args.api_key, cli_mode=True)
    if args.chat:
        api.chat(model=args.model, system_prompt=args.system_prompt, max_tokens=args.max_tokens, 
                 temperature=args.temperature, top_p=args.top_p, top_k=args.top_k, 
                 stream=args.stream, presence_penalty=args.presence_penalty, frequency_penalty=args.frequency_penalty)
    elif args.search:
        api.search(model=args.model, system_prompt=args.system_prompt, max_tokens=args.max_tokens, 
                   temperature=args.temperature, top_p=args.top_p, top_k=args.top_k, 
                   stream=args.stream, presence_penalty=args.presence_penalty, frequency_penalty=args.frequency_penalty)
    else:
        parser.print_help()

if __name__ == "__main__":
    cli_main()