#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#matplotlib ex1

import matplotlib.pyplot as plt

#Basic of plotting, label, legend and title
x1 = [1,2,3]
y1 = [20,27,33]

plt.plot([1,2,3],[4,5,6], label='First Line')
plt.plot(x1,y1, label='Second Line')

plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Growth Graph\nSubtitle of Graph')
plt.legend()
plt.show()
 