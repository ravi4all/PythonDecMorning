Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = "Hello world"
>>> a[0]
'H'
>>> a[1]
'e'
>>> a[2]
'l'
>>> a[3]
'l'
>>> a[0,3]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a[0,3]
TypeError: string indices must be integers
>>> a[0:4]
'Hell'
>>> a[-1]
'd'
>>> a[-2]
'l'
>>> a[0:-1]
'Hello worl'
>>> a[:]
'Hello world'
>>> a[0:]
'Hello world'
>>> a[:100]
'Hello world'
>>> a = "Hello"
>>> print(a*5)
HelloHelloHelloHelloHello
>>> a = "Hello\n"
>>> print(a)
Hello

>>> a
'Hello\n'
>>> print(a*5)
Hello
Hello
Hello
Hello
Hello

>>> a.upper()
'HELLO\n'
>>> print(a.upper())
HELLO

>>> b = "world"
>>> a+b
'Hello\nworld'
>>> 
