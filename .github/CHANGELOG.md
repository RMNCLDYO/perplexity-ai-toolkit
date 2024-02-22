# Changelog

All notable changes to the project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
