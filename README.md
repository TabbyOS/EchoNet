# EchoNet

A real-time Steam comment Bot powered by GPT integration that interacts with your Steam friends. The bot is designed to leave friendly, positive comments on your Steam friends' profiles at random intervals.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Setting Up the Bot](#setting-up-the-bot)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

The EchoNet-Bot is an automated system that leaves cheerful, random comments on your Steam friends' profiles every 3 hours. It uses the GPT model for natural language generation and works exclusively on Linux (Fedora etc...). The bot automatically fetches your Steam friends via the Steam API and interacts with them in a friendly and positive manner.

## Features

- **Randomized comments**: Selects random friendly comments from a database.
- **Scheduled posts**: Leaves a comment every 3 hours.
- **Steam API Integration**: Automatically fetches your Steam friends' profiles.
- **Background operation**: Runs in the background and starts automatically with your PC.
- **Simple GUI**: The bot has a basic and easy-to-use GUI for interaction.

## Installation

### Prerequisites

Before you begin, make sure you have the following:

- Python 3.10+ installed on your system.
- `pip` for installing Python dependencies.
- Git for version control.
- A GitHub account and access to the repository.
- The `steam` library for interacting with Steam API.

### Setting Up the Bot

1. **Clone the repository:**

    Open your terminal and run the following command to clone the repository:

    ```bash
    git clone https://github.com/TabbyOS/EchoNet.git
    cd EchoNet
    ```

2. **Install dependencies:**

    Create a Python virtual environment (recommended) and install the required dependencies:

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**

    The bot requires your Steam credentials and API key to function. Set up your environment variables (you can also use a `.env` file for better security).

    ```bash
    export STEAM_API_KEY="your_steam_api_key"
    export STEAM_USERNAME="your_steam_username"
    export STEAM_PASSWORD="your_steam_password"
    ```

    Alternatively, you can hardcode these in the `config.py` file, but it's not recommended for security reasons.

4. **Install additional dependencies for Linux:**

    If you're running the bot on Linux, you may need to install the required packages for Wine to emulate Windows applications. Here's how you can do that:

Debian/Ubuntu:

    sudo apt update && sudo apt install wine

Fedora:

    sudo dnf install wine

## Configuration

The bot's configuration is simple and can be adjusted directly through the `GUI`. The settings include:

- **API Key**: Your Steam API key.
- **Comment interval**: Set the number of hours between each comment post.
- **Bot behavior**: Modify the bot’s message selection and other behavior.

## Usage

1. **Running the Bot**:

    To run the bot, simply execute the `EchoNet.py` script:

    ```bash
    python EchoNet.py
    ```

    The bot will start running, and it will comment on your Steam friends' profiles at the specified intervals.

2. **Building Executables** (Optional):

    You can build executables for both Windows and Linux using GitHub Actions. This will create standalone executables that can run without Python installed.

    - **For Linux**: The bot can be executed directly on Linux after building.
    - **For Windows**: Use Wine to run the bot if needed.

3. **Running in the Background**:

    The bot is designed to run in the background. It can be configured to start automatically when your computer starts by adding it to your startup applications.

## Contributing

We welcome contributions to this project! If you'd like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Open a pull request.

Please ensure your code adheres to the existing coding style, and write tests where applicable.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
=======
