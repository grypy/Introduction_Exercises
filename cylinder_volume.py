# -*- coding: utf-8 -*-
import math
"""
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place
"""
val_r=float(input("Enter radius of the cylinder(m):"));
val_h=float(input("Enter the height of the cylinder(m):"))

vol=math.pi*(val_r**2)*val_h

print("\nVolume of a cylinder: %.2f square meters." %vol)