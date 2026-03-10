Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #striding
>>> a="data science"
>>> a[::]
'data science'
>>> a[::1]
'data science'
>>> a[::3]           #this command means it starts from 1st letter and adds 3 letters and print that index value
'dacn'
>>> 
\
>>> #2.
>>> b="machine learning"
>>> b[::4]
'miln'
>>> b[3:9]
'hine l'
>>> b[::6]
'men'
>>> b[::9]
'me'
>>> b[::7]
'm n'
>>> b[::2]
'mcielann'
>>> b[5:]
'ne learning'
>>> b[::4]
'miln'
>>> b[::8]
'ml'
>>> 
>>> #3.
>>> c="cloud computing"
>>> c[1:7:2]            #in this command the first 2 numbers index values will be considered that means it starts from 1st index and ends 7index and then last number will add 2 index valu
'lu '
>>> a[2:14:3]
'tsee'
>>> c[2:14:3]
'o mt'
>>> c[5:10:2]
' op'
>>> c[3:12:4]
'uot'
