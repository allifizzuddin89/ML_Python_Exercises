#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#Numpy reorganizing arrays exercise

import numpy as np 

#reshape dimension
before = np.array([[1,2,3,4],[5,6,7,8]])
print('\n',before)

after = before.reshape((4,2)) #reshape into 4 by 2 array
print('\n',after)

#Vertical stack

m1 = np.array([1,2,3])
m2 = np.array([4,5,6])
stack1 = np.vstack([m1,m2,m1]) #3 matrix stacked
print('\n',stack1)

#Horizontal stack
stack2 = np.hstack([m1,m2])
print('\n',stack2)
