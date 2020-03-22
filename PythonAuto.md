

# 基础
## 整型、浮点型和字符串数据类型
## 字符串连接和复制
+ ```python
  'abc' + 'def'
  ```
+ ```python
  'abc' * 5 #字符串变为 abc 重复5次，必须为整型
  ```
## 变量命名规则
1. 只能是一个词。<br>
2. 只能包含字母、数字和下划线。<br>
3. 不能以数字开头。<br>
## `print()`函数
关键字：
+ `seq` 会指定`print()`内元素间隔用什么取代，默认是空格
  ```python
  print('hello', 'world', seq='')
  **```**
+ `end` 会指定两个`print()'之间是否换行，默认是自动添加换行
  ```python
  print('hello',end='')
  print('world')
  ```
## `input()`函数
+ 下例会在输入前输出 Your name is 作为提示，然后将输入赋给 name 
  ```python
  name = input('Your name is: ')
  ```
## `len()`函数
+ 获取长度，如字符串长度，数组长度
## `str() float() int()`函数
+ 返回相应类型的数据
  
# 控制流
## 布尔值
+ `True`
+ `False`
+ 首字母大写
## 比较操作符
## 布尔操作符
+ and
+ not
+ or
## 控制流语句
代码块规则：
1. 缩进增加时，代码块开始。
2. 代码块可以包含其他代码块。
3. 缩进减少为零，或减少为外面包围代码块的缩进，代码块就结束了。
### `if else elif`
  ```python
  if name == 'Alice':
    print('Hi, Alice.')
  elif age < 12:
    print('You are not Alice, kiddo.')
  else:
    print('You are neither Alice nor a little kid.')
  ```
### `while`
  ```python
  name = ''
  while name != 'your name':
    print('Please type your name.')
    name = input()
    print('Thank you!')
  ```
### `break`跳出该层循环
### `continue`直接进行下次循环
### `for` 循环和`range()`函数
  ```python
  name = ''
  for i in range(7):
    print(i)
  ```
  $[0,7)$
### `range()`的开始、停止和步长参数
  ```python
  range(12,16)  #[12,16)
  range(0,10,2) #第三个元素为步长 0 2 4 6 8 
  ```
### 导入模块
  import 语句包含以下部分：
  + import 关键字；
  + 模块的名称；
  + 可选的更多模块名称，之间用逗号隔开。
  ```python
  import random
  import random, sys, os, math
  # 调用模块内函数时候
  random.randit(1,7)  #必须以模块名.函数名的形式
  from random import *  #若以该形式导入模块就直接使用函数名调用
  ```
### 用`sys.exit()`提前结束程序

# 函数
```python
  def hello(name):
    print('Hello ' + name)
    return name
```
## `None` 值
+ ``None`` 是``NoneType`` 数据类型的唯一值（其他编程语言可能称这个值为``null``、``nil`` 或``undefined``）。就像布尔值``True``和``False ``一样，``None`` 必须大写首字母`N`。
## 局部和全局作用域
## 名称相同的局部变量和全局变量
```python
def spam():
  eggs = 'spam local'
  print(eggs) # prints 'spam local'

def bacon():
  eggs = 'bacon local'
  print(eggs) # prints 'bacon local'
  spam()
  print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'
```
结果会是
>bacon local  
>spam local  
>bacon local  
>global   
变量名相同时，会屏蔽全局变量
## `global` 语句
如果需要在一个函数内修改全局变量，就使用global 语句
```python
def spam():
  global eggs
  eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
