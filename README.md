<p align="center">
    <a href="https://python.org" title="Go to Python homepage"><img src="https://img.shields.io/badge/Python-&gt;=3.x-blue?logo=python&amp;logoColor=white" alt="Made with Python"></a>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/maintained-yes-2ea44f" alt="maintained - yes">
    <a href="/CONTRIBUTING.md" title="Go to contributions doc"><img src="https://img.shields.io/badge/contributions-welcome-2ea44f" alt="contributions - welcome"></a>
</p>

<p align="center">
    <a href="https://pypi.org/project/requests"><img src="https://img.shields.io/badge/dependency-requests-critical" alt="dependency - requests"></a>
    <a href="https://pypi.org/project/python-dotenv"><img src="https://img.shields.io/badge/dependency-python--dotenv-yellow" alt="dependency - python-dotenv"></a>
</p>

<p align="center">
    <img width="700" src="https://raw.githubusercontent.com/RMNCLDYO/Perplexity-AI-Wrapper-and-CLI/main/.github/logo.png">
</p>

<p align="center">
    <img src="https://img.shields.io/badge/dynamic/json?label=Perplexity+AI+Wrapper+and+CLI&query=version&url=https%3A%2F%2Fraw.githubusercontent.com%2FRMNCLDYO%2FPerplexity-AI-Wrapper-and-CLI%2Fmain%2F.github%2Fversion.json" alt="Version">
</p>

## Overview
A simple python wrapper and command-line interface (CLI) for Perplexity AI, enabling programatic access to the chat and online search features using a range of Large Language Models.

