# -*- coding: utf-8 -*-
"""
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.
"""
R=0.04
n=1
deposit=float(input("Enter the amount deposited in the savings account:"))
for yr in range(0,4):
    CI=deposit*(1+(R/n))**(n*yr)
    print("Year %d Amount: $%.2f " %(yr,CI))
    
    