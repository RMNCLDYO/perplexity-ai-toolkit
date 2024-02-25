import argparse
from pplx_chat import ChatAPI
from pplx_search import SearchAPI

def main():
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('-a', '--api_key', type=str, help='perplexity api key', metavar='')

    class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter,
                      argparse.RawDescriptionHelpFormatter):
        pass

    parser = argparse.ArgumentParser(
        description="""
    ------------------------------------------------------------------
                               Perplexity.AI                          
                   API Wrapper & Command-line Interface               
                           [v1.1.2] by @rmncldyo                      
    ------------------------------------------------------------------

    Search the web with AI or chat with a suite of large language models. 

    For a full list of the available commands, see below, or type:
    [  %(prog)s chat --help  ] for chat options
    [ %(prog)s search --help ] for search options

    | Option(s)                | Description                                     | Example Usage                                      |
    |--------------------------|-------------------------------------------------|----------------------------------------------------|
    | chat                     | Start a conversation with an AI model.          | chat                                               |
    | search                   | Search the web in real-time with Perplexity.    | search --query "enter your search here"            |
    | -a, --api_key            | Your Perplexity API key.                        | --api_key "your_api_key"                           |
    | -q, --query              | Your online search query.                       | --query "enter your search here"                   |
    | -m, --model              | Select the model for your session.              | --model "sonar-medium-chat"                        |
    | -st, --stream            | Enable streaming responses.                     | --stream                                           |
    | -sp, --system_prompt     | Set an initial system prompt.                   | --system_prompt "you are an advanced ai assistant" |
    | -mt, --max_tokens        | Set the maximum number of response tokens.      | --max_tokens 100                                   |
    | -t, --temperature        | Adjust the randomness of the response.          | --temperature 0.7                                  |
    | -tp, --top_p             | Set nucleus sampling threshold.                 | --top_p 0.9                                        |
    | -tk, --top_k             | Number of top tokens to consider for filtering. | --top_k 40                                         |
    | -pp, --presence_penalty  | Penalize new tokens based on their presence.    | --presence_penalty 0.5                             |
    | -fp, --frequency_penalty | Penalize new tokens based on their frequency.   | --frequency_penalty 0.5                            |
    """,

        formatter_class=CustomFormatter,
        epilog="For detailed usage information, visit our ReadMe here: github.com/RMNCLDYO/Perplexity-AI-Wrapper-and-CLI"
    )


    subparsers = parser.add_subparsers(dest='command', required=True, help='Sub-command help')

    chat_parser = subparsers.add_parser(
        'chat', 
        help='Start a conversation with an AI model.', 
        description='Initiates a new chat session. Allows specifying the model, system prompt, and various parameters to control the chat behavior.', 
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    chat_parser.add_argument('-a', '--api_key', type=str, help='perplexity api key', metavar='')
    chat_parser.add_argument('-m', '--model', type=str, default='sonar-medium-chat', help='model name', metavar='')
    chat_parser.add_argument('-sp', '--system_prompt', type=str, default="you are an advanced ai assistant", help=' model instructions', metavar='')
    chat_parser.add_argument('-st', '--stream', action='store_true', help='enable stream mode')
    chat_parser.add_argument('-mt', '--max_tokens', type=int, help='max token count', metavar='')
    chat_parser.add_argument('-t', '--temperature', type=float, help='response randomness (0-2)', metavar='')
    chat_parser.add_argument('-tp', '--top_p', type=float, help='nucleus sampling threshold (0-1)', metavar='')
    chat_parser.add_argument('-tk', '--top_k', type=int, help='top k tokens for filtering (0-2048)', metavar='')
    chat_parser.add_argument('-pp', '--presence_penalty', type=float, help='new token presence penalty (-2.0 to 2.0)', metavar='')
    chat_parser.add_argument('-fp', '--frequency_penalty', type=float, help='new token frequency penalty (>0)', metavar='')

    search_parser = subparsers.add_parser(
        'search', 
        help='Search the web in real-time with Perplexity.', 
        description='Performs a web search based on a provided query. Allows specifying the model and various parameters to fine-tune the search results.', 
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    search_parser.add_argument('-q', '--query', type=str, required=True, help='enter your search here (* required)', metavar='')
    search_parser.add_argument('-a', '--api_key', type=str, help='perplexity api key', metavar='')
    search_parser.add_argument('-m', '--model', type=str, default='sonar-medium-online', help='model name', metavar='')
    search_parser.add_argument('-sp', '--system_prompt', type=str, help=' model instructions', metavar='')
    search_parser.add_argument('-st', '--stream', action='store_true', help='enable stream mode')
    search_parser.add_argument('-mt', '--max_tokens', type=int, help='max token count', metavar='')
    search_parser.add_argument('-t', '--temperature', type=float, help='response randomness (0-2)', metavar='')
    search_parser.add_argument('-tp', '--top_p', type=float, help='nucleus sampling threshold (0-1)', metavar='')
    search_parser.add_argument('-tk', '--top_k', type=int, help='top k tokens for filtering (0-2048)', metavar='')
    search_parser.add_argument('-pp', '--presence_penalty', type=float, help='new token presence penalty (-2.0 to 2.0)', metavar='')
    search_parser.add_argument('-fp', '--frequency_penalty', type=float, help='new token frequency penalty (>0)', metavar='')

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
        print("No action specified. Use `chat` to start a chat session or `search` to start a search session.")
        parser.print_help()

if __name__ == "__main__":
    main()
