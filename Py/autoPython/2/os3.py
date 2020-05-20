import os
print(os.getcwd())
hello = open('.\\hello.py')
text = hello.read()
print(text)

# 读取一次之后就空了
hello = open('.\\hello.py')
lines = hello.readlines()
for i in lines:
    print(i)

hello = open('.\\hello.py', 'a')
hello.write('# hello world\n')