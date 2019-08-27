Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[1,2,"hello",6,4,3,-10,3.4]
>>> a[0]
1
>>> a[-4]
4
>>> a[4:-4]
[]
>>> len(a)
8
>>> a.insert(3,"students")
>>> a
[1, 2, 'hello', 'students', 6, 4, 3, -10, 3.4]
>>> a.remove("hello")
>>> a
[1, 2, 'students', 6, 4, 3, -10, 3.4]
>>> a.pop()
3.4
>>> a.pop(4)
4
>>> a
[1, 2, 'students', 6, 3, -10]
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a=[4,55,2,33,7.6,-90]
>>> a.sort()
>>> a
[-90, 2, 4, 7.6, 33, 55]
>>> a.reverse()
>>> a
[55, 33, 7.6, 4, 2, -90]
>>> a.append(100)
>>> a
[55, 33, 7.6, 4, 2, -90, 100]
>>> s=a
>>> s
[55, 33, 7.6, 4, 2, -90, 100]
>>> s=a.copy()
>>> a
[55, 33, 7.6, 4, 2, -90, 100]
>>> a.append(100)
>>> a
[55, 33, 7.6, 4, 2, -90, 100, 100]
>>> a.count(100)
2
>>> 
