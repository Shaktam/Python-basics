#1. int data type
#decimal form(base-10)
#binary form(base-2)(bin())
#octal form(base-8)(oct())
#hexadecimal form(base-16)(hex())
#2 float data type
# float represent only decimal
#3. complex datatype
#4.bool dtatatype
#5. string datatype
#slicing of string
# int()
# float()
# complex()
# bool()
# str()
#6. bytes datatpe
#bytes()
# bytes is immutable
# 7. bytearray datatype
# bytearray() 
#8. list datatype
#mutable
#list()
#l=[]
# 9. tuple datatype
# immutable
#tuple()
#t=()
#10. range datatype
#range()
#range(10)
#range(10,20)
#range(10,20,2)
#11. set Datatype
# represent group of alues without duplicate hwere the order is not important
#set{}
#no duplicate, no index, no insertion order, mutable
#12. frozenset
# immutable, no add , no remove
#13. Dict datatype
#represent group of value a key-value pair
# duplicate keys are not allowed but duplicate values are allowed
#14. None datatype
s="durga"
print(s)
print(s[1:40])
print(s[-1:])
print(s[-5])
print(bin(10))
print(hex(10))
#complex
a=1+1.5j
b=2+3.5j
c=a+b
print(c)
print(type(c))
list=[10,20,30,40,50]
list1=list.append('durga')   
print(list)
list2=list.remove(10)
print(list)
list3=list*2
print(list3)
x=5
y=5
z =x is not y
print(id(z))
print(id(y))
print(z)
d=[10,20,30,40]
e=bytearray(d)
e[0]=100
print(type(e))
for i in e:
    print(i)
f=(10,20,30,60)
print(type(f))
# tuple has immutable, no append,no remove, can't replace values
g = range(10,20,2)
for i in g:
    print(i)
#set    
h = {10,20,30,'set',100}
h1= h.add(50)
print(h)    
#frozenset
i={10,20,30,40}
j=frozenset(i)
print(type(j))
for J in j:
    print(J)

#dict data type
k={'a':'abc','b':'def','c':'ghi'}
print(k)    

#escape character
l = 'software\\developer'
l1='software\ndeveloper'
l8='software\'developer'
l2='software\tdeveloper'
l3='software\bdeveloper'
l4='software\"developer'
l5='software\fdeveloper'
l6='software\vdeveloper'
l7='software\rdeveloper'

print(l,l1,l8,l2,l3,l4,l5,l6,l7)

# constant
#constants are not applicable in python
#but in convention to uppercase without changing Value
# MAX_VALUE=100
#Arithmetic
#relational
#logical
#bitwise
#assignment
#special


#Arithmetic operator
# +,-,*,/,%,//,**
m1=10
m2=5
m3=m1+m2
m4=m1-m2
m5=m1*m2
m6=m1/m2
m7=m1%m2
m8=m1//m2
m9=m1**m2
print(m3,m4,m5,m6,m7,m8,m9)

#2. Relational operator

n1=10
n2=20
n3=n1>n2
n4=n1>=n2
n5=n1<n2
n6=n1<=n2
print(n3,n4,n5,n6)

#chaining operator
n7=(n1>n2>30)
n8=(n1<n2<30)
n9=(n1>=n2>=30>=40)
print(n7,n8,n9)

#equality operator

n10= (n1==n2)
n11= (n1!=n2)
print(n10,n11)

#4. Logical operator
#boolean= and,or,not non-boolean= 0=false and non-0(1,2,3,...)=true
o1= 10
o2=20
o3=1
o4= o1 and o2
o5= o3 and o2
print(o4, o5)
o6= o1 or o2
o7= o3 or o2
o8= not o2
o9= not o3
print(o6,o7,o8,o9)

#5.Bitwise Operator(&,|,^,~,<<,>>) only applicable for int and boolean types
p1=100
p2=101
p3=p1&p2
p4=p1|p2
p5=p1^p2
p6=~p2
p7=p1>>p2
p8=p1<<p2
print(p3,p4,p5,p6,p7,p8)

