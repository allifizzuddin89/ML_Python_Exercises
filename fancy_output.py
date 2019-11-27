#Manual string format
#using str.rjust() or str.ljust() or str.center()
for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ') #str.rjust() is for right justifies, give some space on the left
    print(repr(x*x*x).rjust(4))

#For numeric, we can use str.zfill(width)
# it can detect + - signs
 
print('12'.zfill(5))
print('-12'.zfill(9))
print('-3.142'.zfill(9))

##################################################################################################################

#old string format
import math
print("The value of pi is %5.3f."%math.pi) #look at placeholder, 5.3f, 5 means 5 char, .2 means 2 decimal places, f is float


##################################################################################################################
#open(), returns a file object
#usually open(filename, mode)
#mode could be 'r', 'w', 'r+'
#r means read only
#w means write, will overwrite existing file
#a means append, any new data will be added to the end
#r+ means read and write
#must specify encoding, else it will use platform encoding, platform = unix/mac/windows
#convert platform-specifi ending ;
#\n on Unix, \r\n on Windows
#use 'with' keyword when dealing with file object;
#so the file is properly closed

with open('workfile') as f:
    read_data = f.read()
f.closed #check either the file is closed or still open

#if not using 'with', please close the file using f.close()
#after the file is closed, any attempt to use the file will fail




