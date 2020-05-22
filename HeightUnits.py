# -*- coding: utf-8 -*-
"""
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.

Hint:One foot is 12 inches. One inch is 2.54 centimeters.
"""

height_ft=float(input("Enter height in ft:"))
height_in=float(input("Enter height in inches:"))

height_cm=((height_ft*12)+height_in)*2.54
print("Your height: %.2f cms." %(height_cm))



