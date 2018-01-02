Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def temp_conv(c):
	return 9/5 * c + 32

>>> temp_conv(33.5)
92.30000000000001
>>> cel = [32.4,33.5,35.8,38.4,32.7]
>>> for temp in cel:
	temp_conv(temp)

	
90.32
92.30000000000001
96.44
101.12
90.86000000000001
>>> map
<class 'map'>
>>> map(temp_conv, cel)
<map object at 0x0000029609D38DD8>
>>> list(map(temp_conv, cel))
[90.32, 92.30000000000001, 96.44, 101.12, 90.86000000000001]
>>> lambda x,y : x+y
<function <lambda> at 0x0000029609263E18>
>>> a = lambda x,y : x+y
>>> a
<function <lambda> at 0x0000029609D42730>
>>> type(a)
<class 'function'>
>>> a()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a()
TypeError: <lambda>() missing 2 required positional arguments: 'x' and 'y'
>>> a(2,5)
7
>>> a(b,c)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a(b,c)
NameError: name 'b' is not defined
>>> a('b','c')
'bc'
>>> list(map(lambda temp, 9/5*temp+32 cel))
SyntaxError: invalid syntax
>>> list(map(lambda temp: 9/5*temp+32 cel))
SyntaxError: invalid syntax
>>> list(map(lambda temp: 9/5*temp+32, cel))
[90.32, 92.30000000000001, 96.44, 101.12, 90.86000000000001]
>>> f = list(map(lambda temp: 9/5*temp+32, cel))
>>> f
[90.32, 92.30000000000001, 96.44, 101.12, 90.86000000000001]
>>> t = 32.5
>>> f = list(map(lambda temp: 9/5*temp+32, t))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    f = list(map(lambda temp: 9/5*temp+32, t))
TypeError: 'float' object is not iterable
>>> t = 32.5,
>>> f = list(map(lambda temp: 9/5*temp+32, t))
>>> f
[90.5]
>>> def even(num):
	return num % 2 == 0

>>> even(12)
True
>>> a = []
>>> for i in range(1,51):
	a.append(i)

	
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
>>> a = []
>>> a = [i for i in range(1,51)]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
>>> import time
>>> for n in a:
	even(n)

	
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
>>> list(filter(even, a))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> even = [i for i in range(51) if i % 2 == 0]
>>> even
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> def add():
	a = 10
	b = 12
	return a + b

>>> add()
22
>>> def add():
	a = 10
	b = 12
	yield a + b

	
>>> add()
<generator object add at 0x0000029609D62048>
>>> a = add()
>>> a
<generator object add at 0x0000029609D620A0>
>>> 
