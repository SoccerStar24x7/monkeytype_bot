I will post a video sometime in the next 2000 years about how to use this. 

The box maxes out at 999 WPM as that's the limit Monkeytype accepts as real WPM before counting it as "Infinite".

The time interval listed at the top of the "main.py" file is how fast the bot types (0.011298).

You should:
1. run code
2a. quickly switch to a monkeytype tab (you have 3 seconds to do this)
2b. the monkeytype test should be 25 words or less. The bot can't do more than 25 words.
3. Wait and watch the magic.

Required dependencies (run commands in the virtual environment):
- OpenCV: "pip install opencv-python"
- PyTesseract: "pip install pytesseract". must also install Tesseract OCR Engine beforehand.
- PyAutoGUI: "pip install pyautogui"
- TKinter: "pip install tk"

  Or, you can use this command:
  pip install opencv-python pytesseract pyautogui tk

I used OpenCV to crop and load the screenshot (to see the text), PyTesseract to interpret images to text, and PyAutoGui to type. 
