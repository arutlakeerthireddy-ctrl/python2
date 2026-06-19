#python Exception handling(try,except):
#Exception handling is way to handle runtime errors whithout stopping the program
#without exception handling
x=8
y=0
#print(x/y)#ZeroDivisionError: division by zero
print("program ends")
#program crashes and "program ends" is never executed

#with exception handling
try:
    x=8
    y=0
    print(x/y)
except ZeroDivisionError:
    print("cannot divide by zero")
print("program ends")
#cannot divide by zero
#program ends

#what is exception:An exception is an error that occurs during program execution
#ValueError
#TypeError
#IndexError
#KeyError
#ZeroDivisionError
#FileNotFoundError
'''#examples:
int('ab') #valueError
10/0  #ZeroDivisionError
mylist[10] #IndexError
mydict['name']#KeyError
"10"+10 #TypeError
print(x) #NameError
open("abc.txt") #FileNotFoundError'''

#try block:the code that might cause an error is placed inside try
'''try:
    num=int(input())
    print(10/num)'''
#python checks this code,if error occurs execution jumps to except

#except block:used to handle errors
try:
    print(10/0)
except:
    print("Error occurred")#Error occurred

#Avoid plain except:specific exceptions make debugging easier
try:
    print(int("a"))
except ValueError:
    print("error occured")#error occurred

#multiple except blocks
try:
    n=int(input())#hlo
    print(10/n)
except ValueError:
    print("Invalid number")#Invalid number
except ZeroDivisionError:
    print("cannot divide by zero")


#multiple exceptions in one except
try:
    n=int(input())#0
    print(4/n)
except(ValueError,ZeroDivisionError):
    print("Invalid")#Invalid

#capturing Error message (as)
try:
    print(int("a"))
except ValueError as e:
    print(e)#invalid literal for int() with base 10: 'a'

#else block:runs only if no exception occurs
try:
    print(int("9"))
except ValueError:
    print("Error occurred")
else:
    print("no error")#no error

#finally block:always executes
try:
    print(10/0)
except ZeroDivisionError:
    print("Error")
else:
    print("no error")
finally:
    print("always runs")
#Error
#always runs

#complete structure
'''try:
    statement
except:
    statement
else:
    statement
finally:
    statement'''

#nested try-except
try:
    try:
        print(10/0)
    except ZeroDivisionError:
        print("Inner execution")
except:
    print("outer execution")
#Inner execution

#Raising Exceptions(raise):we can create own exceptions
age=-8
if age<0:
    raise ValueError("age cannot be negative")
#ValueError: age cannot be negative



