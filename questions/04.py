"""
Write a program to generate a series of marks of 6 students.
Give moderation up to 5 marks of those who are having
marks < 90 and print the new list of the marks. 
"""

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

"""
OUTPUT:
>>> Enter a number: 5
    Odd

>>> Enter a number: 4
    Even
"""