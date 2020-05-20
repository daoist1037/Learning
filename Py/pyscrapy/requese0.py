import requests
html = requests.get('https://www.baidu.com').content.decode('utf-8')
text = html
print(a)
print(text[:250])
html = requests.get('https://www.baidu.com')
text = html.text
print(text[:250])