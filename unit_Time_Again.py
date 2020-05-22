# -*- coding: utf-8 -*-

"""
Develop a program that begins by reading a number of seconds from the user.
Then your program should display the equivalent amount of time in the form
D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds 
respectively. The hours, minutes and seconds should all be formatted so that
they occupy exactly two digits, with a leading 0 displayed if necessary
"""

seconds_per_day = 86400
seconds_per_hour = 3600
seconds_per_minute = 60
val=int(input("Enter the number of seconds:"))
days=val/(seconds_per_day)
val=val%seconds_per_day

hrs=val/seconds_per_hour
val=val%seconds_per_hour

mins=val/seconds_per_minute
val=val%seconds_per_minute

print("Duration %d:%02d:%02d:%02d." %(days,hrs,mins,val))


