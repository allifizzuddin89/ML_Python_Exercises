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
