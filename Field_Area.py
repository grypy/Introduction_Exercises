# -*- coding: utf-8 -*-
"""
Create a program that reads the length and width of a farmer's field from the 
user in ft. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre
"""

width=input("Enter width of the field(ft):")
length=input("Enter length of the field(ft):")
area = float(width)*float(length)
acres=(area/43560)
print("The field is %5.2f acres" %(acres))
