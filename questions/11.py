"""
Write a python program to create a Dataframe. 
"""

import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Riya"],
    "Age": [14, 15, 14]
}

df = pd.DataFrame(data)

print(df)

"""
OUTPUT:
    Name  Age
0   Aman   14
1  Rahul   15
2   Riya   14
"""