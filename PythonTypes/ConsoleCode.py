Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = []
>>> a.append(1)
>>> a
[1]
>>> a.append(2)
>>> a
[1, 2]
>>> a.append("Hello")
>>> a
[1, 2, 'Hello']
>>> a = [1,2,3,10.5,"Hello",True]
>>> a[0]
1
>>> a[1]
2
>>> a[-1]
True
>>> a[-2]
'Hello'
>>> a[1:5]
[2, 3, 10.5, 'Hello']
>>> a[3][1:2]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a[3][1:2]
TypeError: 'float' object is not subscriptable
>>> a[4][1:2]
'e'
>>> a.append(12)
>>> a
[1, 2, 3, 10.5, 'Hello', True, 12]
>>> a.append(13,14)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.append(13,14)
TypeError: append() takes exactly one argument (2 given)
>>> a.append([13,14])
>>> a
[1, 2, 3, 10.5, 'Hello', True, 12, [13, 14]]
>>> a.extend([15,16,17])
>>> a
[1, 2, 3, 10.5, 'Hello', True, 12, [13, 14], 15, 16, 17]
>>> user = []
>>> user.extend(["Name"])
>>> user
['Name']
>>> user = {"Name" : ["Ram", "Shyam"]}
>>> user
{'Name': ['Ram', 'Shyam']}
>>> a
[1, 2, 3, 10.5, 'Hello', True, 12, [13, 14], 15, 16, 17]
>>> a.insert(0, "Bye")
>>> a
['Bye', 1, 2, 3, 10.5, 'Hello', True, 12, [13, 14], 15, 16, 17]
>>> a[0] = "Hi"
>>> a
['Hi', 1, 2, 3, 10.5, 'Hello', True, 12, [13, 14], 15, 16, 17]
>>> a.pop()
17
>>> a
['Hi', 1, 2, 3, 10.5, 'Hello', True, 12, [13, 14], 15, 16]
>>> a.pop()
16
>>> a
['Hi', 1, 2, 3, 10.5, 'Hello', True, 12, [13, 14], 15]
>>> a.pop(4)
10.5
>>> a
['Hi', 1, 2, 3, 'Hello', True, 12, [13, 14], 15]
>>> a.remove(11)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.remove(11)
ValueError: list.remove(x): x not in list
>>> a.remove(12)
>>> a
['Hi', 1, 2, 3, 'Hello', True, [13, 14], 15]
>>> len(a)
8
>>> a =[12,11,45,3,56,4,7,0,2,23]
>>> sorted(a)
[0, 2, 3, 4, 7, 11, 12, 23, 45, 56]
>>> sorted(a, reverse = True)
[56, 45, 23, 12, 11, 7, 4, 3, 2, 0]
>>> a
[12, 11, 45, 3, 56, 4, 7, 0, 2, 23]
>>> a.sort()
>>> a
[0, 2, 3, 4, 7, 11, 12, 23, 45, 56]
>>> 11 in a
True
>>> 'Hello' not in a
True
>>> 2 and 3 in a
True
>>> 2 or 3 in a
2
>>> b =(12,11,45,3,56,4,7,0,2,23)
>>> a
[0, 2, 3, 4, 7, 11, 12, 23, 45, 56]
>>> b
(12, 11, 45, 3, 56, 4, 7, 0, 2, 23)
>>> a[0] = 'Hi'
>>> a
['Hi', 2, 3, 4, 7, 11, 12, 23, 45, 56]
>>> b[0] = 'Hi'
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    b[0] = 'Hi'
TypeError: 'tuple' object does not support item assignment
>>> b
(12, 11, 45, 3, 56, 4, 7, 0, 2, 23)
>>> b[0]
12
>>> b[0:5]
(12, 11, 45, 3, 56)
>>> user = {"Name" : "Ram", "Age" : 20, "Num" : 89898979}
>>> user
{'Name': 'Ram', 'Age': 20, 'Num': 89898979}
>>> user[0]
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    user[0]
KeyError: 0
>>> user['Name']
'Ram'
>>> for data in user:
	print(data)

	
Name
Age
Num
>>> user.keys()
dict_keys(['Name', 'Age', 'Num'])
>>> user.values()
dict_values(['Ram', 20, 89898979])
>>> for data in user.values:
	print(data)

	
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    for data in user.values:
TypeError: 'builtin_function_or_method' object is not iterable
>>> for data in user.values():
	print(data)

	
Ram
20
89898979
>>> user.items()
dict_items([('Name', 'Ram'), ('Age', 20), ('Num', 89898979)])
>>> for data in user.items():
	print(data)

	
('Name', 'Ram')
('Age', 20)
('Num', 89898979)
>>> user
{'Name': 'Ram', 'Age': 20, 'Num': 89898979}
>>> user['Name'] = ['Ram']
>>> user
{'Name': ['Ram'], 'Age': 20, 'Num': 89898979}
>>> user['Name']
['Ram']
>>> name = user['Name']
>>> name
['Ram']
>>> name.append('Shyam')
>>> user
{'Name': ['Ram', 'Shyam'], 'Age': 20, 'Num': 89898979}
>>> set_1 = {1,2,3,4,5,6}
>>> type(set_1)
<class 'set'>
>>> set_2 = {4,5,6,7,8,9}
>>> set_1.intersection(set_2)
{4, 5, 6}
>>> a
['Hi', 2, 3, 4, 7, 11, 12, 23, 45, 56]
>>> set(a)
{'Hi', 2, 3, 4, 7, 11, 12, 45, 23, 56}
>>> a
['Hi', 2, 3, 4, 7, 11, 12, 23, 45, 56]
>>> set(b)
{0, 2, 3, 4, 7, 11, 12, 45, 23, 56}
>>> set_a = set(a)
>>> set_b = set(b)
>>> set_a.intersection(set_b)
{2, 3, 4, 7, 11, 12, 45, 23, 56}
>>> 
