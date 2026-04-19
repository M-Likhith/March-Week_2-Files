Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary (dict)
a={"name":"likhith","city":"vja"}
print(a)
{'name': 'likhith', 'city': 'vja'}
type(a)
<class 'dict'>
a["name"]
'likhith'
a.keys()
dict_keys(['name', 'city'])
a.values()
dict_values(['likhith', 'vja'])
a.items()
dict_items([('name', 'likhith'), ('city', 'vja')])

#update
a={"year":2026,"month":3}
a.update({"date":4})
a
{'year': 2026, 'month': 3, 'date': 4}

a.update({"date":14,"time":12:00})
SyntaxError: invalid syntax
a.update({"date":14,"time":12})
a
{'year': 2026, 'month': 3, 'date': 14, 'time': 12}

#set default
a={"colour":"white","vechile":"car"}
a.setdefault("year",2026)
2026

a
{'colour': 'white', 'vechile': 'car', 'year': 2026}
a.setdefault(2026,"year")
'year'
a
{'colour': 'white', 'vechile': 'car', 'year': 2026, 2026: 'year'}

#pop,popitem
a={"user":"likhith","mobile no":7897897891,"mail id":"abcd@gmail.com"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("mail id")
'abcd@gmail.com'
a
{'user': 'likhith', 'mobile no': 7897897891}

a.popitem()
('mobile no', 7897897891)
a
{'user': 'likhith'}

#copy,get,clear
>>> a={"time":1,"hour":2,"sec":5}
>>> a.copy()
{'time': 1, 'hour': 2, 'sec': 5}
>>> 
>>> a.get()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.get()
TypeError: get expected at least 1 argument, got 0
>>> a.get("time")
1
>>> a.get("hour")
2
>>> 
>>> a.clear()
>>> a
{}
>>> 
>>> #len,count
>>> a={"name":"likhith","city":"vja"}
>>> len(a)
2
>>> b={"name":"likhith","city":"vja","name":"M likhith"}
>>> print(b)
{'name': 'M likhith', 'city': 'vja'}
>>> a={"name":"likhith","city":"vja","name1":"likhith"}
>>> a
{'name': 'likhith', 'city': 'vja', 'name1': 'likhith'}
>>> 
>>> 
>>> a={"idnos":[10,20,30],"names":["likhith","mani","yaseer"]}
>>> print(a)
{'idnos': [10, 20, 30], 'names': ['likhith', 'mani', 'yaseer']}
>>> a.keys()
dict_keys(['idnos', 'names'])
>>> a.values()
dict_values([[10, 20, 30], ['likhith', 'mani', 'yaseer']])
