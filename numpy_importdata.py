#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#Numpy import data exercise

import numpy as np 

data = np.genfromtxt('numpy_data.txt', delimiter=',')
print('\n',data)
print('\n',data.dtype)

#we notice the data type is float
#change into integer

data = data.astype('int32')
print('\n',data)
print('\n',data.dtype)

#Boolean Masking and Advanced Indexing

#advance slicing, find element greater than 40
#masking and condition
print('\n',data>40)
print('\n',data[data>40])

print('\n',np.any(data>40, axis=0)) #downward matrix
print('\n',np.any(data>40, axis=1)) #rightward compare matrix
print('\n',"higher than 40 and less than 60",'\n',((data>40)&(data<60)))
print('\n',"the elements are: ",'\n',data[(data>40)&(data<60)])


#index with a list in numpy
#rearrange index
print('\n',data[[2,1,0]])
#compare with original data
print('\n',data)

