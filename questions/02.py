"""
Write a python program to print the area and perimeter of Rectangle. 
"""

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area =", area)
print("Perimeter =", perimeter)

"""
OUTPUT:
Enter length: 10
Enter breadth: 20
Area = 200
Perimeter = 60
"""