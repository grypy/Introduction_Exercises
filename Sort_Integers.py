# -*- coding: utf-8 -*-
import math
"""
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.
"""
s1=int(input("Enter the first integer:"))
s2=int(input("Enter the second integer:"))
s3=int(input("Enter the third integer:"))

min_val=min(s1,s2,s3)
max_val=max(s1,s2,s3)
mid_val=(s1+s2+s3)-(min_val+max_val)

print("\nSORT 3 INTEGERS")
print("Smallest integer: %d" %min_val)
print("Largest integer: %d" %max_val)
print("Middle value: %d" %mid_val)