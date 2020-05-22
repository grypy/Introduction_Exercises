# -*- coding: utf-8 -*-
import math

"""
Write a program that begins by reading the air temperature and wind speed from the
user. Once these values have been read your program should display the wind chill
index rounded to the closest integer.
"""
#V   #Kilometers per hour
#Ta  #air temperature

air_temp=float(input("Enter the air temperature(deg.celsius): "))
wind_speed = float(input("Enter the wind speed(km/h): "))

if(air_temp<=10):
    if(wind_speed>4.8):
        WCI =13.12+(0.6215*(air_temp))-(11.37*wind_speed**0.16)+((0.3965*air_temp)*(wind_speed**0.16))
        wind_chill_index=round(WCI)
        print("Wind chill index: %d" %wind_chill_index)
    else:
        print("Enter wind speed > 4.8kph")
else:
    print("Enter Air temperature < 10 deg.celsius")