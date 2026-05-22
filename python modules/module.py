#python modules
#what is module?
'''module is a file that contains python code such as variables,functions,classes etc.
it is used to organize code and reusable'''
#create a module
'''To create a module just save the file with file extension .py'''
#created module with file name mymodule.py
#use a module
'''Now we can use the module by using import statement'''
#syntax:
'''module_name.function_name'''
#example:now import the created module named my.module.py and call greeting function
import mymodule
mymodule.greeting(' keerthi')#hlo keerthi
#variables in module:module contains variables of all types(list,tuple,dictionary)
#example:now import module named mymodule and access dict
import mymodule
x=mymodule.dict['Name']
print(x)#keerthi
#Naming a module:you can name module file whatever you like but it must have file extension .py
#Re-naming a module:
'''you can create alias when you import module by using as keyword'''
#example
import mymodule as my
x=my.dict['roll']
print(x)#14
#Buit-in modules
#example:Import and use the platform module:
import platform
x=platform.system()
print(x)#windows
#using dir() function:it will list all the function names/variable names in a module
#example:List all the defined names belonging to the platform module:
import platform
x=dir(platform)
print(x)

import mymodule
x=dir(mymodule)
print(x)

#import from module:using from keyword we can choose to import only parts from a module
from mymodule import dict
print(dict["Branch"])#csm






