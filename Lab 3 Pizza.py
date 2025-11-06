#This Program will give the price of pizza per square inch

size = eval(input("Enter the size of the pizza"))
price = eval(input("Enter the price of the pizza"))
import math
area = math.pi * ((size/2)**2)
finalprice = price / area
print("The price per square inch of the pizza is $" , round(finalprice,2))
