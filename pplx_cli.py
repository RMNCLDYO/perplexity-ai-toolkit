import argparse
from pplx_chat import ChatAPI
from pplx_search import SearchAPI

def main():
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('-a', '--api_key', type=str, help='Your Perplexity API key')

    parser = argparse.ArgumentParser(prog='Perplexity AI Wrapper & Command-line Interface (CLI)',
                                    description='A wrapper and command-line interface for the Perplexity AI API.',
                                    epilog='For more information, visit https://github.com/rmncldyo/perplexity-ai-wrapper-and-cli')

    subparsers = parser.add_subparsers(dest='command', required=True, help='Sub-command help')

    chat_parser = subparsers.add_parser('chat', help='Start a new chat session')
    chat_parser.add_argument('-a', '--api_key', type=str, required=True, help='Your Perplexity API key')
    chat_parser.add_argument('-m', '--model', type=str, default='sonar-medium-chat', 
                             choices=['sonar-small-chat', 'sonar-medium-chat', 'sonar-small-online', 'sonar-medium-online', 'codellama-34b-instruct', 'codellama-70b-instruct', 'llama-2-70b-chat', 'mistral-7b-instruct', 'mixtral-8x7b-instruct', 'pplx-7b-chat', 'pplx-70b-chat', 'pplx-7b-online', 
                                      'pplx-70b-online'],
                             help='The name of the model to use for chat')
    chat_parser.add_argument('-sp', '--system_prompt', type=str, default="You are an advanced AI assistant.", 
                             help='The initial system prompt setting instructions for the model')
    chat_parser.add_argument('-st', '--stream', action='store_true', help='Enable stream mode for incremental response delivery')
    chat_parser.add_argument('-mt', '--max_tokens', type=int, help='The maximum number of tokens to generate')
    chat_parser.add_argument('-t', '--temperature', type=float, help='The randomness of the response (0-2)')
    chat_parser.add_argument('-tp', '--top_p', type=float, help='The nucleus sampling threshold (0-1)')
    chat_parser.add_argument('-tk', '--top_k', type=int, help='The number of highest probability tokens to keep for filtering (0-2048)')
    chat_parser.add_argument('-pp', '--presence_penalty', type=float, help='Penalty for new tokens based on their presence (between -2.0 and 2.0)')
    chat_parser.add_argument('-fp', '--frequency_penalty', type=float, help='Penalty for new tokens based on their frequency (>0)')

    search_parser = subparsers.add_parser('search', help='Search the web with perplexity')
    search_parser.add_argument('-a', '--api_key', type=str, required=True, help='Your Perplexity API key')
    search_parser.add_argument('-m', '--model', type=str, default='sonar-medium-online', 
                               choices=['sonar-small-online', 'sonar-medium-online', 'pplx-7b-online', 'pplx-70b-online'], 
                               help='The name of the model to use for search')
    search_parser.add_argument('-q', '--query', type=str, required=True, help='The search prompt or question')
    search_parser.add_argument('-sp', '--system_prompt', type=str, default="You are an advanced AI assistant.", 
                               help='The initial system prompt setting instructions for the model')
    search_parser.add_argument('-st', '--stream', action='store_true', help='Enable stream mode for incremental response delivery')
    search_parser.add_argument('-mt', '--max_tokens', type=int, help='The maximum number of tokens to generate')
    search_parser.add_argument('-t', '--temperature', type=float, help='The randomness of the response (0-2)')
    search_parser.add_argument('-tp', '--top_p', type=float, help='The nucleus sampling threshold (0-1)')
    search_parser.add_argument('-tk', '--top_k', type=int, help='The number of highest probability tokens to keep for filtering (0-2048)')
    search_parser.add_argument('-pp', '--presence_penalty', type=float, help='Penalty for new tokens based on their presence (between -2.0 and 2.0)')
    search_parser.add_argument('-fp', '--frequency_penalty', type=float, help='Penalty for new tokens based on their frequency (>0)')

    args = parser.parse_args()

    if args.api_key:
        api_key = args.api_key
    else:
        api_key = None

    if args.stream:
        stream = True
    else:
        stream = False

    if args.command == 'chat':
        api = ChatAPI()
        api.chat(api_key=api_key, stream=stream, model=args.model, system_prompt=args.system_prompt, max_tokens=args.max_tokens,
                   temperature=args.temperature, top_p=args.top_p, top_k=args.top_k, presence_penalty=args.presence_penalty, frequency_penalty=args.frequency_penalty)
    elif args.command == 'search':
        api = SearchAPI()
        api.search(api_key=api_key, stream=stream, model=args.model, query=args.query, system_prompt=args.system_prompt, max_tokens=args.max_tokens,
                   temperature=args.temperature, top_p=args.top_p, top_k=args.top_k, presence_penalty=args.presence_penalty, frequency_penalty=args.frequency_penalty)
    else:
        print("No action specified. Use -chat to start a chat session or -search to start a search session.")
        parser.print_help()

if __name__ == "__main__":
    main()