```
## 异常梳理
如果在try 子句中的代码导致一个错误，程序执行就立即转到except 子句的代
码。
  ```python
  def spam(divideBy):
  try:
    return 42 / divideBy
  except ZeroDivisionError:
    print('Error: Invalid argument.')
  ```

# 列表
## 列表数据类型
+ `['cat', 'bat', 'rat', 'elephant']`
+ `[]`是一个空列表，不包含任何值，类似于空字符串
### 用下标取得列表中的单个值
```python
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1]

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
spam[0]
spam[0][1]
```
### 负数下标
+ 整数值−1 指的是列表中的最后一个下标
+ −2 指的是列表中倒数第二个下标，以此类推
### 利用切片取得子列表
```python
spam[1:3] #左闭右开
spam[:2]
spam[:]
```
### 用下标改变列表中的值
### 列表连接和列表复制
```python
[1, 2, 3] + ['A', 'B', 'C']
['X', 'Y', 'Z'] * 3
```
### 用`del `语句从列表中删除值
+ `del` 语句将删除列表中下标处的值，表中被删除值后面的所有值，都将向前移
动一个下标
## 列表用于循环
### `in` 和`not in` 操作符
```python
'howdy' in ['hello', 'hi', 'howdy', 'heyas']
#返回布尔值
```
### 多重赋值技巧
```python
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
# size color disposition 将依次被赋予与列表cat顺序相同的值
```
## 增强的赋值操作
```python
bacon *= 3
```
## 方法
### 用`index()`方法在列表中查找值
+ 列表值有一个`index()`方法，可以传入一个值，如果该值存在于列表中，就返回它
的下标。如果该值不在列表中，Python 就报 **ValueError**
+ 如果列表中存在重复的值，就返回它第一次出现的下标
```python
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello') #返回下标0
```
### 用`append()`和`insert()`方法在列表中添加值
+ `append()`方法调用，将参数添加到列表末尾
+ `insert()`方法可以在列表任意下标处插入一个值。`insert()`方法的第一个参数是新值的下标，第二个参数是要插入的新值
+ `append()`和`insert()`都不会将 列表 的新值作为其返回值（类似于void函数）
### 用`remove()`方法从列表中删除值
+ 给 `remove()`方法传入一个值，它将从被调用的列表中删除。
  ```python
  spam = ['zophie','fat','yellow']
  spam.remove('fat')
  ```
+ 如果该值在列表中出现多次，只有第一次出现的值会被删除
### 用`sort()`方法将列表中的值排序
+ 数值的列表或字符串的列表，能用 `sort()`方法排序
  ```python
  spam = [2, 5, 3.14, 1, -7]
  spam.sort()
  ```
+ 数值按照大小
+ 对字符串排序时，使用“ASCII 字符顺序”，而不是实际的字典顺序；这意味着大写字母排在小写字母之前。因此在排序时，**小写的a 在大写的Z 之后**
+ 如果需要按照普通的字典顺序来排序，就在sort()方法调用时，将关键字参数`key` 设置为`str.lower`
  ```python
  spam = ['a', 'z', 'A', 'Z']
  spam.sort(key=str.lower)
  ```
+ 同样无返回值
+ 也可以指定`reverse `关键字参数为`True`，让`sort()`按逆序排序。
  ```python
  spam.sort(reverse=True)
  spam
  ```
## 类似列表的类型：字符串和元组
### 元组数据类型
+ 元组输入时用圆括号`()`，而不是用方括号[]
+ 元组**不能**让它们的值被修改、添加或删除。
  `spam=('cat','name','fat')`
+ 如果元组中只有一个值，你可以在括号内该值的后面跟上一个逗号，表明这种情况。否则，Python 将认为，你只是在一个普通括号内输入了一个值。
### 用`list()`和`tuple()`函数来转换类型
```python
tuple(['cat', 'dog', 5])
list(('cat', 'dog', 5))
```
### 引用
```python
spam = 42
cheese = spam
pam = 100
```
spam和cheese
是不同的变量，保存了不同的值，改变spam或者cheese不会影响另一个值

但列表不是这样的。当你将列表赋给一个变量时，**实际上是将列表的“引用”赋给了该变量**。引用是一个值，指向某些数据。列表引用是指向一个列表的值
```python
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
```
代码只改变了cheese 列表，但似乎cheese 和spam 列表同时发生了改变
### `copy` 模块的`copy()`和`deepcopy()`函数
+ `copy.copy()`可以用来复制列表或字典这样的可变值，而不只是复制引用
  ```python
  import copy
  spam = ['A', 'B', 'C', 'D']
  cheese = copy.copy(spam)
  cheese[1] = 42
  ```
+ `deepcopy()`函数将同时复制它们内部的列表

# 字典和结构化数据
## 字典数据类型
+ 字典的索引可以使用许多不同数据类型，不只是整数。字典的索引被称为“键”，键及其关联的值
称为“键-值”对。
```python
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
myCat['size']
```
+ 不像列表，字典中的表项是不排序的,键-值对输入的顺序并不重要
+ 因为字典是不排序的，所以不能像列表那样切片
## `keys()`、`values()`和`items()`方法
+ 有3 个字典方法，它们将返回类似列表的值，分别对应于字典的键、值和键-值对：`keys()、values()和items()`。
+ 这些方法返回的值不是真正的列表，它们不能被修改，没有append()方法。但这些数据类型（分别是`dict_keys、dict_values 和dict_items`）可以用于for 循环。
## `get()`方法
+ ，它有两个参数：要取得其值的键，以及如果该键不存在时，返回的备用值。
+ 不使用get()，当访问一个不存在的键-值，代码就会产生一个错误消息
+ `dict.get(key,value)`
## setdefault()方法
+ 传递给该方法的第一个参数，是要检查的键。第二个参数，是如果该键不存在时要设置的值。如果该键确实存在，方法就会返回键的值
+ 与`get()`区别是：`get`只是返回值，并不更改/添加键-值，`setdefault`则是设置默认值（如果不存在）并返回`value`，若存在则返回`value`
## 漂亮打印
+ 导入`pprint` 模块，就可以使用`pprint()`和`pformat()`函数
+ 使用`pprint`输出字典等，输出的字典是有序的，但不影响原本字典的内容
+ 以下两行代码等价
  ```python
  pprint.pprint(someDictionaryValue)
  print(pprint.pformat(someDictionaryValue))
  ```

# 字符串操作
## 处理字符串
### 字符串可以用双引号开始和结束，就像用单引号一样。使用双引号的一个好处，就是字符串中可以使用单引号字符
### 转义字符
### 原始字符串
  + 在字符串开始的引号之前加上r，使它成为原始字符串。“原始字符串”完全忽略所有的转义字符，打印出字符串中所有的倒斜杠
### 用三重引号的多行字符串
  + 在Python 中，多行字符串的起止是3 个单引号或3 个双引号。“三重引号”之间的所有**引号、制表符或换行**，都被认为是字符串的一部分。Python 的代码块缩进规则不适用于多行字符串
### 多行注释
  + 单行注释 #
  + 多行注释 如同多行字符串 三重引号之间就是注释的内容
### 字符串下标和切片
+ 左闭右开
## 有用的字符串方法
### 字符串方法`upper()`、`lower()`、`isupper()`和`islower()`
+ `upper()`和`lower()`字符串方法返回一个新字符串，其中原字符串的所有字母都被相应地**转换为大写或小写**。字符串中**非字母字符保持不变**。
  + **这些方法没有改变字符串本身，而是返回一个新字符串**
+ 如果字符串至少有一个字母，并且所有字母都是大写或小写，`isupper()`和`islower()`方法就会相应地返回布尔值`True`。否则，该方法返回`False`
+ 因为`upper()`和`lower()`字符串方法本身返回字符串，所以也可以在“那些”返回的字符串上继续调用字符串方法。这样做的表达式看起来就像方法调用链
+ `isX` 字符串方法  
  还有几个字符串方法，它们的名字以 is 开始。这些方法返回一个布尔值，描述了字符串的特点
  + `isalpha()`返回`True`，如果字符串只包含字母，并且非空；
  + `isalnum()`返回`True`，如果字符串只包含字母和数字，并且非空；
  + `isdecimal()`返回`True`，如果字符串只包含数字字符，并且非空；
  + `isspace()`返回`True`，如果字符串只包含空格、制表符和换行，并且非空；
  + `istitle()`返回`True`，如果字符串仅包含以大写字母开头、后面都是小写字母的单词
### 字符串方法`startswith()`和`endswith()`
  + `startswith()`和`endswith()`方法返回`True`，如果它们所调用的字符串以该方法传入的字符串开始或结束。否则，方法返回`False`
### 字符串方法`join()`和`split()`
+ `join()`方法在一个字符串上调用，参数是一个字符串列表，返回一个字符串。返回的字符串由传入的列表中每个字符串连接而成
  ```python
  ', '.join(['cats', 'rats', 'bats']) #返回字符串
  ```
+ `plit()`方法做的事情正好相反：它针对一个字符串调用，返回一个字符串列表
  ```python
  'My name is Simon'.split()
  # 返回字符串列表，分割依据是单词间的空格
  ```
### 用`rjust()`、`ljust()`和`center()`方法对齐文本
+ `rjust()`和`ljust()`字符串方法**返回调用它们的字符串的填充版本**，通过插入空格（默认情况下）来对齐文本。
+ 这两个方法的第一个参数是一个整数长度，用于对齐字符串
+ 第二个可选参数将指定一个填充字符，取代空格字符
+ `center()`字符串方法与`ljust()`与`rjust()`类似，但它让文本居中，而不是左对齐或右对齐
### 用`trip()`、`rstrip()`和`lstrip()`删除空白字符
+ `strip()`字符串方法将**返回一个新的字符串**，它的开头或末尾都没有空白字符。
+ `lstrip()`和`rstrip()`方法将相应删除左边或右边的空白字符
+ 有一个可选的字符串参数，指定两边的哪些字符应该删除
  + 传入`strip()`方法的字符串中，**字符的顺序并不重要**
  ``python
  spam = 'SpamSpamBaconSpamEggsSpamSpam'
  spam.strip('ampS')
  ```
## 用pyperclip 模块拷贝粘贴字符串
+ `pyperclip`模块有`copy()`和`paste()`函数，可以向计算机的剪贴板发送文本，或从它接收文本
## 处理命令行参数 
+ 命令行参数将存储在变量sys.argv 中
  + python pw.py name 那么sys.argv[0] = 'pw.py'，sys.argv[1]='name'

