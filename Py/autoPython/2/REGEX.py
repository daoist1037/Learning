import re
temp = re.compile(r'\d\d\d-\d\d\d\d\d\d\d\d')
mo = temp.search('My telphone number is 173-95898126')

print(mo.group())
text = mo.group()
text = text.split('-')
text = ''.join(text)
print(text)
print('\n\n')
temp = re.compile(r'(\d\d\d)-(\d\d\d\d\d\d\d\d)')
mo = temp.search('My telphone number is 173-95898126')
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))


temp = re.compile(r'\d\d\d')
mo = temp.search('asdddd333\n343')
print(mo.group())
mo = temp.findall('asdddd333\n343')
for i in range(len(mo)):
    print(mo[i])
    print(i)
for name in mo:
    print(name)