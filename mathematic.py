#1

import math

degree = int(input())
radians = degree *(math.pi/180)
print(radians)

#2

height = int(input())
base1 = int(input())
base2 = int(input())
area = 0.5*(base1+base2)*height
print("Height:", height)
print("Base, first value:", base1)
print("Base, second value:", base2)
print("Expected Output:", area)

#3

sides = int(input())
length_of_side = int(input())
area_of_polygon = (sides * (length_of_side)**2) / (4 * math.tan(math.pi / sides))
print("Input number of sides:", sides)
print("Input the length of a side:", length_of_side)
print(f"The area of the polygon is: {area_of_polygon:.0f}")

#4
base_of_parallelogram = int(input())
height_of_parallelogram = int(input())
area_of_parallelogram = base_of_parallelogram * height_of_parallelogram
print("Length of base:", base_of_parallelogram)
print("Height of parallelogram:", height_of_parallelogram)
print("Expected Output:", area_of_parallelogram)