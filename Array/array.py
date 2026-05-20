#array:it stores multiple values in a single variable
#example:
Fruits=['mango','banana','apple']

#Access the elements of an array
x=Fruits[0]
print(x)#mango

#Modify the value of the first array item:
Fruits[0]='grapes'
print(Fruits)#['grapes', 'banana', 'apple']

#length of an array
print(len(Fruits))#3

#looping array elements
for i in Fruits:
    print(i)
'''grapes
banana
apple'''

#Adding array elements
Fruits.append('orange')
print(Fruits)#['grapes', 'banana', 'apple', 'orange']

#Removing array elemnts
Fruits.pop(1)
print(Fruits)#['grapes', 'apple', 'orange']
Fruits.remove('apple')
print(Fruits)#['grapes', 'orange']

#Python does not have built-in support for Arrays, but Python Lists can be used instead.
#clear():remove all elements from a list
Fruits.clear()
print(Fruits)#[]

#extend():add the elements of list to the end of current list
Fruits.extend([1,2,3,3,4])
print(Fruits)#[1, 2, 3, 4]

#copy():returns a copy of list
Fruits.copy()
print(Fruits)#[1, 2, 3, 4]

#count():returns the no. of elements with the specified value
print(Fruits.count(3))#2

#index():returns the index of first element with the specified value
print(Fruits.index(3))#2

#insert():adds an element at the specified position
Fruits.insert(2,9)
print(Fruits)#[1, 2, 9, 3, 3, 4]

#reverse():reverse the order of list
Fruits.reverse()
print(Fruits)#[4, 3, 3, 9, 2, 1]

#sort():sorts the list
Fruits.sort()
print(Fruits)#[1, 2, 3, 3, 4, 9]






