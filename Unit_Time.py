# -*- coding: utf-8 -*-
"""
Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration.
"""
print("Program that determines duration as seconds")
days=int(input("Enter the number of days:"))
hours=int(input("Enter the number of hours:"))
minutes=int(input("Enter the number of minutes:"))
seconds=int(input("Enter the number of seconds:"))

duration=(days*24*3600)+(hours*3600)+(minutes*60)+seconds
print("Duration: %.2f seconds." %duration)


