# -*- coding: utf-8 -*-
"""
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. All of the
values should be displayed using two decimal places, and the decimal points in all
of the numbers should be aligned when reasonable values are entered by the user
"""

SP = 3.49
discount = 0.6
loaves_dob = float(input("Enter the number of loaves of day old bread:"))
reg_price = SP*loaves_dob
total_price=SP*(1-discount)*loaves_dob
disc=SP*discount*loaves_dob
print("\n\nDay old bread Bakery Receipt")
print("Regular price: $%.2f" %reg_price)
print("Discount: $%.2f" %disc)
print("Total price: $%.2f" %total_price)