Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets{}
a={2,5.7,"likhith",6+7j,True,False}
print(a)
{False, True, 2, 5.7, (6+7j), 'likhith'}
b={5,7,8,9,4,5,6}
print(b)
{4, 5, 6, 7, 8, 9}
type(a)
<class 'set'>

#set methods
a={1,2,3,4,5,6}
b={4,5,6}
a.add(20)
a
{1, 2, 3, 4, 5, 6, 20}
a.issubset(b)
False
b.issubset(a)
True

#superset
a={1,2,3,4,5,6}
b={4,5,6}
a.issuperset(b)
True
b.issuperset(a)
False

#union()
a={1,2,3,4,5,6}
b={4,5,6,7,8,9}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}

#intersection
a={1,2,3,4,5,6,7/}
SyntaxError: invalid syntax
a={1,2,3,4,5,6,7}
b={5,6,7,8,9,10}
a.intersection(b)
{5, 6, 7}

#difference
a={1,2,3,4,5,6,7}
b={6,7,8,9,10,11,12}
a.difference(b)
{1, 2, 3, 4, 5}
b.difference(a)
{8, 9, 10, 11, 12}

#update
a={6,7,8,9,10}
b={1,2,3,4,5,6,7}
a
{6, 7, 8, 9, 10}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#intersection_update
a={4,5,6,7,8,9}
b={1,2,3,4,5,6}
a

a.intersection_update(b)
a
{4, 5, 6}
b.intersection_update(a)
b
{4, 5, 6}

#difference_update
a={2,3,4,5,6,7}
b={1,2,3,4,5,6,7,8,9}
a.difference_update(b)
a
set()
b.difference_update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}

a={3,4,5,6,7,8,9,10}
b={1,2,3,4,5,6,11,12}
a
a.difference_update(b)
a
{7, 8, 9, 10}
b.difference_update(a)
b
{1, 2, 3, 4, 5, 6, 11, 12}

#symmetric_difference
a={3,4,5,6,7,8}
b={1,2,3,4,5,6,7}
a.symmetric_difference(b)
{1, 2, 8}
b.symmetric_difference(a)
{1, 2, 8}

#symmetric_difference_update
a={10,20,30,40,50,60}
b=30,40,50,60,70,80,90}
SyntaxError: unmatched '}'
b={30,40,50,60,70,80,90}
a.symmetric_difference_update(b)
a
{70, 10, 80, 20, 90}
b.symmetric_difference_update(a)
b
{40, 10, 50, 20, 60, 30}

#pop & remove in sets
a={1,2,3,4,5,6,7}
>>> b={3,4,5,6,7,8,9}
>>> a.pop()
1
>>> a.remove(5,6)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a.remove(5,6)
TypeError: set.remove() takes exactly one argument (2 given)
>>> a.remove(5)
>>> a
{2, 3, 4, 6, 7}
>>> 
>>> #clear,copy,add
>>> a={1,2,3,4,5}
>>> a.copy()
{1, 2, 3, 4, 5}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(30)
>>> b
{30}
>>> 
>>> #discard
a
>>> ={1,2,3,4,5,6}
SyntaxError: invalid syntax
>>> a={1,2,3,4,5,6}
>>> a.discard(5)
>>> a
{1, 2, 3, 4, 6}
>>> len(a)
5
>>> 
>>> #is disjoint
>>> a={4,5}
>>> b={5,6}
>>> a.isdisjoint(b)
False
>>> a{7,8,9]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> a={7,8,9}
>>> b={1,2,3}
>>> a.isdisjoint(b)
True