# 模式匹配与正则表达式
## 用正则表达式查找文本模式
### 创建正则表达式对象
```python
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
```
+ 向`re.compile()`传入一个字符串值，表示正则表达式，它将返回一个`Regex` 模式对象（或者就简称为Regex 对象
### 匹配`Regex` 对象
+ `Regex` 对象的`search()`方法查找传入的字符串，寻找该正则表达式的所有匹配。如果字符串中没有找到该正则表达式模式，`search()`方法将返回`None`。如果找到了该模式，`search()`方法将返回一个`Match` 对象
+ `Match` 对象有一个`group()`方法，它返回被查找字符串中实际匹配的文本
  ```python
  phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
  mo = phoneNumRegex.search('My number is 415-555-4242.')
  print('Phone number found: ' + mo.group())
  ```
+ `group()`返回匹配到的内容
+ `group(0)`返回匹配到的内容
+ `group(1)`返回正则表达式中第一个括号内的内容，第一组
## 用正则表达式匹配更多模式
### 利用括号分组
+ 向`group()`匹配对象方法传入整数 1 或 2 ，就可以取得匹配文本的不同部分。
+ 向`group()`方法传入 0 或不传入参数，将返回整个匹配的文本
+ 如果想要一次就获取所有的分组，使用`groups()`方法，返回多个值的**元组**
### 用管道匹配多个分组
+ 字符 `|` 称为“管道”。希望匹配许多表达式中的一个时，就可以使用它
+ 第一次出现的匹配文本，将作为`Match` 对象返回。
### 用问号实现可选匹配
```python
batRegex = re.compile(r'Bat(wo)?man')
```
正则表达式中的`(wo)?`部分表明，模式  `wo` 是可选的分组。该正则表达式匹配的文本中，`wo` 将出现**零次或一次**
### 用星号匹配零次或多次
+ *（称为星号）意味着“匹配零次或多次”，即星号之前的分组，可以在文本中出现任意次。它可以完全不存在，或一次又一次地重复
### 用加号匹配一次或多次
+ 加号前面的分组必须“至少出现一次”
### 用花括号匹配特定次数
+ 如果想要一个分组重复特定次数，就在正则表达式中该分组的后面，跟上花括号包围的数字。例如，正则表达式`(Ha){3}`将匹配字符串`'HaHaHa'`，但不会匹配`'HaHa'`
+ 除了一个数字，还可以**指定一个范围**，即在花括号中写下一个最小值、一个逗号和一个最大值。例如，正则表达式`(Ha){3,5}`将匹配`'HaHaHa'`、`'HaHaHaHa'`和`'HaHaHaHaHa'`
+ 也可以不写花括号中的第一个或第二个数字，不限定最小值或最大值（类似于分片)
  比如`(Ha){3,}`将匹配3次或更多次
## 贪心和非贪心匹配
+ Python 的正则表达式默认是“贪心”的，这表示在有二义的情况下，它们会尽可能匹配最长的字符串。比如`(Ha){3,5}`遇到`'HaHaHaHaHa'`会返回`'HaHaHaHaHa'`即是匹配最长字符
+ 花括号的“非贪心”版本匹配尽可能最短的字符串，即在结束的花括号后跟着一个问号。
比如`(Ha){3,5}?`遇到`'HaHaHaHaHa'`会返回`'HaHaHa'`
## findall()方法
+ `findall()`方法将返回一组字符串，包含被查找字符串中的所有匹配
+ `findall()`不是返回一个`Match` 对象，而是返回**一个字符串列表**，只要在正则表达式中没有分组。
+ 如果在正则表达式中有分组，那么`findall` 将返回**元组的列表**。每个元组表示一个找到的匹配，其中的项就是正则表达式中每个分组的匹配字符串
## 字符分类
+ \d  0 到9 的任何数字
+ \D  除0 到9 的数字以外的任何字符
+ \w  任何字母、数字或下划线字符（可以认为是匹配“单词”字符）
+ \W  除字母、数字和下划线以外的任何字符
+ \s  空格、制表符或换行符（可以认为是匹配“空白”字符）
+ \S  除空格、制表符和换行符以外的任何字符 
## 建立自己的字符分类
+ 用方括号定义自己的字符分类
+ 使用短横表示字母或数字的范围
+ 在方括号内，普通的正则表达式符号不会被解释。这意味着，你不需要前面加上倒斜杠转义`.、*、?`或`()`字符
+ 通过在字符分类的左方括号后加上一个插入字符`^`，就可以得到“非字符类。非字符类将匹配不在这个字符类中的所有字符
  `^[ABSGHDH]`
## 插入字符和美元字符
+ 在正则表达式的开始处使用插入符号`^`，表明匹配必须发生在被查找文本开始处
+ 正则表达式的末尾加上美元符号`$`，表示该字符串必须以这个正则表达式的模式结束
## 通配字符
+  `.` （句点）字符称为“通配符”。它匹配**除**了换行之外的所有字符。
### 用点-星匹配所有字符
### 用句点字符匹配换行
+ 通过传入`re.DOTALL` 作为`re.compile()`的第二个参数，可以让句点字符匹配所有字符，包括换行字符。
## 不区分大小写的匹配
+ 。要让正则表达式不区分大小写，可以向`re.compile()`传入`re.IGNORECASE` 或`re.I`，作为第二个参数。
## 用`sub()`方法替换字符串
+ `Regex`对象的`sub()`方法需要传入两个参数。第一个参数是一个字符串，用于取代发现的匹配。第二个参数是一个字符串，即正则表达式。`sub()`方法**返回替换完成后的字符串**。
## 管理复杂的正则表达式
如果要匹配的文本模式很简单，正则表达式就很好。但匹配复杂的文本模式，可能需要长的、费解的正则表达式。你可以告诉`re.compile()`，忽略正则表达式字符串中的空白符和注释，从而缓解这一点。要实现这种详细模式，可以向`re.compile()`传入变量`re.VERBOSE`，作为第二个参数。
```python
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
```
**可以将正则表达式放在多行中，并加上注释**
```python
phoneRegex = re.compile(r'''(
  (\d{3}|\(\d{3}\))? # area code
  (\s|-|\.)? # separator
  \d{3} # first 3 digits
  (\s|-|\.) # separator
  \d{4} # last 4 digits
  (\s*(ext|x|ext.)\s*\d{2,5})? # extension
  )''', re.VERBOSE)
```
## 组合使用`re.IGNORECASE、re.DOTALL `和`re.VERBOSE`
+ `re.compile()`函数只接受一个值作为它的第二参数
+ 可以使用管道字符`（|）`将变量组合起来，从而绕过这个限制。管道字符在这里称为“按位或”操作符。

