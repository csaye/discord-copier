import pyautogui, time, pyperclip

pyautogui.PAUSE = 1

# get mouse positions
input('Press enter when mouse over last message tag:')
message_pos = pyautogui.position()
input('Press enter when mouse over source tab:')
source_pos = pyautogui.position()
input('Press enter when mouse over destination tab:')
destination_pos = pyautogui.position()

# message retrieval loop
input('Press enter when ready to start:')
pyautogui.click(message_pos)
while True:
    pyautogui.press('down')
    pyautogui.hotkey('command', 'c')
    tag = pyperclip.paste()
