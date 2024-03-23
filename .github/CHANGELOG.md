# Changelog

All notable changes to the project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2024-03-23

### Added
- config.py: Introduced a configuration management system to load environment variables and default settings.
- client.py: Implemented a new client architecture for making API requests, including streaming support.

### Improved
- loading.py: No changes detected in functionality, the code remains identical.
- perplexity.py: Enhanced with a modular approach separating chat and search functionalities into distinct classes with improved error handling.
- cli.py: Major overhaul to CLI interface, incorporating new options and better help documentation, facilitating both chat and search operations with the new client architecture.

### Changed
- Environment variable management has been centralized and now requires specific keys (`PERPLEXITY_API_KEY`, `PERPLEXITY_DEFAULT_CHAT_MODEL`, `PERPLEXITY_DEFAULT_SEARCH_MODEL`, `PERPLEXITY_BASE_URL`, `PERPLEXITY_TIMEOUT`), but has defaults already set for ease of use.
- The base API interaction logic has been encapsulated within the Client class, abstracting the complexities of request handling, including streaming.

### Removed
- `pplx.py`, `pplx_cli.py`, `base_api.py`, `pplx_search.py`, and `pplx_chat.py` have been replaced with the new `client.py`, `config.py`, `perplexity.py`, and `cli.py` files, indicating a structural overhaul.
- The direct dependency on .env file loading within API wrapper files has been removed, now managed centrally in `config.py`.

### Fixed
- The handling of API keys and configuration settings has been standardized, fixing inconsistencies in how environment variables were previously managed.

## [1.1.2] - 02/25/2024

`base_api.py`

### Improved

- Enhanced error handling in the post method to provide clearer error messages and gracefully exit the application upon encountering a critical error, improving user experience and debuggability.
- Added a finally block to ensure that the loading animation is always stopped, even if an error occurs, preventing potential terminal display issues.
- Modified the loading animation to start only in non-streaming requests to avoid overlap with streaming output, enhancing output readability.
- Streamlined the API key retrieval process with a more descriptive error message if the API key is not found, aiding users in configuration setup.

### Fixed

- Fixed an issue where the loading animation could potentially continue running or the cursor remained hidden if an exception was thrown during a request.
- Addressed a potential bug by ensuring the terminal is cleared only on error, preserving user input and previous interactions for reference.

`pplx_cli.py`

### Added

-Introduced a custom argparse formatter CustomFormatter combining ArgumentDefaultsHelpFormatter and RawDescriptionHelpFormatter to improve the help text readability.
- Implemented detailed command descriptions and examples in the CLI help output, providing immediate guidance to users without external documentation.

### Changed

- Unified the -a, --api_key argument declaration across both chat and search commands to improve code maintainability.
- Implemented a shared function to add common arguments to both chat and search parsers, reducing code duplication.
- Updated argument descriptions for enhanced clarity, making it easier for users to understand the purpose and usage of each command.
- Modified all argument metavariables to an empty string, streamlining the help output by removing uppercase type hints for a cleaner interface.

### Removed

- Eliminated redundant argument declarations, specifically for --api_key in both chat and search subparsers, centralizing its declaration for cleaner code.

## [1.1.1] - 02/23/2024

### Added
- Support for Perplexity Labs latest `sonar-small-chat`, `sonar-small-online`, `sonar-medium-chat`, and `sonar-medium-online` AI models offering improvements in cost-efficiency, speed, and performance.
- Extended context window support, now accommodating up to 16k tokens for models like `mixtral-8x7b-instruct` and all Perplexity models.
- Increased public rate limits across all models to accommodate approximately 2x more requests.

> [!WARNING]  
> On March 15, the `pplx-70b-chat`, `pplx-70b-online`, `llama-2-70b-chat`, and `codellama-34b-instruct` models will no longer be available through the Perplexity API.

## [1.1.0] - 02/22/2024

### Added
- loading.py for implementing a loading spinner, enhancing user experience during network requests.
- base_api.py introducing BaseAPI class for shared API functionality, including request handling and streaming support.
- pplx_chat.py and pplx_search.py classes, extending BaseAPI to separate concerns for chat and search functionalities.
- Detailed error handling and environmental variable support for API key configuration, increasing usability and flexibility.
- A comprehensive command-line interface setup in pplx_cli.py, facilitating the use of both chat and search functionalities through a unified interface.

### Changed
- Modularized the codebase into separate files (pplx_cli.py, loading.py, base_api.py, pplx_chat.py, pplx_search.py), improving code organization and maintainability.
- Enhanced the command-line interface with more detailed options, including model selection, temperature, top_p, top_k, presence penalty, and frequency penalty settings, allowing for a more customized user experience.
- Updated the streaming functionality to use a loading spinner, providing real-time feedback during asynchronous operations.
- Improved API key management by supporting environmental variables and .env files, simplifying configuration.

### Removed
- The single-file script structure, replacing it with a more modular and scalable project architecture.
- Direct use of requests and json in the CLI functions, moving this logic to the BaseAPI class to reduce redundancy.

### Fixed
- Fixed issue where streaming was not working.
- Fixed issue where command line parameters were not being set.
- Fixed argument parsing structure in pplx_cli.py with subparsers for chat and search commands, enabling a more structured and versatile command-line interface.

### Security
- Implemented secure API key handling through environment variables and .env files, reducing the risk of key exposure.

## [1.0.1] - 01/30/2024

### Added
- Added support for new model "codellama-70b-instruct" by Meta.

## [1.0.0] - 01/10/2024

### Added
- Initial release.
