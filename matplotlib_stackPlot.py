#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#stack plot

import matplotlib.pyplot as plt

hari = [1,2,3,4,5,6,7]
makan = [1,1,2,2,3,1,1]
tidur = [7,6,6,8,8,8,11]
main = [2,2,2,3,1,2,1]

plt.stackplot(hari, makan, tidur, main, colors=['c','b','m'])
plt.plot([],[],label='Makan', linewidth=5, color='c')
plt.plot([],[],label='Tidur', linewidth=5, color='b')
plt.plot([],[], label='Main', linewidth=5,color='m')

plt.ylabel('Aktiviti')
plt.xlabel('Jumlah Hari')
plt.title('Activity Plot\nMasa Terluang')
plt.legend()
plt.show()