import pyautogui
import time
import webbrowser

busca = "Olha essa geometria - BRKsEDU"
webbrowser.open("https://www.youtube.com")

time.sleep(5)
pyautogui.click(799, 102) 
time.sleep(1)

pyautogui.write(busca, interval=0.1)
pyautogui.press("enter")

pyautogui.countdown(5)
pyautogui.click(845, 260)


# pyautogui.mouseInfo()