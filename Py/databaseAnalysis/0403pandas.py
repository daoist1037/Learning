# -*- coding: utf-8 -*-
import pandas as pd

s = pd.Series([1,2,3],index=['a','b','c'])
d = pd.DataFrame([[1,2,3],[4,5,6]],columns=['a','b','c'])
d2 = pd.DataFrame(s)

d.head()
d.describe()

pd.read_excel('test_bonjean.xls')