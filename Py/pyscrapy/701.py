import json
data={
    'basic_info':{
        'name':'king',
        'age':24,
        'sex':'male',
        'merry':'false'
            },
    'work_info':{
        'salary':1800,
        'position':'engineer',
        'department':None
            }
        }
text = json.dumps(data,indent=4)
text = json.dumps(data)
print(text)
dict_2 = json.loads(text)
print(dict_2)