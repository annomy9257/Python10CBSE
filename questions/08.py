"""
Write a python program to create a Series from a list.
"""

import pandas as pd
l = [1, 2, 3, ]
s = pd.Series(l)
print(s)

"""
OUTPUT:
0    1
1    2
2    3
dtype: int64
"""