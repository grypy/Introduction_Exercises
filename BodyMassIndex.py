# -*- coding: utf-8 -*-
"""
Write a program that computes the body mass index (BMI) of an individual. Your
program should begin by reading a height and weight from the user. Then it should
use one of the following two formulas to compute the BMI before displaying it. If
you read the height in inches and the weight in pounds then body mass index is
computed using the following formula:
    American units BMI=(weight/(height^2))*703
    British units BMI=(weight/(height^2))
"""
print("Body Mass Index of an individual")
metric_system=int(input("Choose type of metric system:\n1.American system \n2.British system\n"))
if(metric_system == 1):
    height = float(input("Enter height(Inches):"))
    weight = float(input("Enter weight(pounds)"))
    BMI = ((weight)/(height**2))*703
    print("BMI: %.2f " %BMI)
    
elif(metric_system == 2):
    height = float(input("Enter height(meters):"))
    weight = float(input("Enter weight(kgs)"))
    BMI = ((weight)/(height**2))
    print("BMI: %.2f " %BMI)
    
else:
    print("Invalid option")
    