# 读写文件
## 文件与文件路径
### `Windows` 上的倒斜杠以及`OS X` 和`Linux` 上的正斜杠
+ 在`Windows` 上，路径书写使用**倒斜杠**作为文件夹之间的分隔符。
+ 在`OS X 和`Linux` 上，使用**正斜杠**作为它们的路径分隔符。
#### `os.path.join()`
+ 。如果将单个文件和路径上的文件夹名称的字符串传递给它，`os.path.join()`就会返回一个文件路径的字符串，包含正确的路径分隔符
```python
import os
os.path.join('usr', 'bin', 'spam')
## 结果是'usr\\bin\\spam'
```
### 当前工作目录
#### `os.getcwd()` 和 `os.chdir()`
可以取得当前工作路径的字符串，并可以利用`os.chdir()`改变它
### 绝对路径与相对路径
### 用`os.makedirs()`创建新文件夹
将创建所有必要的中间文件夹，目的是确保完整路径名存在
### `os.path` 模块
+ 导入 `import os`（`os.path` 是`os` 模块中的模块，）
### 处理绝对路径和相对路径
`os.path` 模块提供了一些函数，返回一个相对路径的绝对路径，以及检查给定的路径是否为绝对路径。
+ 调用 `os.path.abspath(path)`将返回参数的绝对路径的字符串。这是将相对路径转换为绝对路径的简便方法。
+ 调用 `os.path.relpath(path, start)`将返回从`start` 路径到`path` 的相对路径的字符串。如果没有提供`start`，就使用当前工作目录作为开始路径。
+ 调用 `os.path.isabs(path)`，如果参数是一个绝对路径，就返回`True`，如果参数是一个相对路径，就返回`False`。
+ **基本名称**跟在路径中最后一个斜杠后，它和文件名一样
+ **目录名称**是最后一个斜杠之前的所有内容 
+ 调用 `os.path.dirname(path)`将返回一个字符串，它包含`path` 参数中最后一个斜杠之前的所有内容。
+ 调用`os.path.basename(path)`将返回一个字符串，它包含`path` 参数中最后一个斜杠之后的所有内容。
+ 如果同时需要一个路径的目录名称和基本名称，就可以调用`os.path.split()`，获得这两个字符串的元组
+ `os.path.split()`不会接受一个文件路径并返回每个文件夹的字符串的列表。如果需要这样，请使用`split()`字符串方法，并根据`os.path.sep` 中的字符串进行分割
  + `split()`字符串方法将返回一个**列表**，包含该路径的所有部分。如果向它传递`os.path.sep`，就能在所有操作系统上工作。 
  ```python 
  calcFilePath = 'C:\\Windows\\System32\\calc.exe'
  calcFilePath.split(os.path.sep)
  # 默认情况下 os.path.seq 会自动根据PC来适应
  ```
### 查看文件大小和文件夹内容
`os.path` 模块提供了一些函数，用于查看文件的字节数以及给定文件夹中的文件和子文件夹。
+ 调用 `os.path.getsize(path)`将返回`path` 参数中文件的字节数
+ 调用 `os.listdir(path)`将返回文件名字符串的**列表**，包含`path` 参数中的每个文件（请注意，这个函数在`os` 模块中，而不是`os.path`）
+ 调用`os.walk()`函数列出文件夹以及子文件夹中的每个文件
### 检查路径有效性
+ 如果 `path` 参数所指的文件或文件夹存在，调用`os.path.exists(path)`将返回`True`，否则返回`False`。
+ 如果 `path` 参数存在，并且是一个文件，调用`os.path.isfile(path)`将返回`True`，否则返回`False`。
+ 如果 `path` 参数存在，并且是一个文件夹，调用`os.path.isdir(path)`将返回`True`，否则返回`False`。
## 文件读写过程
+ 1. 调用open()函数，返回一个File 对象。
  2. 调用File 对象的read()或write()方法。
  3. 调用File 对象的close()方法，关闭该文件。
或者
+ ```python
  with open(path) as name:
    # 各种文件对象的操作代码
  ```
  等价于
  ```python
  file = open(path)
  # 各种文件对象的操作代码
  file.close()
  ```
### 用`open()`函数打开文件
传递的字符串路径可以是绝对路径，也可以是相对路径。`open()`函数返回一个`File` 对象。
+ 默认是只读的形式打开
+ 要进行写入操作，传入第二个参数'w'等
### 读取文件内容
+ `helloContent = helloFile.read()`将整个文件的内容读取为**一个字符串**值
+ 使用`readlines()`方法，从该文件取得一个字符串的列表。列表中的每个字符串就是文本中的每一行
### 写入文件
要以“**写入纯文本模式**”或“**添加纯文本模式**”打开该文件，或简称为“写模式”和“添加模式”。
+ 写模式将覆写原有的文件，从头开始;将`'w'`作为第二个参数传递给`open()`
+ 将`'a'`作为第二个参数传递给`open()`，以添加模式打开该文件
+ 如果传递给`open()`的文件名不存在，写模式和添加模式都会创建一个新的空文件。在读取或写入文件后，调用`close()`方法，然后才能再次打开该文件。
## 用`shelve` 模块保存变量
+ 利用`shelve` 模块，你可以将Python 程序中的变量保存到二进制的`shelf` 文件中。
```python
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
```
+ 就像字典一样，`shelf` 值有`keys()`和`values()`方法，返回`shelf` 中键和值的类似列表的值。因为这些方法返回类似列表的值，而**不是真正的列表**，所以应该将它们传递给`list()`函数，取得列表的形式
## 用`pprint.pformat()`函数保存变量

# 组织文件
## `shutil`模块
### 复制文件和文件夹
#### `shutil.copy(source,destination)` 复制文件
+ 调用`shutil.copy(source, destination)`，将路径`source` 处的文件复制到路径`destination`处的文件夹（`source` 和`destination` 都是字符串）。
+ 如果`destination` 是一个文件名，它将作为被复制文件的新名字。
+ 该函数返回一个字符串，表示被复制文件的路径
#### `shutil.copytree(source,destination)` 复制文件夹
+ 调用`shutil.copytree(source, destination)`，将路径`source` 处的文件夹，包括它的所有文件和子文件夹，复制到路径`destination` 处的文件夹。
+ `source` 和`destination` 参数都是字符串。
+ 该函数返回一个字符串，是新复制的文件夹的路径
### 文件和文件夹的移动与改名
+ 调用`shutil.move(source, destination)`，将路径`source` 处的文件夹移动到路径`destination`，并返回新位置的绝对路径的字符串。
+ 如果 `destination` 指向一个文件夹，`source` 文件将移动到`destination` 中，并保持原来的文件名
+ 如果已经存在一个文件，它就会被覆写
### 永久删除文件和文件夹
+ 用 `os.unlink(path)`将删除`path` 处的文件。
+ 调用 `os.rmdir(path)`将删除`path` 处的文件夹。**该文件夹必须为空**，其中没有任何文件和文件夹。
+ 调用 `shutil.rmtree(path)`将删除`path` 处的文件夹，它包含的所有文件和文件夹都会被删除。
### 用`send2trash` 模块安全地删除，可以在回收站找到
+ `send2trash(path)`
## 用`zipfile` 模块压缩文件
### 读取`ZIP`文件
```python
import zipfile
wxampleZip = zipfile.ZipFile(path)
exampleZip.namelist()

