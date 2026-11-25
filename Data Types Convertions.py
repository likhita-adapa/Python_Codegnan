Python 3.14.10 (tags/v3.14.10:b703b2c, Oct 25 2026, 17:36:52) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#DATA TYPES
a=1
type(a)
<class 'int'>
b=2.34
type(b)
<class 'float'>
c='Hello'
type(c)
<class 'str'>
c1="Double String"
type(c1)
<class 'str'>
c2='''Triple'''
type(c2)
<class 'str'>
c2="'mixed"'
SyntaxError: unterminated string literal (detected at line 1)

c3="'Mixed one'"
type(c3)
<class 'str'>
type(c2)
<class 'str'>
comp=4+5j
type(comp)
<class 'complex'>
comp11=j
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    comp11=j
NameError: name 'j' is not defined
complex=5j
>>> type(complex)
<class 'complex'>
>>> asd=j
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    asd=j
NameError: name 'j' is not defined
>>> x=3j=4j
SyntaxError: cannot assign to literal
>>> x=3j+4j
>>> type(x)
<class 'complex'>
>>> t=True
>>> type(t)
<class 'bool'>
>>> f=False
>>> type(f)
<class 'bool'>
>>> 
>>> 
>>> tr=true
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    tr=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> tru=True
>>> type(tru)
<class 'bool'>
