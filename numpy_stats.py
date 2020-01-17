#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#Numpy statistics exercise

import numpy as np 

stats = np.array([[1,33,1],[4,20,6]])

#minimum
min_stats = np.min(stats)
max_stats = np.max(stats)
print('\n',min_stats)
print('\n',max_stats)

#by row or column
min_stats = np.min(stats, axis=0) #0 to the right, 1 to downward
print('\n',min_stats)
stats_sum = np.sum(stats)
print('\n',stats_sum) #sum all element

