Python 3.14.10 (tags/v3.14.10:b703b2c, Oct 25 2026, 17:36:52) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #DATA TYPE CONVERSIONS
>>> #### INT #####
>>> int(2)
2
>>> int(3.45)
3
>>> int(True)
1
>>> int(False)
0
>>> int("HI")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int("HI")
ValueError: invalid literal for int() with base 10: 'HI'
>>> int(3+4j)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    int(3+4j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> 
>>> 
>>> ### FLOAT #####
>>> float(2)
2.0
>>> float(3.445)
3.445
float("Hello")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float("Hello")
ValueError: could not convert string to float: 'Hello'
float(True)
1.0
float(False)
0.0
float(3+5j)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    float(3+5j)
TypeError: float() argument must be a string or a real number, not 'complex'



#### Boolean #####
bool(3)
True
bool(4.56)
True
bool(True)
True
bool(False)
False
bool("String")
True
bool(4j+6)
True


#### STRING ####
str(2)
'2'
str(4.56)
'4.56'
str("abcd")
'abcd'
str(True)
'True'
str(False)
'False'
str(4j+8)
'(8+4j)'


####Complex###
complex(4)
(4+0j)
complex(5.6)
(5.6+0j)
complex(True)
(1+0j)
complex(False)
0j
complex(3j+7)
(7+3j)
complex("xyz")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    complex("xyz")
ValueError: complex() arg is a malformed string
str("5")
'5'
bool(4)
True
bool(00)
False
bool(10)
True
bool(01)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
bool(False)
False
bool(1,1)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    bool(1,1)
TypeError: bool expected at most 1 argument, got 2
bool(1)
True
int(1;2)
SyntaxError: invalid syntax
complex(6,8)
(6+8j)
