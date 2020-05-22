# -*- coding: utf-8 -*-
import math
"""
Create a program that reads two integers, a and b,
from the user. Your program should compute and display
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of ab
"""

a=int(input("Enter the first integer:"))
b=int(input("Enter the second integer:"))

sum=a+b
diff=a-b
product=a*b
quotient=a/b
remainder=a%b
log_val=math.log10(a)
res=a**b

#showing the results of the calculator
print("\n\n Arithmetic Calculator:")
print("Sum(a+b):",sum)
print("Difference(a-b):",diff)
print("Product(a*b):",product)
print("Division quotient:",quotient)
print("Division remainder:",remainder)
print("Logarithmic_value: %.2f" %(log_val))
print("Result(a^b):",res)