spamInfo = exampletZip.getinfo(file)
spamInfo.file_size
spamInfo.compress_size
```
+ `namelist()`方法返回`ZIP`文件中包含的所有文件和文件夹的字符串的列表
+ 这些字符串可以传递给`ZipFile` 对象的`getinfo()`方法，返回一个关于特定文件的`ZipInfo` 对象。`ZipInfo` 对象有自己的属性，诸如表示字节数的`file_size`和`compress_size`，它们分别表示原来文件大小和压缩后文件大小
+ `ZipFile` 对象表示整个归档文件，而`ZipInfo` 对象则保存该归档文件中每个文件的有用信息
### 解压缩
+ `ZipFile`对象的`extractall()`方法
```pthon
exampleZip.extractall()
# 解压到工作目录
exampleZip.extractall(path)
# 解压到指定目录下
```
### 创建和添加到`ZIP` 文件
+ 必须以“写模式”打开`ZipFile` 对象，即传入`'w'`作为第二个参数
```python
import zipfile
exampleZip = zipfile.ZipFile(path,'w')
exampleZip.write(path,compress_type=zipfile.ZIP_DEFAULTED)
exampleZip.close()
```
### 将一个文件夹备份到一个`ZIP` 文件
+ 递归添加到`ZIP`文件里面
 + `os.walk()` 

# 调试
## 抛出异常
+ 抛出异常使用`raise` 语句。
  + `raise` 关键字；
  + 对 `Exception` 函数的调用；
  + 传递给`Exception` 函数的字符串，包含有用的出错信息。
```python
def boxPrint(symbol, width, height):
  if len(symbol) != 1:
    raise Exception('Symbol must be a single character string.')
  if width <= 2:
    raise Exception('Width must be greater than 2.')
  if height <= 2:
    raise Exception('Height must be greater than 2.')
  print(symbol * width)
  for i in range(height - 2):
    print(symbol + (' ' * (width - 2)) + symbol)
  print(symbol * width)
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
  try:
    boxPrint(sym, w, h)
  except Exception as err:
    print('An exception happened: ' + str(err))
```
+ 这个程序使用了`except` 语句的`except Exception as err` 形式。如果`boxPrint()`返回一个`Exception` 对象，这条语句就会将它保存在名为`err` 的变量中。`Exception` 对象可以传递给`str()`，将它转换为一个字符串，得到用户友好的出错信息
## 取得反向跟踪的字符串
+ 只要抛出的异常没有被处理，`Python` 就会显示反向跟踪。但你也可以调用`traceback.format_exc()`，得到它的字符串形式。
+ 如果你希望得到异常的反向跟踪的信息，但也希望`except` 语句优雅地处理该异常，这个函数就很有用
+ 需要导入`traceback` 模块。
```python
import traceback
try:
  raise Exception('This is the error message.')
except:
  errorFile = open('errorInfo.txt', 'w')
  errorFile.write(traceback.format_exc())
  errorFile.close()
  print('The traceback info was written to errorInfo.txt.')
# 将反向跟踪信息写入一个日志文件，并让程序继续运行
```
## 断言
+ `assert`语句包含以下部分：
  `assert` 关键字；
  条件（即求值为`True` 或`False` 的表达式）；
  逗号；
  当条件为`False` 时显示的字符串。
+ 当某些语句要在特定条件下才算正确执行，`assert`用在此处，可以让我们知道这里的运行条件不符合我们的预期（即便这些语句能够正常运行）
```python
  podBayDoorStatus = 'open'
  assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
  podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can't do that.''
  assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
  # 第二行不会抛出异常，字符串的值符合设定；第四行抛出异常，字符串的值不符合设定
```
### 禁用断言
+ 在运行`Python` 时传入`-O` 选项，可以禁用断言。
+ 参考附录B
## 日志
记日志是一种很好的方式，可以理解程序中发生的事，以及事情发生的顺序。`Python` 的`logging` 模块使得你很容易创建自定义的消息记录。这些日志消息将描述程序执行何时到达日志函数调用，并列出你指定的任何变量当时的值。另一方面，缺失日志信息表明有一部分代码被跳过，从未执行。
### 使用日志模块
+ 要启用`logging` 模块，在程序运行时将日志信息显示在屏幕上，请将下面的代码复制到**程序顶部（但在`Python` 的`#!`行之下）**：
```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s
- %(message)s')
```
+ 打印日志信息时，使用 `logging.debug()` 函数
+ 这个 `debug()`函数将调用`basicConfig()`，打印一行信息。这行信息的格式是我们在`basicConfig()`函数中指定的，并且包括我们传递给`debug()` 的消息。
```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s
- %(message)s')
logging.debug('Start of program')
def factorial(n):
  logging.debug('Start of factorial(%s%%)' % (n))
  total = 1
  for i in range(n + 1):
    total *= i
    logging.debug('i is ' + str(i) + ', total is ' + str(total))
  logging.debug('End of factorial(%s%%)' % (n))
  return total
print(factorial(5))
logging.debug('End of program')
```
+ 加入一次`logging.disable(logging.CRITICAL)`调用，就可以禁止日志
### 日志级别
|    级别    |             日志函数 |                              描述                              |
| :--------: | -------------------: | :------------------------------------------------------------: |
|  `DEBUG`   |    `logging.debug()` | 最低级别。用于小细节。通常只有在诊断问题时，你才会关心这些消息 |
|   `INFO`   |     `logging.info()` |        用于记录程序中一般事件的信息，或确认一切工作正常        |
| `WARNING`  |  `logging.warning()` |     用于表示可能的问题，它不会阻止程序的工作，但将来可能会     |
|  `ERROR`   |    `logging.error()` |               用于记录错误，它导致程序做某事失败               |
| `CRITICAL` | `logging.critical()` |                             最高级                             |
+ 日志级别的好处在于，你可以改变想看到的日志消息的优先级
+ 向`basicConfig()`函数传入`logging.DEBUG` 作为`level` 关键字参数，这将显示所有日志级别的消息（`DEBUG`是最低的级别）
+ 将`basicConfig()` 的 `level` 参数设置为`logging.ERROR`，这将只显示`ERROR`和`CRITICAL` 消息
### 禁用日志
+ 只要向`logging.disable()` 传入一个日志级别，它就会**禁止该级别和更低级别**的所有日志消息
### 将日志记录到文件
+ `logging.basicConfig()` 函数接受`filename` 关键字参数
```python
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# 日志信息将被保存到myProgramLog.txt 文件中
```

