Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="codegnan"
len(a)
8
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1

#count
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("t")
5
a.count("k")
2
a.count("z")
0
a.count(" ")
3

#find a string
a="python"
a[1]
'y'
a.find("n")
5
a.find("t")
2
b="codegnan"
b.find("n")
5
#in find if there are 2 same letters it consider only first letter in the string

#escape sequences
#\n - new line
#\t - tab space
a="nmae\nmobileno\tmail id\ncity"
print(a)
nmae
mobileno	mail id
city
a="nmae:likhith\nmobileno:6302146671\tmail id: likhith.mentrumilli@gmail.com\ncity: vijayawada
SyntaxError: unterminated string literal (detected at line 1)
"nmae:likhith\nmobileno:6302146671\tmail id: likhith.mentrumilli@gmail.com\ncity: vijayawada"
'nmae:likhith\nmobileno:6302146671\tmail id: likhith.mentrumilli@gmail.com\ncity: vijayawada'
a="nmae:likhith\nmobileno:6302146671\tmail id: likhith.mentrumilli@gmail.com\ncity: vijayawada"
print(a)
nmae:likhith
mobileno:6302146671	mail id: likhith.mentrumilli@gmail.com
city: vijayawada

#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="wait wait until you succeed"
b.replace("wait","work")
'work work until you succeed'
b.replace("woit","work",1)     #here if there are two same words if we give word index value it only replace the 1st index word
'wait wait until you succeed'
b.replace("wait","work",1)
'work wait until you succeed'

#upper()
a="hello"
a.upper()
'HELLO'

#lower
b="HI"
b.lower()
'hi'

#capitalize - this is used to convert only first letter in the word
c="python"
c.capitalize()
'Python'

#title - this is used to capital all first letter of the different words given in single line
d="i am in class"
d.title()
'I Am In Class'

#conditions
a="likhith"
a.isupper()
False
a.islower()
True
a.startswith("l")
True
a.endswith("h")
True
a.isalpha()
True

b="python course"
b.isalpha()     #this condition gives true if there should be only all alphabets without spaces & special characters
False

c="pythoncourse"
c.isalpha()
True

d="12345"
d.isdigit()
True
d.isalnum()
True

e="likhith@123"
e.isalnum()
False
#in isalnum() there should not be any special characters and only numbers then only it gives true

#strip
#lstrip(),rstrip()
a="        likhith        "
a.strip()
'likhith'
a.lstrip()
'likhith        '
a.rstrip()
'        likhith'
>>> 
>>> #split()
>>> a="python java c c++"
>>> a.split()
['python', 'java', 'c', 'c++']
>>> b="i am learning python course"
>>> b.split()
['i', 'am', 'learning', 'python', 'course']
>>> 
>>> #join()
>>> a="python","java","c","c++"
>>> "".join(a)
'pythonjavacc++'
>>> " ".join(a)
'python java c c++'
>>> "or".join(a)
'pythonorjavaorcorc++'
>>> 
>>> #concatenation
>>> a"python"
SyntaxError: invalid syntax
>>> a="python"
>>> b="course"
>>> print(a+b)
pythoncourse
>>> print(a+" " +b)
python course
>>> 
>>> fname="likhith"
>>> lname="m"
>>> print(fname+" "+lname)
likhith m
>>> print(fname.title()+" "+lname.title())
Likhith M
>>> print((fname+"
...        
SyntaxError: unterminated string literal (detected at line 1)
>>> print((fname+" "+lname).title())
...        
Likhith M
>>> 
>>> #formatting
...        
>>> a=3
...        

