# -*- coding: utf-8 -*-
"""
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized.
"""
val=float(input("Enter your measurement(ft):"))
res_inches=val*12
res_yards=val*(1/3)
res_miles=val*(1/5280)

print("\n\nMEASUREMENTS OUTPUTS:")
print("Distance(feet): %.2f ft." %val)
print("Distance(Inches): %.2f Inches" %res_inches)
print("Distance(Yards): %.2f Yards" %res_yards)
print("Distance(Miles): %.2f Miles" %res_miles)