# 从Web 抓取信息
+ `webbrowser`：是Python 自带的，打开浏览器获取指定页面。
+ `requests`：从因特网上下载文件和网页。
+ `Beautiful Soup`：解析HTML，即网页编写的格式。
+ `selenium`：启动并控制一个`Web`浏览器。`selenium`能够填写表单，并模拟鼠标在这个浏览器中点击。
##`webbrowser` 模块
```python
  import webbrowser
  webbrowser.open('http://inventwithpython.com/')
```
## 用`requests` 模块从`Web` 下载文件
### 用`requests.get()`函数下载一个网页
```python
import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(res.text[:250])
```
+ 。通过检查`Response` 对象的`status_code` 属性，你可以了解对这个网页的请求是否成功。如果该值等于`requests.codes.ok`，那么一切都好（顺便说一下，`HTTP`协议中“`OK`”的状态码是`200`。你可能已经熟悉`404` 状态码，它表示“没找到”）
+ 如果请求成功，下载的页面就作为一个字符串，保存在`Response` 对象的`text`变量中
### 检查错误
+ 。检查成功有一种简单的方法，就是在`Response`对象上调用`raise_for_status()`方法。如果下载文件出错，这将抛出异常。如果下载成功，就什么也不做。
### 将下载的文件保存到硬盘
+ 必须用“写二进制”模式打开该文件，即向函数传入字符串`'wb'`，作为`open()`的第二参数。
+ 目的是为了保存该文本中的“`Unicode` 编码”。
## 用`BeautifulSoup` 模块解析`HTML`
### 从`HTML` 创建一个`BeautifulSoup` 对象
```python
import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
# 将响应结果的text 属性传递给bs4.BeautifulSoup()
```
+ 也可以向`bs4.BeautifulSoup()`传递一个`File` 对象，从硬盘加载一个`HTML` 文件
```python
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
```
### 用`select()`方法寻找元素
| 传递给 `select()`方法的选择器         | 将匹配…                                                       |
| ------------------------------------- | ------------------------------------------------------------- |
| `soup.select('div')`                  | 所有名为`<div>`的元素                                         |
| `soup.select('#author')`              | 带有 `id` 属性为`author` 的元素                               |
| `soup.select('.notice')`              | 所有使用`CSS class` 属性名为`notice` 的元素                   |
| `soup.select('div span')`             | 所有在`<div>`元素之内的`<span>`元素                           |
| `soup.select('div > span')`           | 所有直接在<div>元素之内的`<span>`元素，中间没有其他元素       |
| `soup.select('input[name]')`          | 所有名为`<input>`，并有一个`name` 属性，其值无所谓的元素      |
| `soup.select('input[type="button"]')` | 所有名为`<input>`，并有一个`type` 属性，其值为`button` 的元素 |
+ `select()`返回一个列表，列表中元素为`Tag`对象。在该元素上调用`getText()`方法，返回该元素的文本，或内部的`HTML`。一个元素的文本是在开始和结束标签之间的内容
+ `Tag` 对象的`get()`方法让我们很容易从元素中获取属性值。向该方法传入一个属性名称的字符串，它将返回该属性的值。
## 用`selenium` 模块控制浏览器
需要安装`driver`驱动
对于`chrome`浏览器
```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://inventwithpython.com')
# 将浏览器指向该网址
```
### 在页面中寻找元素
+ `WebDriver` 对象有好几种方法，用于在页面中寻找元素。它们被分成`find_element_*`和`find_elements_*`方法，前者返回一个对象，后者返回一个列表

| 方法名                                                                                                  | 返回的WebElement 对象/列表                                     |
| ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| `browser.find_element_by_class_name(name)` <br>`browser.find_elements_by_class_name(name)`              | 使用 `CSS` 类`name` 的元素                                     |
| `browser.find_element_by_css_selector(selector)`<br>`browser.find_elements_by_css_selector(selector)`   | 匹配 `CSS selector` 的元素                                     |
| `browser.find_element_by_id(id)`<br>`browser.find_elements_by_id(id)`                                   | 匹配 `id` 属性值的元素                                         |
| `browser.find_element_by_link_text(text)`<br>`browser.find_elements_by_link_text(text)`                 | 完全匹配提供的`text` 的`<a>`元素                               |
| `browser.find_element_by_partial_link_text(text)`<br>`browser.find_elements_by_partial_link_text(text)` | 包含提供的`text` 的`<a>`元素                                   |
| `browser.find_element_by_name(name)`<br>`browser.find_elements_by_name(name)`                           | 匹配 `name` 属性值的元素                                       |
| `browser.find_element_by_tag_name(name)`<br>`browser.find_elements_by_tag_name(name)`                   | 匹配标签`name` 的元素`<br>`(大小写无关，`<a>`元素匹配'a'和'A') |
### 点击页面
+ `find_element_*`和`find_elements_*`方法返回的`WebElement` 对象有一个`click()`方法，模拟鼠标在该元素上点击
```python
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read It Online')
type(linkElem)
linkElem.click() # follows the "Read It Online" link
```
### 填写并提交表单
+ 向`Web` 页面的文本字段发送击键，只要找到那个文本字段的`<input>`或`<textarea>`元素，然后调用`send_keys()`方法。
```python
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://gmail.com')
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('not_my_real_email@gmail.com')
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('12345')
passwordElem.submit()
```
+ 在任何元素上调用`submit()`方法，都等同于点击该元素所在表单的`Submit` 按钮
### 发送特殊键
+ 这些值保存在`selenium.webdriver.common.keys` 模块的属性中

| 属性                                            | 含义                                     |
| ----------------------------------------------- | ---------------------------------------- |
| Keys.DOWN, Keys.UP, Keys.LEFT,Keys.RIGHT        | 键盘箭头键                               |
| Keys.ENTER, Keys.RETURN                         | 回车和换行键                             |
| Keys.HOME, Keys.END,Keys.PAGE_DOWN,Keys.PAGE_UP | Home 键、End 键、PageUp 键和Page Down 键 |
| Keys.ESCAPE, Keys.BACK_SPACE,Keys.DELETE Esc、  | Backspace 和字母键                       |
| Keys.F1, Keys.F2, . . . , Keys.F12              | 键盘顶部的F1 到F12 键                    |
| Keys.TAB                                        | Tab 键                                   |
### 点击浏览器按钮
`browser.back()`点击“返回”按钮。
`browser.forward()`点击“前进”按钮。
`browser.refresh()`点击“刷新”按钮。
`browser.quit()`点击“关闭窗口”按钮。

# 处理Excel 电子表格
## `openpyxl`

# 处理PDF 和Word 文档
## PyPDF2
## docx

# 处理CSV 文件和JSON 数据
## csv 模块
## json模块

