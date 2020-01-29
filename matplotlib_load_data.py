#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89

import matplotlib.pyplot as plt 
import csv

#import using numpy
#also import using std library

#using std library

x = []
y = []

with open('numpy_data.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

print(x,' ',y,'\n')
plt.plot(x,y,label='Load Data from Text')
plt.xlabel('Range')
plt.ylabel('Data')
plt.legend()
plt.title('Using Std Library')
plt.show()
plt.close()
#using numpy

import numpy as np 

data = np.genfromtxt('numpy_data.txt', delimiter=',')
print(data)

data = data.astype('int32')
x = data[0:3,0]
print('\n',x)

y = data[0:3,1]
print('\n',y)

plt.plot(x,y)
plt.title('Using Numpy Library')
plt.xlabel('X data')
plt.ylabel('Y data')
plt.show()
plt.close()