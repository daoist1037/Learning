import pyperclip,pyautogui,time,random

text = [
        '草泥马','龟孙','兔孙','mmp','乌龟王八蛋','欧尼酱','带死ki'
        ]
time.sleep(5)

for i in range(100):
    num = random.randint(0,6)
    pyperclip.copy(text[num])
    pyautogui.click(clicks=1,button='right')
    pyautogui.moveRel(20,100,duration=0.01)
    pyautogui.click(clicks=1,button='left')
    pyautogui.moveRel(-20,-100,duration=0.01)
    pyautogui.moveRel(700,70,duration=0.01)
    pyautogui.click(clicks=1,button='left')
    pyautogui.moveRel(-700,-70,duration=0.01)
