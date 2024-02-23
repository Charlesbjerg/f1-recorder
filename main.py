from typing import Union
from fastapi import FastAPI
import pyautogui
import subprocess
import time

# Init FastAPI
app = FastAPI()

# Routes
@app.get("/api/record/start")
def record_start():

    # Take a screenshot
    # im1 = pyautogui.screenshot()
    # im1.save('my_screenshot.png')

    # Write line to console
    print("Launching Chrome...");

    # Launch an application
    subprocess.call(['open', '/Applications/Google Chrome.app']);

    # Wait for application to launch
    time.sleep(2)

    # Click on the address bar
    pyautogui.moveTo(300, 75)
    pyautogui.click()

    # Open a new tab
    pyautogui.hotkey('command', 't')

    # Type in the address and go to it
    pyautogui.typewrite('https://www.nowtv.com/gb/watch/playback/live/1306')
    pyautogui.press('enter')

    # Wait for pageload
    time.sleep(10)

    # Click on the centre of the screen
    pyautogui.moveTo(960, 540)
    pyautogui.click()

    # Make page full screen
    pyautogui.hotkey('command', 'f')

    # Start recording

    return "Chrome launched"


@app.get("/api/record/stop")
def record_stop():

    # Stop recording


    # Close chrome


    return "Recording stopped"
