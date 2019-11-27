#6 modules
#.py suffix
#a module is a file containing python definition and statement
#after quit the python interpreter/IDE definition (ftn and var) will be lost
#therefore we make script aka module, so we can call anytime

#import fibo.py module


import fibo

fibo.fib(1000)
print(fibo.fib2(100))
print(fibo.__name__) 

#can assign to a local name for convenience

fib = fibo.fib
fib(200)

#module can contain executable statement and also function statement
#each module has its own private symbol table, no worries clashes on user's global var
#can import a module's var via notation "modname.itemname"
#modules also can import other modules
#imported module's name are placed in the importing module's global's symbol table
#use "import" to do so

from fibo import fib, fib2
fib(700)

#how to import all names in a module
#import all names except with underscore '_'
#however use import * is not recommended as best method

from fibo import *
fib(350)

#if the module name is followed by 'as'
#name following 'as' is bound directly to the imported module
#same way as import fibo will do, the diff is as fibtest

import fibo as fibtest
fibtest.fib(1000) # compare to (e.g) fibtest = fibo.fib, refer line 18

#also as effective as using 'from'

from fibo import fib2 as fibonacci
fibonacci(1800)

##################################################################################
print('\n','-'*100)

##6.1 Executing modules as scripts
#use python fibo.py <arguements>
#__main__ vs __name__
#__name__ is the name of the imported module
#__main__ is the current script or current module
#look at first_module.py and second_module.py for better understanding

####################################################################################

###6.1.2 The module search path
#when a module is imported, the interpreter will search for built ibn module
#if there is none, it will search for the module in the list of variable in the sys.path


####6.1.3 "compiled" python files
#to speed up loading, python cached the compiled version in the __pychache__ dir under the name module.version.pyc
#  read more!

###################################################################################

####6.2 Standard module
#Python Library Reference
#environment variable PYTHONPATH
#can modify using standard operation such as append() ; sys.path.append('dir')

###################################################################################

####6.3 The dir() function
#the built in dir() function is used to defined which names a module defines


import fibo, sys 
print(dir(fibo))
print('\n', dir(sys))

#without arguement, dir() list the names we have defined currently
print('\n', dir())

#dir( does not list the names of built in functions and variables
#if we want that, we could use standard modules 'builtins'

import builtins
print('\n', dir(builtins))

#########################################################################################

###6.4 Packages
#a directory of packages (folder) contains a collection of modules which contains __init__.py file
#each folder must have __init__.py file, can be no content file
#package is very important when developing a huge application
#essential to organize and avoid collision on global variables name and module name
#https://realpython.com/python-modules-packages/#python-packages
#https://www.youtube.com/watch?v=urE5MuYd-YM&t=348s
#https://hackernoon.com/pip-install-abra-cadabra-or-python-packages-for-beginners-33a989834975

##6.4.1

# __init__.py: must exist in every folder of the packages
#__init__.py can be empty or consist of explicit index
#__all__ = [ "module1","module2","module3", "etc"] ; example of explicit index
#explicit index is important to ensure all sub-packages is imported
#from module1.submodule1 * ; means import all, so author must include explicit index for 
# user's convenience but not a recommended practice
#if there is no explicit index, from moudule1.submodule1 * does not import all sub-packages
#it will only look for the previously imported sub-packages or module if any
#so best use from package import specific_submodule

##6.4.2

#intra_package referece
#a packgae or module import another package or module
#let's say under package sound > effects > echo.py , surround.py, reverse.py
#sound > filters > equalizer.py, vocoder.py, karaoke.py
#sound > formats >wavread.py, wavwrite.py, aiffread.py, aiffread.py, auread.py, auwrite.py
#use absolute import

#let's say we are in the surround.py
#RELATIVE import ;
#from . import echo ; means import echo, from the same current folder
#from .. import formats ; means import from previous folder
#from .. filters import equalizer ; means import from previous folder, only import equalizer
#These imports use leading dots to indicate the current and parent packages involved in the relative import
#refer https://realpython.com/absolute-vs-relative-python-imports/

#A single dot means that the module or package referenced is in the same directory as the current location
#Two dots mean that it is in the parent directory of the current location—that is, the directory above. 
#Three dots mean that it is in the grandparent directory
#can use relative import
#relative import specifies the resource to be imported relative to the current location

#absolute import specifies the resource to be imported using its full path from the project’s root folder.

#if packages is in different directory, covered that in workspace "allif_packages"