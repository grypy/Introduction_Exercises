# -*- coding: utf-8 -*-
import math
"""
The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is:
distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))

Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers
"""

print("For point A:")
ta=float(input("Enter latitude:"))
ga=float(input("Enter longitude:"))
print("For point B:")
tb=float(input("Enter latitude:"))
gb=float(input("Enter latitude:"))

t1=math.radians(ta)
g1=math.radians(ga)
t2=math.radians(tb)
g2=math.radians(gb)

distance=6371.01*1/(math.cos(math.sin(t1)))*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2)

print("\n\nDistance between point A and B on the earth surface: %.2f kms." %(distance))