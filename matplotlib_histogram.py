#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#matplotlib histogram

import matplotlib.pyplot as plt 
import numpy as np
import random

#Bar Chart
age = [random.randrange(1,100,1) for i in range(25)]
print(age)
print('\n',type(age))
print('\n',len(age))
id = [x for x in range(len(age))]
print('\n',id)

plt.bar(id,age, label='People')
plt.xlabel('Id')
plt.ylabel('Age')
plt.title('Bar chart of Population\nPuncak Alam')
plt.legend()
plt.show()

#Histogram
#use bin
#1 bin could contain any value
#histogram can be used to analyze value
#in this case bin is used to contain age range
#we could see how many people is age 0-10, 11-20...91-100
#bar chart could not provide this kind of stats

age1 = [random.randrange(1,100,1) for i in range(25)]
bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(age1,bins,histtype='bar',rwidth=0.8, label='People Distribution')
plt.xlabel('Age')
plt.ylabel('People')
plt.title('Distribution of Population\nPuncak Alam')
plt.legend()
plt.show()