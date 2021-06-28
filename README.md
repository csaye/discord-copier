# Discord Copier

Copies received messages from one discord server to another.

## Dependencies

Discord Copier is written in [Python](https://www.python.org/downloads) and depends on pyautogui, pyperclip, and [Google Chrome](https://www.google.com/chrome). Once Python is installed, install dependency packages with `pip install pyautogui pyperclip`.

## Setup

Open two Google Chrome tabs. One should have the Discord server you want to copy messages from and the other should have the Discord server you want to paste messages to. In the tab with the source server, press `command + shift + c` to open the developer console and select the elements tab. Use `command + f` to search for `scrollerInner` and select the `div` with the class.

## Running

Download and run the [DiscordCopier.py](DiscordCopier.py) file with `python DiscordCopier.py`. It will prompt you to first hover your mouse over the last element within the `scrollerInner` `div` we found earlier. Press enter. Then hover your cursor over the source and destination tabs and press enter on each. After pressing enter one more time to start the program, it should run.
