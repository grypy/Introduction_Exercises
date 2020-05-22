# -*- coding: utf-8 -*-
import math
"""
Write a program that begins by reading a radius, r, from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r. Use the pi constant in the math module in your
calculations.
"""
radius=float(input("Enter the radius of the object(m):"))
area_circle= math.pi*radius**2
volume_sphere=(4/3)*math.pi*radius**3

print("\n\nArea of a circle: %.2f square meters." %area_circle)
print("Volume of a sphere: %.2f cubic meters." %volume_sphere)