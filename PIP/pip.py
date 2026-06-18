#what is PIP
'''PIP stands for pip install packages,pythons package manager
it is a tool used to install,update,remove python libraries(packages)'''
#basic PIP commands
#pip --version: 
'''checks if pip is installed'''
#pip install package_name:
'''install a package'''
#ex:pip install numpy
#pip install numpy==2.0.0:
'''install a specific version'''
#pip list:
'''view installed packages'''
#pip show package_name:displays version,location,author
'''get information about package'''
#ex:pip show numpy
#pip install --upgrade package_name:
'''update a package'''
#ex:pip install --upgrade numpy
#pip uninstall package_name
'''uninstall a package'''
#ex:pip uninstall numpy

#example:import and use "camelcase":
import camelcase
c=camelcase.CamelCase()
txt="hello kee"
print(c.hump(txt))#Hello Kee