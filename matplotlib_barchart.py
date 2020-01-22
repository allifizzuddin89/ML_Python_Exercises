#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#matplotlib barchart

import matplotlib.pyplot as plt 

#barchart
x = [1,2,3,4]
y = [11,33,2,100]
x1 = [5,6,7,8]
y1 = [22,11,5,76]

#lets put some color
plt.bar(x,y,label='Bar 1',color='magenta') #can also use hex code, c=cyan instead of type fully cyan
plt.bar(x1,y1,label='Bar 2')
plt.xlabel('Type')
plt.ylabel('Height')
plt.title('Growth Chart\nMaryam Comey')
plt.legend()
plt.show()