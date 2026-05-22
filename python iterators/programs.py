#Create an iterator to print numbers from 1 to 10.
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

#Create an iterator to print even numbers from 2 to 20.
class Numbers:
    def __iter__(self):
        self.num=2
        return self
    def __next__(self):
        if self.num<=20:
            x=self.num
            self.num+=2
            return x
        else:
            raise StopIteration
obj=Numbers()
for i in obj:
    print(i)

#Create an iterator to print odd numbers from 1 to 15.
class Numbers:
    def __iter__(self):
        self.num=1
        return self
    def __next__(self):
        if self.num<=15:
            x=self.num
            self.num+=2
            return x
        else:
            raise StopIteration
obj=Numbers()
for i in obj:
    print(i)

#Create an iterator to print squares of numbers from 1 to 10.
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
    print(i*i)

#Create an iterator to print cubes of numbers from 1 to 5.
class Numbers:
    def __iter__(self):
        self.num=1
        return self
    def __next__(self):
        if self.num<=5:
            x=self.num
            self.num+=1
            return x
        else:
            raise StopIteration
obj=Numbers()
for i in obj:
    print(i**3)