# -*- coding: utf-8 -*-

"""
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula
"""
val=input("Enter a positive integer: ")
n=int(val)
if(n%2 !=0):
    print("Not a positive integer!")
else:
    sum=(n*(n+1))/2
    print("The sum is ",sum)