# 保持时间、计划任务和启动程序
+ `time` 和`datetime` 模块
+ 利用`subprocess` 和`threading` 模块，你也可以编程按时启动其他程序
## `time` 模块
### `time.time()`函数
+ `Unix` 纪元是编程中经常参考的时间：1970 年1 月1 日0 点，即协调世界时`（UTC）`
+ `time.time()`函数返回自那一刻以来的秒数，是一个浮点值，这个数字称为`UNIX` 纪元时间戳
```python
import time
time.time()
```
### `time.sleep()`函数
+ 暂停程序
+ ，在`IDLE` 中按`Ctrl-C` 不会中断`time.sleep()`调用。`IDLE` 会等待到暂停结束，再抛出`KeyboardInterrupt` 异常
## `datetime` 模块
+ `datetime` 模块有自己的`datetime` 数据类型。`datetime` 值表示一个特定的时刻
+ 调用`datetime.datetime.now()`返回一个`datetime` 对象，表示当前的日期和时间，根据你的计算机的时钟。这个对象包含当前时刻的年、月、日、时、分、秒和微秒
+ 也可以利用`datetime.datetime()`函数，向它传入代表年、月、日、时、分、秒的整数，得到特定时刻的`datetime` 对象。这些整数将保存在`datetime` 对象的`year、month、day、hour、minute `和`second`属性中。
+ `Unix` 纪元时间戳可以通过`datetime.datetime.fromtimestamp()`，转换为`datetime`对象
### `timedelta` 数据类型
+ `datetime` 模块还提供了`timedelta` 数据类型，它表示一段时间，而不是一个时刻。
+ `datetime.timedelta()`函数接受关键字参数`weeks、days、hours、minutes、seconds、milliseconds 和microseconds`。没有`month 和yea`r 关键字参数，因为“月”和“年”是可变的时间
+ `total_seconds()`方法返回只以秒表示的时间
+ 算术运算符可以用于对`datetime` 值进行日期运算
```python
dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)
dt + thousandDays
# datetime.datetime(2017, 11, 23, 18, 38, 50, 636181)
```
### 将`datetime` 对象转换为字符串
+ `strftime()`
| strftime指令 | 含义，                                                              |
| ------------ | ------------------------------------------------------------------- |
| %Y           | 带世纪的年份，例如'2014'，                                          |
| %y           | 不带世纪的年份，'00'至'99'（1970 至2069），00'至'99'（1970 至2069） |
| %m           | 数字表示的月份，'01'至'12'，01'至'12'                               |
| %B           | 完整的月份，例如'November'，                                        |
| %b           | 简写的月份，例如'Nov'，                                             |
| %d           | 一月中的第几天，'01'至'31'，                                        |
| %j           | 一年中的第几天，'001'至'366'，                                      |
| %w           | 一周中的第几天，'0'（周日）至'6'（周六），                          |
| %A           | 完整的周几，例如'Monday'，                                          |
| %a           | 简写的周几，例如'Mon'，                                             |
| %H           | 小时（24 小时时钟），'00'至'23'，                                   |
| %I           | 小时（12 小时时钟），'01'至'12'，                                   |
| %M           | 分，'00'至'59'，                                                    |
| %S           | 秒，'00'至'59'，                                                    |
| %p           | 'AM'或'PM'，                                                        |
| %%           | 就是'%'字符，                                                       |
+ 向`strftime()`传入一个定制的格式字符串，其中包含格式化指定（以及任何需要的斜线、冒号等），`strftime()`将返回一个格式化的字符串，表示`datetime` 对象的信息。
```python
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
oct21st.strftime('%Y/%m/%d %H:%M:%S')
# '2015/10/21 16:29:00'
oct21st.strftime('%I:%M %p')
# '04:29 PM'
oct21st.strftime("%B of '%y")
# "October of '15"
```
### 将字符串转换成`datetime` 对象
```python
datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
# datetime.datetime(2015, 10, 21, 0, 0)
datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
# datetime.datetime(2015, 10, 21, 16, 29)
datetime.datetime.strptime("October of '15", "%B of '%y")
# datetime.datetime(2015, 10, 1, 0, 0)
datetime.datetime.strptime("November of '63", "%B of '%y")
# datetime.datetime(2063, 11, 1, 0, 0)
```
## 多线程
### 创建一个`Thread` 对象
```python
import threading
def takeANap():
  time.sleep(5)
  print('Wake up!')
threadObj = threading.Thread(target=takeANap)
threadObj.start()
```
### 向线程的目标函数传递参数
```pythpn
import threading
threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'],kwargs={'sep': ' & '})
```
## 从`Python` 启动其他程序
+ `subprocess` 模块
```python
import subprocess
subprocess.Popen('C:\\Windows\\System32\\calc.exe')
```
### `Popen`对象
+ `poll()和wait()`
+ 如果这个进程在`poll()`调用时仍在运行，`poll()`方法就返回`None`。如果该程序已经终止，它会返回该进程的整数退出代码。退出代码用于说明进程是无错终止（退出代码为0），还是一个错误导致进程终止（退出代码非零，通常为1，但可能根据程序而不同）。
+ `wait()`方法将阻塞，直到启动的进程终止
### 向`Popen()`传递命令行参数
+ 向`Popen()`传递一个列表，作为唯一的参数。该列表中的第一个字符串是要启动的程序的可执行文件名，所有后续的字符串将是该程序启动时，传递给该程序的命令行参数。实际上，这个列表将作为被启动程序的`sys.argv` 的值。
```python
subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\hello.txt'])
```
### 用默认的应用程序打开文件
+ 根据操作系统，向`Popen()传入'start'、'open'或'see'`，分别代表`windows、OS X、Linux`
```python
fileObj = open('hello.txt', 'w')
fileObj.write('Hello world!')
# 12
fileObj.close()
import subprocess
subprocess.Popen(['start', 'hello.txt'], shell=True)
# 传入了shell=True 关键字参数，这只在Windows 上需要
```
# 发送电子邮件和短信
# 操 作 图 像
## `pillow`模块
### 颜色和`RGBA` 值
+ `RGBA`值是一组数字，指定顔色中的**红、绿、蓝和`alpha`（透明度）**的值。这些值是从0（根本没有）到255（最高）的整数
+ 在`Pillow`中，`RGBA`值表示为四个整数值的元组。例如，红色表示为（255，0，0，255）。这种颜色中红的值为最大，没有绿和蓝，并且`alpha`值最大，这意味着它完全不透明。
+ 如果颜色的`alpha`值为0，不论`RGB`值是什么，该颜色是不可见的
+ `Pillow`提供`ImageColor.getcolor()`函数，该函数接受一个颜色名称字符串作为第一个参数，字符串'RGBA'作为第二个参数，返回一个RGBA元组
```python
from PIL import ImageColor
ImageColor.getcolor('red', 'RGBA')
# (255, 0, 0, 255)
ImageColor.getcolor('RED', 'RGBA')
# (255, 0, 0, 255)
ImageColor.getcolor('Black', 'RGBA')
# (0, 0, 0, 255)
ImageColor.getcolor('chocolate', 'RGBA')
# (210, 105, 30, 255)
ImageColor.getcolor('CornflowerBlue', 'RGBA')
# (100, 149, 237, 255)
```
### 坐标和`Box`元组
+ 图像像素用`x`和`y`坐标指定，分别指定像素在图像中的水平和垂直位置。原点是位于图像左上角的像素，用符号`(0，0)`指定
+ 许多Pillow函数和方法需要一个矩形元组参数。这意味着Pillow需要一个四个整坐标的元组，表示图像中的一个矩形区域。四个整数按顺序分别是：
  + 左：该矩形的最左边的x坐标
  + 顶：该矩形的顶边的y坐标。
  + 右：该矩形的最右边右面一个像素的x坐标。此整数必须比左边整数大。
  + 底：该矩形的底边下面一个像素的y坐标。此整数必须比顶边整数大。注意，该矩形包括左和顶坐标，直到但不包括右和底坐标。
