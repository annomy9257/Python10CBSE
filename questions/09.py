"""
Write a python program to create a Series with custom indexes. 
"""

import pandas as pd

n = [10, 20, 30]

s = pd.Series(n, index=["A", "B", "C"])

print(s)

"""
OUTPUT:
A    10
B    20
C    30
dtype: int64
"""