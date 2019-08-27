Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=(1,2,"hello",6,4,3,-10,3.4)
>>> a[0]
1
>>> a[0:6]
(1, 2, 'hello', 6, 4, 3)
>>> a[-1]
3.4
>>> a[-2]
-10
>>> a[4:-2]
(4, 3)
>>> len(a)
8
>>> a.insert(3,"students")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.insert(3,"students")
AttributeError: 'tuple' object has no attribute 'insert'
>>> a. insert(3,"students")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a. insert(3,"students")
AttributeError: 'tuple' object has no attribute 'insert'
>>> a.remove("hello")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.remove("hello")
AttributeError: 'tuple' object has no attribute 'remove'
>>> a.remove["hello"]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.remove["hello"]
AttributeError: 'tuple' object has no attribute 'remove'
>>> a*2
(1, 2, 'hello', 6, 4, 3, -10, 3.4, 1, 2, 'hello', 6, 4, 3, -10, 3.4)
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> 
