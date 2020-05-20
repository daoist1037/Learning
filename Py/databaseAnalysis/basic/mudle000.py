import hmac
import hashlib
# 可见，摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。

# 摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。

# 我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())
