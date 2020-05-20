import requests
data = {
    'name':'va',
    'password':'vaa'
    }
html = requests.post('http://exercise.kingname.info/exercise_requests_post', json=data).content.decode()
print(html)