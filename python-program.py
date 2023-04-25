#Q.Write a Python Program to find Area of circle
from math import pi
r=16
A=pi*r**2
print(A)
#Q2:write a program to read two numbers from keyboard and print sum
import operator
# a=input("Enter first value:")
# b=input("Enter Second Value:")
#c=operator.__add__(int(a),int(b))
#print(c)
#Q3. write a program to read employee data from keyboard and print data
# Eno=int(input("Enter the Employee Number:"))
# Ename=input("Enter the Employee Name:")
# Esalary=float(input("Enter the Employee Salary:"))
# Eaddress=input("Enter the Employee address:")
# Emaritalstatus=bool(input("Employee Married?[True|False]:"))
# print("Please Confirm Information")
# print("Employee No:",Eno)
# print("Employee Name:", Ename)
# print("Employee Salary:", Esalary)
# print("Employee Address:", Eaddress)
# print("Employee Married:", Emaritalstatus)

#Q4. write a program to read multiple values from keyboard in a single line

# a,b= [int(x) for x in input("Enter two numbers:").split()]
# print("Output is:",a*b)

#Q5. write a program to read 3 float number from keyboard with , seperator and print their sum

# a,b,c=[float(y) for y in input("Enter three numbers:").split(',')]
# print("sum is:", a+b+c)

#eval()
z=eval("10*20+30")
print(z)

#y=eval(input("Enter the values:"))
#Enter the values 10*30/4
#print(y)

#Q6. Write a program to accept list from the keyboard on the display

#l=eval(input("Enter List:"))
#print(type(l))
#print(l)

m=('paddy', 'Rice', 'Corn')
print(list(enumerate(m)))
print(set(enumerate(m)))
print(dict(enumerate(m)))
print(tuple(enumerate(m)))
