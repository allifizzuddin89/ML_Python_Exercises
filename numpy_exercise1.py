#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#Exercise 1

import numpy as np 

array1 = np.arange(30).reshape(6,5)
print(array1)

list1 = [ x for x in range(1,31)]
print('\n',list1)

#creating 6 by 5 matrix using list1
array2 = np.array(list1).reshape(6,5)
print('\n',array2)
print('\n',type(array2))

matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
print('\n',matrix[0])
print('\n',len(matrix))

#slice row 2:4 and column 0:2
#to get 11,12,16,17
array3 = array2[2:4,0:2]
print('\n',array3)

#indexing diaogonal value
#2,8,14,20

array4 = array2[[0,1,2,3],[1,2,3,4]] #array2[[row],[column]]
print('\n',array4)

#indexing 4,5,24,29,30

array5 = array2[[0,4,5],3:]
print('\n',array5)