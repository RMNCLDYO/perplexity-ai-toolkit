from base_api import BaseAPI

class SearchAPI(BaseAPI):
    def search(self, api_key=None, model="sonar-medium-online", query=None, system_prompt=None, max_tokens=None, temperature=None, top_p=None, top_k=None, stream=False, presence_penalty=None, frequency_penalty=None):
        print("------------------------------------------------------------------\n")
        print("                           Perplexity.AI                          \n")
        print("               API Wrapper & Command-line Interface               \n")
        print("                       [v1.1.1] by @rmncldyo                      \n")
        print("------------------------------------------------------------------\n")
        
        self.api_key = api_key
        self.stream = stream
        endpoint = "chat/completions"
        payload = self._construct_payload(model, query, system_prompt, max_tokens, temperature, top_p, top_k, stream, presence_penalty, frequency_penalty)
        print("User:", query)
        self.post(endpoint, payload)
        print()

    def _construct_payload(self, model, query, system_prompt, max_tokens, temperature, top_p, top_k, stream, presence_penalty, frequency_penalty):
        messages = [{"role": "system", "content": system_prompt}] if system_prompt else []
        messages.append({"role": "user", "content": query})
        payload = {
            "model": model,
            "messages": messages,
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
