#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#Numpy exercise 1

import numpy as np 

#initialize array

a = np.array([1,2,3])
print(a)

b = np.array([[5.6,3.3,7.8],[2.0,5.3,4.3]])
print('\n',b)

#get dimension info
print('\n',a.ndim)
print('\n',b.ndim)

#get shape info
print('\n',a.shape) #row x column, 3 column
print('\n',b.shape) #row x column, 2 x 3

#get type info
print('\n',a.dtype)
print('\n',b.dtype)

#set type
b1 = np.array([[5.6,3.3,7.8],[2.0,5.3,4.3]], dtype='int16')
print('\n',b1)
print('\n',b1.dtype)

#Get size info
print('\n',a.itemsize) #8byte
print('\n',b.itemsize) #8byte
print('\n',b1.itemsize) #2byte
print('\n',b1.size) #number of elements in the array

#get total size
print('\n',a.size*a.itemsize)
#also similar
print('\n',a.nbytes)

#slicing

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print('\n',a)

#get a specifi element [r,c]
print(a[1,6]) #get an element at row 1 column 6
#also similar
print('\n',a[1,-1]) #use negative

#get a specific row
print('\n',a[0,:]) #first row and everything on column

#get a specific column
print('\n',a[:,0]) #everything on first column

#[startindex:endindex:stepsize]
print('\n',a[0,1:6:2]) #first row, start with 1, end with 6, increment 2

#change element
a[1,2] =55 #2nd row, 3rd column
print('\n',a)

a[:,2] = [1,2]
print('\n',a)

#3D array
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]], dtype='float32')
print('\n',b)

#get specific element (work outside in)
#first row, second row, second column ~3d array

print('\n',b[0,1,1])

#test
print('\n',b[:,1,1])

#replace
b[:,1,:] = [[45,3.2],[33,7.3]]
print('\n',b)

#Initialize different types of array
#all 0s matrix

print('\n',np.zeros(2))
print('\n',np.zeros((2,3)))
print('\n',np.zeros((2,3,4,5)))

#any other number
c = np.full((2,2),78, dtype='float32')  #np.full((dimension),element)
print('\n',c)
print(c.dtype)

#25:29
