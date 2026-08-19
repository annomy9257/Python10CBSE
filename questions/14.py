"""
Write a python program to plot a bar graph of a student for the marks of 5 subjects. 
"""

import matplotlib.pyplot as plt

subjects = ["English", "Maths", "Science", "Hindi", "Computer"]
marks = [85, 90, 78, 88, 95]

plt.bar(subjects, marks)

plt.title("Marks of 5 Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()

"""
OUTPUT:
[GRAPHICAL USER INTERFACE OPENS]
"""