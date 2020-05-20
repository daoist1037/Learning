import webbrowser,requests
#webbrowser.open('https://map.baidu.com/search/华中科技大学/@12959238.56,4825347.47,12z')
#webbrowser.open('https://www.google.com/maps/place/华中科技大学')

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(len(res.text))
print(res.text[:250])
res.raise_for_status()
filename = open('Rmom.txt', 'wb')
for chunk in res.iter_content(100000):
    filename.write(chunk)

filename.close()

'''
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
res.raise_for_status()
在交互环境中使用
'''