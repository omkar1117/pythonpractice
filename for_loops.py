Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:/Users/chand/Desktop/py practice/file_read.py ===========
Enter the filename to read:C:/Users/chand/Desktop/py practice/details.txt
Traceback (most recent call last):
  File "C:/Users/chand/Desktop/py practice/file_read.py", line 16, in <module>
    L.append(details)
NameError: name 'L' is not defined
>>> 
=========== RESTART: C:/Users/chand/Desktop/py practice/file_read.py ===========
Enter the filename to read:C:/Users/chand/Desktop/py practice/details.txt
List Here [{'first_name': 'Python'}, {'last_name': 'Perl'}, {'email': 'ruby@anrc.in'}, {'first_name': 'Testing'}, {'last_name': 'Team'}, {'email': 'test@control.in'}]
>>> a=''
>>> if a:
	print("Variable exists with data")

	
>>> a=None
>>> if a:
	print("Variable exists with data")

	
>>> a="test
SyntaxError: EOL while scanning string literal
>>> a="test"
>>> if a:
	print("Variable exists with data")

	
Variable exists with data
>>> x=[1,2,3,4,5]
>>> for row in x:
	print(row)

	
1
2
3
4
5
>>> a
'test'
>>> for d in a:
	print(d)

	
t
e
s
t
>>> for row in x.reverse():
	print("Data here::", row)

	
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    for row in x.reverse():
TypeError: 'NoneType' object is not iterable
>>> x
[5, 4, 3, 2, 1]
>>> for row in x:
	print("Data here::", row)

	
Data here:: 5
Data here:: 4
Data here:: 3
Data here:: 2
Data here:: 1
>>> for i,row in enumerate(x):
	print("Data here::",i,row)

	
Data here:: 0 5
Data here:: 1 4
Data here:: 2 3
Data here:: 3 2
Data here:: 4 1
>>> 
>>> 
>>> for i,row in enumerate(x):
print("Hello world")
SyntaxError: expected an indented block
>>> 
>>> for i, row in enumerate(x):
	if i == 2:
		print("Matched Value:", row)

		
Matched Value: 3
>>> 