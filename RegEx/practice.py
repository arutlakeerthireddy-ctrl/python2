#regex patterns in python
#\d:matches a digit(0-9)
#Extract all digits from "My age is 20 and roll number is 105".
import re
text="My age is 20 and roll number is 105"
result=re.findall("\d",text)#['2', '0', '1', '0', '5']
print(result)  

#\d+:one or more digits
#Find all numbers in "Price: 250, Discount: 50".
import re
text="Price: 250, Discount: 50"
result=re.findall("\d+",text)
print(result)#['250', '50']

#\w:letter,digit,_
#Count the number of word characters in "Python_3".
import re
text="Python_3"
result=re.findall("\w",text)
print(result)#['P', 'y', 't', 'h', 'o', 'n', '_', '3']

#\w+:one or more word characters
#Extract all words from "Python is easy!".
text="python is easy!"
result=re.findall("\w+",text)
print(result)#['python', 'is', 'easy']

#\s:whitespace
#Find all spaces in "Hello World Python".
import re
text="Hello World Python"
result=re.findall("\s",text)
print(result)#[' ', ' ']

#\S:non whitespace character
result=re.findall("\S",text)
print(result)
#['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd', 'P', 'y', 't', 'h', 'o', 'n']

#. :any character except newline
#Find patterns matching "c.t" in "cat cot cut"
text="cat cot cut"
result=re.findall("c.t",text)
print(result)#['cat', 'cot', 'cut']

#^:start of string
#Check whether "Python is fun" starts with "Python".
s="Python is fun"
result=re.match("^Python",s)
if result:
    print("starts with python")
else:
    print("doesnot starts with python")

    