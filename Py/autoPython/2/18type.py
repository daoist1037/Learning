import pyautogui,subprocess,time
subprocess.Popen(['start','hello.txt'],shell = True)
time.sleep(3)
pyautogui.click()
pyautogui.press('shift')
pyautogui.typewrite('hello world')
pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')