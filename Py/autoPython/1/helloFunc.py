def hello():
    print('hello')
    print('world')
    print('hello there.')
def Hello(name):
    print('Hello ' + name)
    return 1

hello()
hello()
hello()
r = Hello('alpha')
print(r)

print('Hello ', end='')
print('world')