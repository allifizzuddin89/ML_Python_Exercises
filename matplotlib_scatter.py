#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#scatter plot

import matplotlib.pyplot as plt 
import random

x= [random.randrange(1,100,2) for x in range(30)]
y= [x for x in range(len(x))]
plt.scatter(x,y, label='Scatter Plot',color='green', marker='X',s=20) #change marker and its size
plt.xlabel('Random X')
plt.ylabel('Random Y')
plt.title('Scatter Plot\nTest 1')
plt.legend()
plt.show()