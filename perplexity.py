from client import Client

class Chat:
    def __init__(self):
        self.client = None

    def run(self, api_key=None, model=None, prompt=None, system_prompt=None, stream=None, max_tokens=None, temperature=None, top_p=None, top_k=None, presence_penalty=None, frequency_penalty=None):
        
        self.client = Client(api_key=api_key)
        self.model = model if model else self.client.config.get('base_chat_model')

        conversation_history = []

        if system_prompt:
            conversation_history.append({"role": "system", "content": system_prompt})

        print("Type 'exit' or 'quit' at any time to end the conversation.\n")

        print("Assistant: Hello! How can I assist you today?")
        while True:
            if prompt:
                user_input = prompt.strip()
                print(f"User: {user_input}")
                prompt = None
            else:
                user_input = input("User: ").strip()
                if user_input.lower() in ['exit', 'quit']:
                    print("\nThank you for using the Perplexity AI toolkit. Have a great day!")
                    break

                if not user_input:
                    print("Invalid input detected. Please enter a valid message.")
                    continue

            conversation_history.append({"role": "user", "content": user_input})

            payload = {
                "model": self.model,
                "messages": conversation_history,
                "system_prompt": system_prompt,
                "stream": stream,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "top_p": top_p,
                "top_k": top_k,
                "presence_penalty": presence_penalty,
                "frequency_penalty": frequency_penalty
            }

            data = {k: v for k, v in payload.items() if v is not None}
            
            endpoint = "chat/completions"

            if stream:
                response = self.client.stream_post(endpoint, data)
                assistant_response = response
            else:
                response = self.client.post(endpoint, data)
                assistant_response = response
                print(f"Assistant: {assistant_response}")
            conversation_history.append({"role": "assistant", "content": assistant_response})


class Search:
    def __init__(self):
        self.client = None

    def run(self, api_key=None, model=None, query=None, system_prompt=None, stream=None, max_tokens=None, temperature=None, top_p=None, top_k=None, presence_penalty=None, frequency_penalty=None):
        
        self.client = Client(api_key=api_key)
        self.model = model if model else self.client.config.get('base_search_model')

        if "online" not in self.model:
            print("Error: { Invalid model type }. Please use a search model instead of a chat model.")
            exit(1)

        if not query:
            print("Error: { Invalid input detected }. Please enter a valid search query.")
            exit(1)

        if system_prompt:
            message = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ]
        else:
            message = [{"role": "user", "content": query}]
        
        payload = {
            "model": self.model,
            "messages": message,
            "system_prompt": system_prompt,
            "stream": stream,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
            "presence_penalty": presence_penalty,
            "frequency_penalty": frequency_penalty
        }

        data = {k: v for k, v in payload.items() if v is not None}
        
        endpoint = "chat/completions"

        if stream:
            response = self.client.stream_post(endpoint, data)
            assistant_response = response
        else:
            response = self.client.post(endpoint, data)
            assistant_response = response
            print(f"Assistant: {assistant_response}")

        print("\nThank you for using the Perplexity AI toolkit. Have a great day!")