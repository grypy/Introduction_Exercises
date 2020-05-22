# -*- coding: utf-8 -*-

"""
Exercise 3: Area of a Room
Write a program that asks the user to enter the width and length of a room. 
Once the value has been read, your proram should compute and display the area 
of the room. 
The length and the width will be entered as floating point numbers. 
(include units in your prompt and output message in either ft or meters.) depending
on which unit you are more comfortable working with. 

"""
width=input("Enter width of the room(ft):")
length=input("Enter length of the room(ft):")
#Convert string to float

area=float(width)*float(length)
print("Area of the room: ",area," square ft.")

