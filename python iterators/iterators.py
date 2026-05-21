#python iterators:An iteartor is an object that contains a countable no.of values
#lists,tuples,dictionaries and sets are all iterable objects.they are iterable containers which you can get an iterator from
#it consists methods
#iter():converts an iterable into an iterator
#next():gets the next value from the iterator
#Return an iterator from a tuple, and print each value:
tuple=('hi','hlo','hmm')
x=iter(tuple)
print(next(x))#hi
print(next(x))#hlo
print(next(x))#hmm
#print(next(x))#stop iteration

#strings also iterable objects,and can return an iterator
#example
name="keerthi"
x=iter(name)
print(next(x))#k
print(next(x))#e
print(next(x))#e
print(next(x))#r
print(next(x))#t
print(next(x))#h
print(next(x))#i

#looping through an iterator
for i in tuple:
    print(i)
for ch in name:
    print(ch)

#create an iterator
#__iter__() method
#initializes the iterator
#returns the iterator object itself
class Demo:
    def __iter__(self):
        return self
#__next__() method
#returns the next value
#Raises stopiteration when no values are left
class Demo:
    def __next__(self):
        return 10

#example
class Numbers:
    def __iter__(self):
        self.num=1
        return self
    def __next__(self):
        if self.num<=10:
            x=self.num
            self.num+=1
            return x
        else:
            raise StopIteration

obj=Numbers()
for i in obj:
    print(i)
#StopIteration tells python to stop the loop








