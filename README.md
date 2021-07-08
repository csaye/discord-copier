# Discord Copier

Copies received messages from one Discord server to another.

## Requirements

It is suggested that you use a Python virtualenv (`pip install virtualenv`) with Python version 3.9. Run `virtualenv -p python3 env` to initialize the environment. You only need to initialize the environment once.

To run, activate the environment: `source env/bin/activate`. Then run `pip install -r requirements.txt`.

To exit the environment, run `deactivate`.

## Installation

1) Download the `discord-copier` directory.
2) Invite the Discord Copier bot to you desired server using [this link](`https://discord.com/oauth2/authorize?client_id=859870778270416917&permissions=2048&scope=bot`). The bot will send messages to the first channel with the name `general`.
3) Make sure [Google Chrome](https://www.google.com/chrome) and [Python](https://www.python.org/downloads) are installed on your machine.

**Loading the extension**

1) Open the Extension Management page by navigating to `chrome://extensions` on Google Chrome.
2) Enable Developer mode by clicking the toggle switch next to **Developer Mode**.
3) Click the **Load unpacked** button and select the `discord-copier` directory.

![](https://user-images.githubusercontent.com/27871609/124992129-6fc48b80-dff7-11eb-9a45-a361aaec333a.png)

**Running**

1) Navigate to the `discord-copier` directory in the command line.
2) Install dependencies with `pip install websockets` or by following the virtualenv instructions above.
3) Start the socket server and the Discord bot by running `python server.py`.
4) Activate the extension on a Chrome tab with your source server. Press the `Start` button to begin listening for messages.
