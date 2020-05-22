# -*- coding: utf-8 -*-
import math 
"""
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:
q = mCΔT.
Write a program that reads the mass of some water and the temperature change
from the user. Your program should display the total amount of energy that must be
added or removed to achieve the desired temperature change

Hint: The specific heat capacity of water is 4.186 J
g◦C. Because water has a density of 1.0 gram per millilitre, 
you can use grams and millilitres interchangeably
in this exercise.
Extend your program so that it also computes the cost of heating the water. 
Electricity is normally billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
your program to compute the cost of boiling water for a cup of coffee.
Hint: You will need to look up the factor for converting between Joules and
kilowatt hours to complete the last part of this exercise
"""
C=4.186
KWH_conv = 3600000

mass=float(input("Enter the mass of water(g):"))
T=float(input("Enter the temperature change(deg.celsius):"))

q=(mass*C*T)
q1=q/1000      #Kilo-Joules
print("\nThe total amount of energy:% .2f KJs." %q1)
print("\nThe cost of boiling water for a cup of coffee")
energy_used=(q/KWH_conv)
cost=(energy_used*8.9) #cost given in dollars
print("Energy consumed: %.2f Kwh" %energy_used)
print("Cost: %.2f cents" %cost)
