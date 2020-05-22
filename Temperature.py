# -*- coding: utf-8 -*-
"""
Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the internet.
"""

temp=float(input("Enter the temperature(deg.celsius): "))
temp_kelvin=temp+273
temp_fahrenheit=(temp*1.8)+32

print("\nTemperature Readings:")
print("Temp(deg.celsius): %.2foC " %temp)
print("Temp(Kelvin):%.2fK" %temp_kelvin)
print("Temp(Fahrenheit): %.2fF" %temp_fahrenheit)
