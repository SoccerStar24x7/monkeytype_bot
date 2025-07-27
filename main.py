import cv2
import pytesseract as pyt
import pyautogui
import time
import os


typing_interval = 0.011298 # exact interval needed to achieve 999 wpm (max limit on monkeytype)


time.sleep(3)

fullScreen = pyautogui.screenshot("full_screen.png")

time.sleep(0.5)

img = cv2.imread("full_screen.png")
if img is None:
    raise FileNotFoundError("Image could not be loaded. Check the path or file format.")

width, height = pyautogui.size()

crop = img[round(0.40625*height):round(0.6875*height), 0:width]

extractedText = pyt.image_to_string(crop)

areaToDelete = extractedText.find("english") + 7

text = extractedText[areaToDelete:]

while text.find("\n") != -1:
    text = text.replace("\n", " ")

pyautogui.typewrite(text, interval=typing_interval)

os.remove("full_screen.png")
