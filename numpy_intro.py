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

# copy shape/dimension from other array
#full
#full_like
a1 = np.full_like(a,4)
print('\n',a1)
print('\n',a)

#similar with
a1 = np.full(a.shape,5)
print('\n',a1)

#generate random decimal number, 4 by 2 array
r1 = np.random.rand(4,2) #instead of giving input in tuples,"np.random.rand((4,2))", put directly
print('\n',r1)

#similar if use a.shape (ndarray.shape)
r2 = np.random.random_sample(a.shape)
print('\n',r2)

#random integer value
r3 = np.random.randint(22,size=(4,2)) #22 is limit value for random algo
print('\n',r3)

r3 = np.random.randint(-2,10, size=(3,5)) #10 is end value, start with 2
print('\n',r3)

#identity matrix
idmatrix = np.identity(3) # 3 by 3 identity matrix
print('\n',idmatrix)

#repeat an array
#axis is direction on numpy array, 0 right, 1 down
a2 = np.array([[1,2,3]]) # 2 dim array
r4 = np.repeat(a2,3, axis=0) #repeat 3 times
print('\n',r4)

#exrcise
ex = np.array([[1,1,1,1,1],[1,0,0,0,1],[1,0,9,0,1],[1,0,0,0,1],[1,1,1,1,1]])
print('\n',ex)

#similar
sol = np.full((5,5),1,dtype='int16')
print('\n',sol)

zer = np.zeros((3,3))
print('\n',zer)
zer[1,1] = 9
print('\n',zer)
sol[1:4,1:4] = zer
print('\n',sol)

#COPY issue!!!
#see below

a = np.array([1,2,3])
print('\n',a)
b = a
print('\n',b)
#lets change b
b[1] = 22
print('\n',b)
#lets print a
print('\n',a)

#we can see a also change
#we did not want this happens
#so, ndarray.copy()
a = np.array([1,2,3])
b = a.copy()
print('\n',a)

