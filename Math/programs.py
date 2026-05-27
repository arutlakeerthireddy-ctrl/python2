#Addition & Subtraction
#What is 245 + 378?
import math
x=math.fsum([245,378])
print(x)#623.0

#Subtract 589 from 1000.
x=math.fsum([1000,-589])
print(x)#411.0

#Find the sum of 456, 789, and 234.
print(math.fsum([456,789,234]))#1479

#What is 950 − 475?
print(math.fsum([950,-475]))#475

#math.fabs:returns positive value of a number
print(math.fabs(-7))#7.0

#Write a program to find the factorial of 6.
print(math.factorial(6))#720

#Write a program to find the GCD of 24 and 36.
print(math.gcd(24,36))#12

#Find sin(1) using the math module.
print(math.sin(1))#0.84147098

#Write a program to find the cosine value of 0.
print(math.cos(0))#1.0

#Write a program to find the natural logarithm of 10.
print(math.log(10))#2.302585092994046

#math.trunc()
#Write a program to remove the decimal part from 9.8 using math.trunc().
print(math.trunc(9.8))#9

#Find the truncated value of 15.99.
print(math.trunc(15.99))#15

'''python math module doesnot support fractions but uses fractions module'''
import math
from fractions import Fraction
x=Fraction(2,5)+Fraction(9,3)
print(x)#17/5

