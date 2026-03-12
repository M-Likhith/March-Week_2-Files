Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple
>>> a=(2,4.5,"c",7+9,True,False)
>>> type(a)
<class 'tuple'>
>>> len(a)
6
>>> a.index(True)
4
>>> a.count(4.5)
1
>>> a.count(7+9j)
0
