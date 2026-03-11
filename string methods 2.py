Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #formatting
>>> a=3
>>> b=6
>>> print(a+b)
9
>>> print("the sum is:",a+b)
the sum is: 9
>>> 
>>> city="vja"
>>> print("the city is:",city)
the city is: vja
>>> name="likhith"
>>> print("name is:",name)
name is: likhith
>>> 
>>> #format method
>>> a="motu"
>>> b="patlu"
>>> print("hello {}{}".format(a,b))
hello motupatlu
>>> print("hello {} {}".format(a,b))
hello motu patlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello patlu
>>> 
>>> #fstring
>>> a="rama"
>>> b="sita"
>>> print(f"hello {a}{b}")
hello ramasita
>>> print(f"hello {a} {b}")
hello rama sita
>>> print(f"hello {a} hello {b}")
hello rama hello sita
