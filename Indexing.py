Python 3.14.10 (tags/v3.14.10:b703b2c, Oct 25 2026, 17:36:52) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#INDEXING
a="My Name is Likhita"
a[0]+a[1]
'My'
a[3]+a[4]+a[5]+a[6]+a[7]
'Name '
a[3]+a[4]+a[5]+a[6]
'Name'
a[8]+a[9]
'is'
a[11]+a[12]+a[13]+a[14]+a[15]+a[16]+a[17]
'Likhita'

#Slicing
#[a:b]

a[0:]
'My Name is Likhita'
a[:]
'My Name is Likhita'
a[11:]
'Likhita'
a[11:18]
'Likhita'
a[11:16]
'Likhi'
a[3:7]
'Name'
a[0:10]
'My Name is'
#Negative Slicing
a[-7:]
'Likhita'
a[-10:-8]
'is'
a[-15:-11]
'Name'
a[:-1]
'My Name is Likhit'
a[-18:]
'My Name is Likhita'
a[-15:]
'Name is Likhita'


##Striding
#[a:b:i]

a="Hello,Everyone! What Doing?"
a[0:5]
'Hello'
a[6]
'E'
a[5]
','
a[6:14]
'Everyone'
a[14]
'!'
a[15:20]
' What'
a[16:20]
'What'
a[21:26]
'Doing'
a[26]
'?'
a[:15]
'Hello,Everyone!'
a[0:15:3]
'HlErn'
a[6:14:1]
'Everyone'
a[6:14:3]
'Ern'

# Negative Striding
a[-11:]
'What Doing?'
a[-11:-7]
'What'
a[-21:-10]
'Everyone! W'
a[-21:-9]
'Everyone! Wh'
a[-21:-12]
'Everyone!'
a[-21:-7:3]
'Ern a'
a[-21:-7:-3]
''
a[-21:-7:-2]
''
a[-7:-12:-3]
' h'
a[-21:-7]
'Everyone! What'
>>> a[-21:-7:1]
'Everyone! What'
>>> a[-21:-7:-2]
''
>>> a[-7:-21:-1]
' tahW !enoyrev'
>>> a[-7:-21:-3]
' h!oe'
>>> a[-6:-21:-3]
'Da nr'
>>> a[-6]
'D'
>>> a[-5:-21:-3]
'otWeyv'
>>> a[-8:-21:-3]
'tWeyv'
>>> a[::-1]
'?gnioD tahW !enoyrevE,olleH'
>>> string="HELLO ALL OF YOU"
>>> s[::-1]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s[::-1]
NameError: name 's' is not defined
>>> string[::-1]
'UOY FO LLA OLLEH'
>>> string[::]
'HELLO ALL OF YOU'
