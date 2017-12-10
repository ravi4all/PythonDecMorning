Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def func_1():
	print("Hello")

	
>>> func_1()
Hello
>>> 
>>> def func_1(x,y):
	print(x+y)

	
>>> func_1(1,2)
3
>>> def func_1(x,y):
	return x+y

>>> func_1(2,3)
5
>>> def func_1(x,y):
	return x+y, x-y, x/y, x*y

>>> func_1(2,3)
(5, -1, 0.6666666666666666, 6)
>>> a = func_1(2,3)
>>> a
(5, -1, 0.6666666666666666, 6)
>>> a[0]
5
>>> a,b,c,d = func_1(2,3)
>>> a
5
>>> b
-1
>>> c
0.6666666666666666
>>> d
6
>>> a,b = func_1(2,3)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a,b = func_1(2,3)
ValueError: too many values to unpack (expected 2)
>>> a,*b = func_1(2,3)
>>> a
5
>>> b
[-1, 0.6666666666666666, 6]
>>> 
