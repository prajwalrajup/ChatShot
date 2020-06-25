
import pyautogui

for i in range(10):
    img = pyautogui.screenshot(region=(410,133,955,542))
    img.save(str(i)+".jpg")
    # screen x = 410,133,1365,675
