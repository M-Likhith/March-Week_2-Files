Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#fstring
a="rama"
b="sita"
print(f"hello {a}{b}")
hello ramasita
print(f"hello {a} {b}")
hello rama sita
print(f"hello {a} hello {b}")
hello rama hello sita

#list []
a=[3,5.6,"python",7+8j,True,False]
print(a)
[3, 5.6, 'python', (7+8j), True, False]
type(a)
<class 'list'>
b=9
type(b)
<class 'int'>
c=[10]
type(c)
<class 'list'>

#list methods
#append
a=["python","java","c","ds","ml"]
a.append("C")
print(a)
['python', 'java', 'c', 'ds', 'ml', 'C']
a.append(["c++","java"])
print(a)
['python', 'java', 'c', 'ds', 'ml', 'C', ['c++', 'java']]

#extend
a=["html","css"]
a.extend(["python","java"])
a
['html', 'css', 'python', 'java']

#insert()
a
['html', 'css', 'python', 'java']
a.insert(1,"ds")
a
['html', 'ds', 'css', 'python', 'java']
a.insert(4,"c")
a
['html', 'ds', 'css', 'python', 'c', 'java']

#index
a=["apple","banana","grapes"]
a.index("grapes")
2

#copy
b=a.copy()
b
['apple', 'banana', 'grapes']

#clear
a.clear()
a
[]
b=[]
#append
b.append("c")
b
['c']
b.extend(["A","B"])
b
['c', 'A', 'B']

#pop()
a=["hi","hello","how","are","you"]
a.pop()
'you'
print(a)
['hi', 'hello', 'how', 'are']
a.pop(3)
'are'
>>> a
['hi', 'hello', 'how']
>>> 
>>> #sort
>>> a=["python","java","c","ds","ml"]
>>> a.sort()
>>> a
['c', 'ds', 'java', 'ml', 'python']
>>> b=[9,3,0,2,11,4,5]
>>> b.sort()
>>> b
[0, 2, 3, 4, 5, 9, 11]
>>> 
>>> #reverse()
>>> a=["white","black","red"]
>>> a.reverse()
>>> a
['red', 'black', 'white']
>>> b=[2,3,4,5,6,7,8,9]
>>> b.reverse()
>>> b
[9, 8, 7, 6, 5, 4, 3, 2]
>>> 
>>> #remove()
>>> a=["html","css","js"]
>>> a.remove("js")
>>> a
['html', 'css']
>>> 
>>> #len()
>>> a=["mango","kiwi","dragon"]
>>> len(a)
3
>>> b="grapes"
>>> len(b)
6
>>> 
>>> #count
>>> c="mango"
>>> c.count("mango")
1
>>> d=["mango","dragon","dragon"]
>>> d.count("mango")
1
>>> d.count("dragon")
2
