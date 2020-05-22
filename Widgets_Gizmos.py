# -*- coding: utf-8 -*-
"""
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order
"""

WIDGET_WEIGHT = 75
GIZMO_WEIGHT = 112

widget=int(input("Enter the number of widgets:"))
gizmo=int(input("Enter the number of gizmos:"))

#to compute the total weight of the order
grand_total = (WIDGET_WEIGHT*widget)+(GIZMO_WEIGHT*gizmo)
print("\nTotal weight of order:", grand_total, "grams")

