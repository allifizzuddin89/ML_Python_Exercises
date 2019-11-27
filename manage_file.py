#HOW TO CREATE, OPEN, READ, WRITE FILE
# 
# open(), returns a file object
#usually open(filename, mode)
#mode could be 'r', 'w', 'r+'
#r means read only
#w means write, will overwrite existing file
#a means append, any new data will be added to the end
#r+ means read and write
#w+ means create new file
#x means create new file, if file exist this operation will fail
#t means text mode
#b binary mode

#must specify encoding, else it will use platform encoding, platform = unix/mac/windows
#convert platform-specifi ending ;
#\n on Unix, \r\n on Windows
#use 'with' keyword when dealing with file object;
#so the file is properly closed

# with open('workfile','r' ) as f:
#     read_data = f.read()
# f.closed #check either the file is closed or still open

#if not using 'with', please close the file using f.close()
#after the file is closed, any attempt to use the file will fail

#create new file
f= open("allif_v1.txt","w+") #also can use with open("allif_v1.txt", "w+") so we could avoid using f.close()
for i in range(10):
    f.write("This is line {}\r\n".format(i+1))
f.close() 

#append data
f = open('allif_v1.txt', 'a+')
for i in range(2):
    f.write("Append line value is {}\r\n".format(i*i))
f.close()

#read only
f= open("allif_v1.txt", "r")
if f.mode == 'r':
    print("yes it is open now \n")
    contents = f.read()
    print(contents)

#read line by line
f.seek(0)
f1 = f.readlines()
for x in f1:
    print(x, end = " ")
f.close()

with open("allif_v1.txt","a+") as f:
    f.write("cuba lagi \r\n")

with open("allif_v1.txt","r+") as f:
    print(f.read())

#also can work multiple mode, e.g. "rwa"

#Binary operation
#file.seek()
#file.tell()
#file.seek(0) ==> reset the cursor, esp if in read file mode