## Key Features
- **Python Wrapper**: Simplifies calling the Perplexity API with a few lines of code.
- **Command-Line Interface**: Enables users to interact with the API directly from the terminal.
- **Support for Multiple Models**: Integrates with a range of models including `codellama-70b-instruct`, `pplx-7b-chat`, `pplx-70b-chat`, `pplx-7b-online`, `pplx-70b-online`, `llama-2-70b-chat`, `codellama-34b-instruct`, `mistral-7b-instruct`, and `mixtral-8x7b-instruct`, as defined in `models.json` and [here](https://docs.perplexity.ai/docs/model-cards).
- **Flexible Configuration**: Customizable settings for model choice, token limits, temperature, top_k and more.

## Prerequisites
- `Python 3.x`
- A [Perplexity AI](https://perplexity.ai) account and API key.

## Dependencies
- `requests`: For making HTTP requests to the Perplexity API.
- `python-dotenv`: (*Optional*) For loading environment variables from an `.env` file.

## Getting an Account and API Key
1. **Create an Account**: Visit [Perplexity AI](https://perplexity.ai) and sign up for an account.
2. **Open the API Page**: Once logged in, navigate to your account settings and click on API. You can also access the page [here](https://www.perplexity.ai/pplx-api). 
3. **Generate an API Key**: The API key is a your access token that can be used until it is manually refreshed or deleted.

## Installation
Clone the repository and install the required dependencies:
```bash
git clone https://github.com/RMNCLDYO/Perplexity-AI-Wrapper-and-CLI.git
cd Perplexity-AI-Wrapper-and-CLI
pip install -r requirements.txt
```

## Configuration
1. **Environment Variables** (*Optional*): Set your Perplexity API key in a `.env` file:
   ```
   api_key='your_api_key_here'
   ```
***NOTE:*** If you choose not to store your API key as an environment variable, you must pass your API key through the wrapper like this: `PerplexityAPI(api_key='your_api_key').search()` or through the CLI like this: `--api-key your_api_key --search`.

## General Usage

### Wrapper
- **Initialize Online Search Session**: 
    ```python
    from pplx import PerplexityAPI
    
    PerplexityAPI().search()
    ```

- **Initialize Chat Session**:
    ```python
    from pplx import PerplexityAPI

    PerplexityAPI().chat()
    ```

### Command-line interface (CLI)
- **Help Menu**: Refer to the help for more options:
  ```bash
  python pplx.py --help
  ```
- **Initialize Online Search Session**: 
  ```bash
  python pplx.py --api-key your_api_key --search
  ```
- **Initialize Chat Session**: 
  ```bash
  python pplx.py --api-key your_api_key --chat
  ```

## Advanced Usage

### CLI Usage Options
| **Option(s)**                     | **Description**            | **Example Usage**                    |
|-----------------------------------|----------------------------|--------------------------------------|
| `-a`, `--api-key`                 | Your Perplexity API key.    | `--api-key your_api_key`             |
| `-c`, `--chat`                    | Start a new chat session.   | `--chat`                             |
| `-s`, `--search`                  | Start a new search session. | `--search`                           |
| `-m`, `--model`                   | The name of the model that will complete your prompt. Possible values include `codellama-70b-instruct`, `pplx-7b-chat`, `pplx-70b-chat`, `pplx-7b-online`, `pplx-70b-online`, `llama-2-70b-chat`, `codellama-34b-instruct`, `mistral-7b-instruct`, and `mixtral-8x7b-instruct`.                 | `--model pplx-70b-chat`              |
| `-st`, `--stream`                 | Enabling this feature will deliver the response in incremental segments, providing users with a continuous flow of data, akin to the way services like ChatGPT transmit information.         | `--stream`                           |
| `-sp`, `--system-prompt`          | The initial system prompt. The system prompt xplicitly sets the insturctions for the model.              | `--system-prompt "Your prompt here"` |
| `-mt`, `--max-tokens`             | The maximum number of completion tokens returned by the API. The total number of tokens requested in max_tokens plus the number of prompt tokens sent in messages must not exceed the context window token limit of model requested. If left unspecified, then the model will generate tokens until either it reaches its stop token or the end of its context window.   | `--max-tokens 100`                   |
| `-t`, `--temperature`             | The amount of randomness in the response, valued between 0 inclusive and 2 exclusive. Higher values are more random, and lower values are more deterministic. You should either set temperature or top_p, but not both. | `--temperature 0.7`                  |
| `-tp`, `--top-p`                  | The nucleus sampling threshold, valued between 0 and 1 inclusive. For each subsequent token, the model considers the results of the tokens with top_p probability mass. You should either alter temperature or top_p, but not both. | `--top-p 0.9`                        |
| `-tk`, `--top-k`                  | The number of tokens to keep for highest top-k filtering, specified as an integer between 0 and 2048 inclusive. If set to 0, top-k filtering is disabled.        | `--top-k 40`                         |
| `-pp`, `--presence-penalty`       | A value between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. Incompatible with `frequency_penalty`.     | `--presence-penalty 0.5`             |
| `-fp`, `--frequency-penalty`      | A multiplicative penalty greater than 0. Values greater than 1.0 penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. A value of 1.0 means no penalty. Incompatible with `presence_penalty`.    | `--frequency-penalty 0.5`            |

- **Initialize Online Search Session**: 
  ```bash
  python pplx.py -a your_api_key -s -m pplx-7b-online -mt 2000
  ```
- **Initialize a Chat Session**: 
  ```bash
  python pplx.py -a your_api_key -chat -m mixtral-8x7b-instruct -tk 1096 -fp 0.5
  ```

### Wrapper Usage Options
Here are the options that can be passed as parameters in the Python wrapper:

| **Parameter**         | **Description**                                | **Example Usage**                    |
|-----------------------|------------------------------------------------|--------------------------------------|
| `api_key`             | Your Perplexity API key.                        | `api_key='your_api_key'`             |
| `model`               | The name of the model that will complete your prompt. Possible values include `codellama-70b-instruct`, `pplx-7b-chat`, `pplx-70b-chat`, `pplx-7b-online`, `pplx-70b-online`, `llama-2-70b-chat`, `codellama-34b-instruct`, `mistral-7b-instruct`, and `mixtral-8x7b-instruct`.                                     | `model='pplx-70b-chat'`              |
| `stream`              | Determines whether or not to incrementally stream the response.                             | `stream=True`                        |
| `system_prompt`             | The initial system prompt. The system prompt xplicitly sets the insturctions for the model.                        | `system_prompt="Your prompt here"`             |
| `max_tokens`          | The maximum number of completion tokens returned by the API. The total number of tokens requested in max_tokens plus the number of prompt tokens sent in messages must not exceed the context window token limit of model requested. If left unspecified, then the model will generate tokens until either it reaches its stop token or the end of its context window.                       | `max_tokens=100`                     |
| `temperature`         | The amount of randomness in the response, valued between 0 inclusive and 2 exclusive. Higher values are more random, and lower values are more deterministic. You should either set temperature or top_p, but not both.                     | `temperature=0.7`                    |
| `top_p`               | The nucleus sampling threshold, valued between 0 and 1 inclusive. For each subsequent token, the model considers the results of the tokens with top_p probability mass. You should either alter temperature or top_p, but not both.                     | `top_p=0.9`                          |
| `top_k`               | The number of tokens to keep for highest top-k filtering, specified as an integer between 0 and 2048 inclusive. If set to 0, top-k filtering is disabled.                            | `top_k=40`                           |
| `presence_penalty`    | A value between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. Incompatible with `frequency_penalty`.                         | `presence_penalty=0.5`               |
| `frequency_penalty`   | A multiplicative penalty greater than 0. Values greater than 1.0 penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. A value of 1.0 means no penalty. Incompatible with `presence_penalty`.                        | `frequency_penalty=0.5`              |                                                                                |

- **Initialize Online Search Session**: 
    ```python
    from pplx import PerplexityAPI
    
    PerplexityAPI().search(model="pplx-7b-online", max_tokens=2000)
    ```

- **Initialize Chat Session**:
    ```python
    from pplx import PerplexityAPI

    PerplexityAPI().chat(model="mixtral-8x7b-instruct", top_k=1096, frequency_penalty=0.5)
    ```

### Available Models

| **Model**                | **Context Length** (*max tokens*) |
|--------------------------|--------------------|
| `codellama-34b-instruct` | 16384              |
| `codellama-70b-instruct` | 16384              |
| `llama-2-70b-chat`       | 4096               |
| `mistral-7b-instruct`    | 4096               |
| `mixtral-8x7b-instruct`  | 4096               |
| `pplx-7b-chat`           | 8192               |
| `pplx-70b-chat`          | 4096               |
| `pplx-7b-online`         | 4096               |
| `pplx-70b-online`        | 4096               |

**Last updated Janurary 30, 2024*

## API Rate Limits
Be mindful of Perplexity's API rate limits, which can be found [here](https://docs.perplexity.ai/docs/rate-limits).

## Contributing
Contributions are welcome!

Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for detailed guidelines on how to contribute to this project.

## Reporting Issues
Encountered a bug? We'd love to hear about it. Please follow these steps to report any issues:

1. Check if the issue has already been reported.
2. Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) template to create a detailed report.
3. Submit the report [here](https://github.com/RMNCLDYO/Perplexity-AI-Wrapper-and-CLI/issues).

Your report will help us make the project better for everyone.

## Feature Requests
Got an idea for a new feature? Feel free to suggest it. Here's how:

1. Check if the feature has already been suggested or implemented.
2. Use the [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) template to create a detailed request.
3. Submit the request [here](https://github.com/RMNCLDYO/Perplexity-AI-Wrapper-and-CLI/issues).

Your suggestions for improvements are always welcome.

## Versioning and Changelog
Stay up-to-date with the latest changes and improvements in each version:

- [CHANGELOG.md](.github/CHANGELOG.md) provides detailed descriptions of each release.

## Security
Your security is important to us. If you discover a security vulnerability, please follow our responsible disclosure guidelines found in [SECURITY.md](.github/SECURITY.md). Please refrain from disclosing any vulnerabilities publicly until said vulnerability has been reported and addressed.

## License
Licensed under the MIT License. See [LICENSE](LICENSE) for details.
