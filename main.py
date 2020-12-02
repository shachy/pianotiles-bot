import time

import keyboard
import pyautogui
import win32api
import win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


while not keyboard.is_pressed('q'):
    if pyautogui.pixelMatchesColor(757, 670, (0, 0, 0)):
        click(757, 670)
    if pyautogui.pixelMatchesColor(897, 670, (0, 0, 0)):
        click(897, 670)
    if pyautogui.pixelMatchesColor(1029, 670, (0, 0, 0)):
        click(1029, 670)
    if pyautogui.pixelMatchesColor(1156, 670, (0, 0, 0)):
        click(1156, 670)
