#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#Numpy math exercise

import numpy as np 

a = np.array([1,2,3,4])
print('\n',a+2)
print('\n',a/4)
a+=6
print('\n',a)
print('\n',np.cos(a))

print('*'*100)
#Linear algebra

print('\n',"MATH with Numpy")
a = np.ones((2,3))
print('\n',a)
b = np.full((3,2),7)
print('\n',b)

#use matrix multiply ftn
c = np.matmul(a,b)
print('\n',c)
print('\n',c.dtype)

#Determinant of matrix
c = np.identity(3)
print('\n',c)
det = np.linalg.det(c)
print('\n',det)

#inverse
#singular vector decomposition
#eigenvalues
#matrix norm
#Refer