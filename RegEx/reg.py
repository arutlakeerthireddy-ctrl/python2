#$:End of string
#Check whether "Learn Python" ends with "Python".
import re
text="Learn Python"
result=re.search("Python$",text)
if result:
    print("Ends with Python")
else:
    print("not")

#*:zero or more occurrences
#Find matches of "ab*" in "a ab abb abbb"
#a=must be present
#b=zero or more b's
import re
s="a ab abb abbb"
result=re.findall("ab*",s)
print(result)#['a', 'ab', 'abb', 'abbb']


#+:one or more occurrences
print(re.findall(r"ab+",s))#['ab', 'abb', 'abbb']

#?:0 or 1 occurrences
#Match "colou?r" with "color" and "colour".
print(re.findall(r"colou?r","color"))#['color']
print(re.findall(r"colou?r","colour"))#['colour']

#Extract all phone numbers from "Call me at 9876543210 or 9123456789":
s="Call me at 9876543210 or 9123456789"
result=re.findall("\d+",s)
print(result)#['9876543210', '9123456789']

#Validate whether an email is in correct format "student123@gmail.com"
import re
e="student123@gmail.com"
pattern=r"\w+@\w+\.\w+"
print(re.search(pattern,e))#<re.Match object; span=(0, 20), match='student123@gmail.com'>

#Replace all digits in "Room 101 is on floor 2"
s="Room 101 is on floor 2"
print(re.sub("\d","#",s))#Room ### is on floor #