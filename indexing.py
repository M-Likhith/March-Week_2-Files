Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="i am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]+a[3]
'am'
>>> a[1]
' '
>>> a[0]
'i'
>>> a[1]+a[4]+a[7]
'   '
>>> 
>>> #2.
>>> b="simple is better than complex"
>>> b[10]+b[11]+b[12]+b[13]+b[14]+b[15]
'better'
>>> b[22]+b[23]+b[24]+b[25]+b[26]+b[27]+b[28]
'complex'
>>> b[0]+b[1]+b[2]+b[3]+b[4]+b[5]
'simple'
>>> 
>>> #negative indexing
>>> #1.
>>> c="i love python"
>>> c[-6]+c[-5]+c[-4]+c[-3]+c[-2]+a[-1]
'pythos'
>>> c[-11]+c[-10]+c[-9]+c[-8]
'love'
>>> 
>>> #2.
>>> d="vijayawada is royal city"
>>> d[-10]+d[-9]+d[-8]+d[-7]+d[-6]
'royal'
>>> d[-4]+d[-3]+d[-2]+d[-1]
'city'
>>> d[-13]+d[-12]
'is'
>>> 
>>> #3.
>>> e="vizag is a city a of destiny"
>>> e[-7:]
'destiny'
>>> e[-15]+e[-14]+e[-13]+e[-12]
'ty a'