#7. Assignment operator
#(+=,-=,/=,*=,%=,//=,**=,&=,|=,^=,<<=,>>=)
q1=20
q2=10
q3=90
q4=20
q5=15
q6=30
q7=120
q8=150
q9=210
q10=220
q11=310
q12=205
q13=305
q14=120
q1+=15
q2-=10
q3/=5
q4*=25
q5%=5
q6//=25
q7**=15
q8&=10
q11|=12
q12^=30
q13<<=15
q14>>=25
print(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14)
#8.Teranary operator or conditional operator
a,b=10,20
x=30 if a>b else 40
print(x)

#x=int(input("enter the first number:"))
#y=int(input("enter the second number:"))
min= x if x<y else y
#print(min)
#Nesting for Program is possible
#program for min 3 num

#x=int(input("enter the first number:"))
#y=int(input("enter the second number:"))
#z=int(input("enter the third number:"))
min= x if x<y and x<y else y if y<z else z
print(min)
#Program for max 3num
max= x if x>y and x>y else y if y>z else z
print(max)

eq= x if x==y and x==y else y if y==z else z
print(eq)

#9.Special operator
#*Identity operator(is,is not)
#(address comparison)
r1=10
r2=10
r3=r1 is r2
r4=r1 is not r2
r5=r1==r2
print(id(r1))
print(id(r2))
print(r3,r4,r5)
list1=["one","two","three"]
list2=["one","two","three"]
print(list1 is list2)
print(list1 is not list2)
print(list1==list2)
#*Membership Operator(in, not in)
#(To check whether the given operator present in the given collection(It maybe string,set,tuple,dic or list))
s1="learning python is easy"
print('n' in s1)
print('ea' in s1)
print('learn' not in s1)

#*Operator Precedence
""" 
1.()-> parentesis
2.**-> exponential
3.~,- -> bitwise complement , unary minus operator
4.*,/.%,//->multiplication,division,modulo,floor division
5.+,- -> addition, subtraction
6.<<,>>-> left,right
7.&-> Bitwise AND
8.^-> Bitwise xor
9.|-> Bitwise or
10.>,>=,<,<=,==,!= -> relational operator
11.=,+=,*=,-=,/= -> assignment operator
12. is,is not -> Identity operator
13. in, not in-> Membership operator
14. not -> Logical NOT
15. and -> Logical AND
16. or ->Logical OR """

s2=10
s3=20
s4=25
s5=30
s6=(s2+s3)%(s4+s5)
s7=(s2+s3)*(s4/s5)
s8=(10+12/20**15)
s9=(3/2*4+3+(10/5)**3-2)
print(s6,s7,s8,s9)

#Mathematical Function
#Collection of function, variable and classes
import math# or from math import sqrt,pi,pow (using this we can directly use sqrt or any function instead of typing math every time)

t1=math.sqrt(16) #The math.sqrt() method square root of given integer,
t2= math.pi
t3=math.ceil(1.4)#The math.ceil() method rounds a number upwards to its nearest integer
t4= math.floor(1.4)# The math.floor() method rounds a number downwards to its nearest integer
t5=math.pow(2,5)
t6=math.log10(20)
t7=math.factorial(10)
t8=math.trunc(10)
t9=math.gcd(10,20)
t10=math.sin(10)
t11=math.cos(10)
t12=math.tan(10)
print(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12)

# for more Details refer this link(https://www.w3schools.com/python/module_math.asp)
#Important Variables of Math module
# pi->3.14
# e->2.71
# inf-infinity
# nan->not a number

#Reading dynamic input from keyboard(raw_input,input)
#1. raw_input()
#t13=raw_input("Enter Value:") raw_input only used in python2
#2.input()
t14=input("Enter Value:")
print(type(t14))
# Command Line Argument
#argv is not an arraz but a list