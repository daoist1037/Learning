#%%
import pandas as pd 
import numpy as np
frame = pd.Series(['a', 'b', 'c', 'd'])
frame.to_excel('a.xlsx')
# %%
import sqlite3
query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
c REAL, d INTEGER
); """
con = sqlite3.connect('../../mydata.sqlite')
con.execute(query)
con.commit()        

# %%
