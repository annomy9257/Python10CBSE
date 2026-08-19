"""
Write a python program to create a Dataframe from a list of lists and with specified column names.
"""

import pandas as pd

data = [
    ["Bob", 14],
    ["Danny", 15],
    ["xkd", 14]
]

df = pd.DataFrame(data, columns=["Name", "Age"])

print(df)

"""
OUTPUT:
    Name  Age
0    Bob   14
1  Danny   15
2    xkd   14
"""