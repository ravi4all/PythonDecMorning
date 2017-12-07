Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 2
>>> a = "*"
>>> print(a*5)
*****
>>> for i in range(1,6):
	print('*' * ((i*2)-1)))
	
SyntaxError: invalid syntax
>>> for i in range(1,6):
	print('*' * ((i*2)-1))

	
*
***
*****
*******
*********
>>> for i in range(1,6):
	print('*' * i)

	
*
**
***
****
*****
>>> for i in range(1,6):
	print(' ' * (6-i) + '*' * (2*i + 1))

	
     ***
    *****
   *******
  *********
 ***********
>>> for i in range(1,6):
	print(' ' * (6-i) + '*' * (2*i - 1))

	
     *
    ***
   *****
  *******
 *********
>>> for i in reversed(range(1,6)):
	print(' ' * (6-i) + '*' * (2*i - 1))

	
 *********
  *******
   *****
    ***
     *
>>> 
