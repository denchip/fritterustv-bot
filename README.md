# FritterusTV Bot

> Telegram bot with django admin panel for making random choice


# Open source
* License: MIT license


## Install your bot dependencies 📦

You have two primary options to install de bot Python dependencies: pip or Poetry. You can also use pipenv, virtualenvwrapper or another package managers. We recommend Poetry.

1. Install dependencies using [Poetry](https://python-poetry.org):

    ```
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    cd src/bot
    poetry install
    ```

✨ **Tip (optional):** Create these aliases on your `.bashrc` or `.zshrc`, like this

    ```
    alias poetry="python3 -m poetry"
    alias django="poetry run ./dev.py"
    alias djr="django runserver"
    alias djm="django makemigrations && django migrate"
    alias djmr="djm && djr"
    ```

1. Or install your dependencies using pip.

    ```
    pip3 install -r requirements.txt
    ```
## Initialize your bot environment variables

Place your env vars to the `.env` file (never push this file to the repo):

    SECRET_KEY=your django random secret key
    TELEGRAM_TOKEN=your bot token


## Start the bot

Start the bot (using the previously suggested alias, optional):

    django runbot

Or using Poetry:

    python3 -m poetry run ./dev.py runbot

Or using Python:

    python3 dev.py runbot