## 用 `Pillow`操作图像
### `Image`模块
+ `Image.open()`函数的返回值是`Image`对象数据类型
```python
from PIL import Image
catIm = Image.open(path)
```
### 处理 `Image`数据类型
```python
from PIL import Image
catIm = Image.open('zophie.png')
catIm.size
# (816, 1088)
width, height = catIm.size
width
# 816 
height
# 1088 
catIm.filename
# 'zophie.png'
catIm.format
# 'PNG'
catIm.format_description
# 'Portable network graphics'
atIm.save('zophie.jpg')
```
+  `Image.new()`函数，它返回一个 `Image`对象,对象表示空白的图像。
```python
from PIL import Image
im = Image.new('RGBA',(100,200),'purple')
# 100像素宽，200像素高，带有紫色背景
im.save(path)
im2 = Image.new('RGBA',(20,20))
im2.save(path)
```
### 裁剪图片
+ `Image`对象的`crop()`方法，接受一个元组，返回一个`Image`对象，表示被裁剪后的图像
### 复制和粘贴图像到其他图像
```python
catCopy.paste(Image,(x,y))
```
### 调整图像大小
+ `resize()`方法在`Image`对象上调用，回指定宽度和高度的一个新`Image`对象，它接受两个整数的元组作为参数，表示返回图像的新高度和宽度。
### 旋转和翻转图像
+ `Image`对象的`rotate()`旋转图像，返回旋转后的新`Image`对象
```python
catIm.rotate(90).save(path)
# 旋转90°
```
### 更改单个像素
```python
im.getpixel((x,y))
im.getpixel((x,y),(R,G,B))
```
## 在图像上绘画
+ `Pillow`的`ImageDraw`模块
+ `ImageDraw`对象
```python
from PIL import Image,ImageDraw
im = Image.new(RGBA,(x,y),color)
draw = ImageDraw.Draw(im)
draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
```
### 绘制形状
+ **这些方法的`fill`和`outline`参数是可选的，如果未指定，默认为白色。**  
|  形状  |              函数              |                                                                                             注意                                                                                             |
| :----: | :----------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|   点   |       `point((xy),fill)`       |                            `xy`表示`x和y`坐标的列表，例如`[(x,y),(x,y)...]`和`[x,y,x,y...]`<br>`fill`参数是点的颜色，要么是一个`RGBA`元组，要么是颜色名称的字符串                            |
|   线   |    `line((xy),fill,width)`     | `xy`表示`x和y`坐标的列表，例如`[(x,y),(x,y)...]`和`[x,y,x,y...]`<br>`fill`参数是点的颜色，要么是一个`RGBA`元组，要么是颜色名称的字符串<br>可选的`width`参数是线的宽度，如果未指定，缺省值为1 |
|  矩形  | `rectangle((xy),fill,outline)` |                        `xy`参数是一个矩形元组，形式为`(left, top,  right,  bottom)`<br>选的`fill`参数是颜色，将填充该矩形的内部。可选的`outline`参数是矩形轮廓的颜色                         |
|  椭圆  |      `ellipse((xy),fill)`      |                   `xy`参数是一个矩形元组`(left, top, right, bottom)`，它表示正好包含该椭圆的矩形。<br>可选的fill参数是椭圆内的颜色，<br>可选的outline参数是椭圆轮廓的颜色                    |
| 多边形 |      `polygon((xy),fill)`      |                                                                                            同矩形                                                                                            |
### 绘制文本
ImageDraw对象还有text()方法，用于在图像上绘制文本。text()方法有4个参数：`xy、text、fill和font`
+ `xy`参数是两个整数的元组，指定文本区域的左上角
+ `text`参数是想写入的文本字符串
+ 可选参数`fill`是文本的颜色
+ 可选参数`font`是一个`ImageFont`对象，用于设置文本的字体和大小。需要导入`ImageFont`模块
+ 导入`Pillow`的`ImageFont`模块，就可以调用`ImageFont.truetype()`函数，它有两个参数。第一个参数是字符串，表示字体的`TrueType`文件，这是硬盘上实际的字体文件
+ 第二个参数是一个整数，表示字体大小的点数（而不是像素）。请记住，`Pillow`创建的`PNG`图像默认是每英寸72像素，一点是1/72英寸
```python
from PIL import Image, ImageDraw, ImageFont
import os
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
draw.text((20, 150), 'Hello', fill='purple')
fontsFolder = 'FONT_FOLDER' # e.g. ‘/Library/Fonts’
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
im.save('text.png')
```

# 用`GUI`自动化控制键盘和鼠标
+ `pyautogui`模块
## 走对路
### 通过注销关闭所有程序
+ 在`Windows`和`Linux`上，注销的热键是`Ctrl-Alt-Del`。
### 暂停和自动防故障装置
+ 将`pyautogui.PAUSE`变量设置为要暂停的秒数,每个`PyAutoGUI`函数调用在执行动作之后，都会等待指定的时间
+ ·pyautogui·也有自动防故障功能。将鼠标移到屏幕的左上角，这将导致`pyautogui`产生`pyautogui  .FailSafeException`异常
+ 如果你尽可能快地向左上移动鼠标，自动防故障功能都将停止程序;可以设置`pyautogui.FAILSAFE = False`，禁止这项功能。
## 控制鼠标移动
+ `pyautogui.size()`函数返回两个整数的元组，包含屏幕的宽和高的像素数
### 移动鼠标
+ `pyautogui.moveTo(x,y,duration)`;`(x,y)`表示移动的目的地位置，可选的`duration`整数或浮点数关键字参数，指定了将鼠标移动到目的地所需要的秒数
```python
import pyautogui
pyautogui.moveTo(100,100,duration=0.25)
```
+ `pyautogui.moveRel()`函数相对于**当前的位置**移动鼠标
```python
pyautogui.moveRel(100,100,duration=0.25)
```
### 获取鼠标位置
+ 通过调用`pyautogui.position()`函数，可以确定鼠标当前的位置
## 控制鼠标交互
### 点击鼠标
+ 鼠标点击`pyautogui.click()`
```python
pyautogui.click(x,y,botton='left')
pyautogui.click(x,y,botton='middle')
pyautogui.click(x,y,botton='right')
```
+ `pyautogui.mouseDown()`按下鼠标按键，不松开
+ `pyautogui.mouseUp()`松开鼠标按键
+ `pyautogui.doubleClick()`函数只执行双击鼠标左键。
+ `pyautogui.rightClick()`和`pyautogui.middleClick()`函数将分别执行双击右键和双击中键
### 拖动鼠标
+ `pyautogui.dragTo()`和`pyautogui.dragRel()`（移动到新的位置或者相对当前位置的位置）
+ `x`坐标/水平移动，`y`坐标/垂直移动，以及可选的时间间隔
### 滚动鼠标
+ `scroll()`滚动发生在鼠标的当前位置。传递正整数表示向上滚动，传递负整数表示向下滚动。
## 处理屏幕
+ `pyautogui`拥有屏幕快照的功能，可以根据当前屏幕的内容创建图形文件。这些函数也可以返回一个`Pillow`的`Image`对象，包含当前屏幕的内容
### 获取屏幕快照
```python
import pyautogui
from PIL import Image
im = pyautogui.screenshot()
```
### 分析屏幕快照
+ 如果屏幕上指定的`x、y`坐标处的像素与指定的颜色匹配，`PyAutoGUI`的`pixelMatchesColor()`函数将返回`True`
## 控制键盘
### 通过键盘发送一个字符串
+ `pyautogui.typewrite()`函数向计算机发送虚拟按键
```python
pyautogui.typewrite（'Helloworld!',0.25）
```
### 键名
+ `pyautogui.KEYBOARD_KEYS`
```python
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])
```
### 按下和释放键盘
+ 就像`mouseDown()和mouseUp()`函数一样，`pyautogui.keyDown()和pyautogui.keyUp()`将向计算发送虚拟的按键和释放。同样也有`pyautogui.press()`函数调用上述两个函数，模拟完整的击键
```python
pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')
```
### 热键组合
```python
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')
```
+ 上述操作复杂，可以使用`pyautogui.hotkey(`)`函数,它接受多个键字符串参数，按顺序按下，再按相反的顺序释放
```python
pyautogui.hotkey('ctrl', 'c')
```
