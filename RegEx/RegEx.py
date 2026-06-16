#Regular Expressions(Regex):
'''Regex is a sequence of characters used to search,match and manipulate text patterns
python provides 're' module to work with regex'''
import re
#regex functions
#re.search():checks if pattern exists anywhere in the string
import re
text="good morning daddy"
result=re.search("morning",text)
if result:
    print("Found")#found

#re.match():checks only at the beginning of the string
text="learning python"
result=re.match("learning",text)
print(result)
#if string starts with learning it return a match

#re.findall():returns all matches as a list
text="gee,kee,vee"
print(re.findall("ee",text))#['ee', 'ee', 'ee']

#re.sub():replaces matched text
text="i love maa"
result=re.sub("maa","dad",text)
print(result)#i love dad






