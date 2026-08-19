"""
Write a python program to Load an image and give Title of the image. 
"""

import matplotlib.pyplot as plt

image = plt.imread("questions/image.png")

plt.imshow(image)
plt.title("My Image")

plt.show()

"""
OUTPUT:
[GRAPHICAL USER INTERFACE OPENS]
"""