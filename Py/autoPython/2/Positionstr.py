import pyautogui,time
pyautogui.click(button='right',clicks=1)
try:
    while True:
        x,y = pyautogui.position()
        PositionStr = 'X:'+str(x).rjust(4)+' Y:'+str(y).rjust(4)
        print(PositionStr,end='')
        time.sleep(1)
        print('\b'*len(PositionStr),end='',flush=True)

except KeyboardInterrupt:
    print('\nDone!')

'''
‘\b’:主要功能是将光标倒退指定长度的字符；加入end=’ ‘,使得执行后不换行
‘\r’:主要功能是将光标回到一行的开始位置；同样的，加入end=’ ',使得执行后不换行
'''
