import pyautogui

pyautogui.PAUSE = 1

pyautogui.hotkey('win', 'r')

pyautogui.write("chrome")
pyautogui.press('enter')

pyautogui.write("youtube.com")
pyautogui.press('enter')

pyautogui.countdown(3)
pyautogui.click(728, 118)
pyautogui.write("pokemon ")
pyautogui.press('enter')


