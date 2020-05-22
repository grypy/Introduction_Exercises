# -*- coding: utf-8 -*-
import math
"""
area of the triangle based on the length of the sides
s=(s1+s2+s3)/2
"""
s1=float(input("Enter the length of the first side(S1):"))
s2=float(input("Enter the length of the second side(S2):"))
s3=float(input("Enter the length of the third side(S3):"))

s=(s1+s2+s3)/2
val = s*(s-s1)*(s-s2)*(s-s3)
area=math.sqrt(val)
print("Area of a triangle %.2f square meters." %area)
