# -*- coding: utf-8 -*-
"""
)
The area of a triangle can be computed using the following formula, where b is the
length of the base of the triangle, and h is its height:
area =0.5*b*h
Write a program that allows the user to enter values for b and h. The program
should then compute and display the area of a triangle with base length b and height h
"""
b=float(input("Enter the base length of the triangle (m):"))
h=float(input("Enter the height of the triangle (m):"))
area=(0.5)*b*h
print("Area of the triangle: %.2f square meters." %area)

