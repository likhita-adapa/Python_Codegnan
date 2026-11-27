Python 3.14.10 (tags/v3.14.10:b703b2c, Oct 25 2026, 17:36:52) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Operatorss
#1.Arthematic Operators
a=4
b=6
print(a+b)
10
print(a-b)
-2
print(a*b)
24
print(a/b)
0.6666666666666666
print(a//b)
0
print(a**b)
4096
print(a%b)
4

#2.Assignment Operators
a=3
b=4
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
7
a-=b
a
3
a*=b
a
12
a/=b
a
3.0
a//=b
a
0.0
a%=b
a
0.0
a**=b
a
0.0

#Comprasion Operators
a=6
b=4
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True

#Logical Operators
x=4
y=9
#For and
x<y and x<=y
True
y<x and y>=x
False
x>y and x>=y
False
y>=x and y!=x
True

#For Or
x<y and x<=y
True
y<x or y>=x
True
x<y or x<=y
True
x>y or x>=y
False

#For Not
not(x<y and x<=y)
False
not(x>y or x>=y)
True


# Identify Operators
a=10
b=69
a is b
False
a is not b
True
a=4
b=4
>>> a is b
True
>>> 
>>> # Membership Operators
>>> num=22,33,44,55,66,77,88,99,100
>>> 22 in num
True
>>> 44 not in num
False
>>> 100 in num
True
>>> 
>>> # Bitwise Operators
>>> a=6
>>> b=7
>>> a&b
6
>>> a | b
7
>>> a^b
1
>>> ~a
-7
>>> s=5
>>> s<<2
20
>>> s>>3
0
