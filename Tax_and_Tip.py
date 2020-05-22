# -*- coding: utf-8 -*-

"""
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places
"""

meal_cost=input("Enter the cost of the meal:")
mc=float(meal_cost)
tax= 0.16*mc #local tax rate 16% (Kenya)
tip=0.18*mc  #18% the meal cost
grand_total=mc+tax+tip

print("\n\nSERENA HOTEL RECEIPT:")
print("Meal Cost:$%.2f" %(mc))
print("Tax amount:$%.2f" %(tax))
print("Tip amount:$%.2f" %(tip))
print("Grand_total:$%.2f" %(grand_total))