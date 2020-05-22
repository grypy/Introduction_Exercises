# -*- coding: utf-8 -*-
"""
Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0m/s. Assume that the acceleration
due to gravity is 9.8m/s2. You can use the formula vf = vi2 + 2ad to compute the
final speed, vf , when the initial speed, vi, acceleration, a, and distance, d, are known.
"""

g=9.8   #msec**-2
height = float(input("Enter the height from which the object is dropped(m):"))
vi=0
vf=(vi**2)+(2*g*height)
print("The final speed: %.2f m/s." %vf)

