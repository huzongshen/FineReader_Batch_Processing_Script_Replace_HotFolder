import pyautogui
pyautogui.sleep(1)
pyautogui.hotkey("shift","ctrl","R")
pyautogui.sleep(0.1)
pyautogui.hotkey("alt","r")
a=5
while a!=0:
    pyautogui.sleep(1)
    try:
        location = pyautogui.locateOnScreen("jpg/chuli.png")#处理已完成
        print('image found')
        pyautogui.press("space")
        pyautogui.hotkey("ctrl","s")
        pyautogui.sleep(9)
        pyautogui.hotkey("alt","F4")
        pyautogui.hotkey("alt","tab")
        a = 0
    except pyautogui.ImageNotFoundException:
        print('ImageNotFoundException: image not found')
    try:
        location = pyautogui.locateOnScreen("jpg/ocr.png")#OCR已完成功完成
        print('image found')
        pyautogui.hotkey("space")
        pyautogui.sleep(0.5)
        pyautogui.hotkey("ctrl","s")
        pyautogui.sleep(2)
        pyautogui.hotkey("enter")
        pyautogui.sleep(1)
        pyautogui.hotkey("alt","F4")
        pyautogui.hotkey("alt","tab")
        a = 0
    except pyautogui.ImageNotFoundException:
        print('ImageNotFoundException: image not found')
