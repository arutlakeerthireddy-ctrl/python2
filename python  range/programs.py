#Print numbers from 0 to 9 using range().
x=range(0,10)
print(list(x))#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Print numbers from 1 to 20.
x=range(1,21)
print(list(x))#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#Print all even numbers from 2 to 20.
x=range(2,21,2)
print(list(x))#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#Print all odd numbers from 1 to 19.
x=range(1,20,2)
print(list(x))#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

#Print numbers from 10 to 1 in reverse order.
x=range(10,0,-1)
print(list(x))#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#Find the sum of numbers from 1 to 100 using range().
x=range(1,101)
print(sum(list(x)))#5050

#Print the multiplication table of 5 using range().
for i in range(1,10+1):
    print(5*i)

#Count how many numbers between 1 and 50 are divisible by 3.
count=0
for i in range(1,51):
    if i%3==0:
        count+=1
print(count)#16

#Print squares of numbers from 1 to 10.
for i in range(1,10+1):
    print(i*i)

#Create a list of numbers from 50 to 100 with a step size of 5.
x=range(50,101,5)
print(list(x))#[50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]