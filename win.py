import os
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
    # path = os.path('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
    subprocess.call('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe https://www.nowtv.com/gb/watch/playback/live/1306');

    # Wait for application to launch
    time.sleep(2)

    # Click on the address bar
    # pyautogui.moveTo(300, 75)
    # pyautogui.click()

    # Open a new tab
    # pyautogui.hotkey('control', 't')

    # Type in the address and go to it
    # pyautogui.write('https://www.nowtv.com/gb/watch/playback/live/1306')
    # pyautogui.press('enter')

    print('Waiting on page load')
    # Wait for pageload
    time.sleep(10)

    # Click on the centre of the screen
    pyautogui.moveTo(960, 540)
    pyautogui.click()

    # Make page full screen
    pyautogui.hotkey('control', 'f')

    # Start recording
    pyautogui.hotkey('alt', 'f9')

    return "Chrome launched"


@app.get("/api/record/stop")
def record_stop():

    # Stop recording


    # Close chrome


    return "Recording stopped"
