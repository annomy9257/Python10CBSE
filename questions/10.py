"""
Write a python program to create a Series from a dictionary. 
"""

import pandas as pd

data = {"D": 10, "E": 20, "F": 30}

series = pd.Series(data)

print(series)

"""
OUTPUT:
D    10
E    20
F    30
dtype: int64
"""