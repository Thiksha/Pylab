it2016b204@cmruuser:~$ python3 lab111.py
python3: can't open file 'lab111.py': [Errno 2] No such file or directory
it2016b204@cmruuser:~$ cd Documents
it2016b204@cmruuser:~/Documents$ python3 lab111.py
PRATHIKSHA RAVOOR
it2016b204@cmruuser:~/Documents$ python3
Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a=5
>>> b=6
>>> print(a+b)
11
>>> c=a+b
>>> c
11
>>> d=input
>>> d=input("enter a value")
enter a value45
>>> e=(input("enter a value")
... 37
  File "<stdin>", line 2
    37
     ^
SyntaxError: invalid syntax
>>> e=input("enter a value")
enter a value37
>>> g=d+e
>>> print("g")
g
>>> print(g)
4537
>>> int(g=d+e)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'g' is an invalid keyword argument for int()
>>> d=int(input("enter a value"))
enter a value45
>>> e=int(input("enter a value"))
enter a value37
>>> g=d+e
>>> print(g)
82
>>> 

