from base_api import BaseAPI

class ChatAPI(BaseAPI):
    def chat(self, api_key=None, model="sonar-medium-chat", system_prompt="You are an advanced AI assistant.", max_tokens=None, temperature=None, top_p=None, top_k=None, stream=False, presence_penalty=None, frequency_penalty=None):
        print("------------------------------------------------------------------\n")
        print("                           Perplexity.AI                          \n")
        print("               API Wrapper & Command-line Interface               \n")
        print("                       [v1.1.1] by @rmncldyo                      \n")
        print("------------------------------------------------------------------\n")
        
        self.api_key = api_key
        self.stream = stream
        endpoint = "chat/completions"
        
        self.chat_history = []
        self.chat_history.append({"role": "system", "content": system_prompt})
        print("Assistant: Hello, how can I assist you today?")
        while True:
            user_input = input("User: ")
            if user_input.lower() in ['quit', 'exit']:
                print("\nThank you for using the Perplexity.AI API Wrapper & Command-line Interface. Have a great day!\n")
                break
            self.chat_history.append({"role": "user", "content": user_input})
            payload = self._construct_payload(model, system_prompt, max_tokens, temperature, top_p, top_k, stream, presence_penalty, frequency_penalty)
            response = self.post(endpoint, payload)
            self.chat_history.append({"role": "assistant", "content": response})

    def _construct_payload(self, model, system_prompt, max_tokens, temperature, top_p, top_k, stream, presence_penalty, frequency_penalty):
        payload = {
            "model": model,
            "messages": self.chat_history,
            "system_prompt": system_prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
            "stream": stream,
            "presence_penalty": presence_penalty,
            "frequency_penalty": frequency_penalty
        }
        payload = {k: v for k, v in payload.items() if v is not None}
        return payload
