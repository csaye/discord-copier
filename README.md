# Discord Copier

Copies received messages from one Discord server to another.

## Requirements

It is suggested that you use a Python virtualenv (`pip install virtualenv`) with Python version 3.9. Run `virtualenv -p python3 env` to initialize the environment. You only need to initialize the environment once.

To run, activate the environment: `source env/bin/activate`. Then run `pip install -r requirements.txt`.

To exit the environment, run `deactivate`.

## About

Discord Copier uses Python to set up a socket server, a chrome extension to pull chat messages from a server, and a Discord bot to send those messages into another server.

## Running

Start the socket server and the Discord bot with `python server.py` and `python bot.py`. Enable the listener in the server you want to pull messages from with the chrome extension. Start and stop listening in your target server with `!start` and `!stop`.
