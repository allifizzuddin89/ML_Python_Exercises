#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89
#pie chart

import matplotlib.pyplot as plt 

Hari = [1,2,3,4,5,6,7]
Kerja = [8,8,8,8,8,4,4]
Main = [1,1,1,2,1,2,1]
Tidur = [6,6,6,5,6,8,11]

potongan = [11,2,3]
aktiviti = ['Kerja', 'Main', 'Tidur']
warna = ['c','b','m']
plt.pie(potongan, labels=aktiviti, colors=warna, startangle=90, shadow=True, explode=(0.2,0,0), autopct='%1.1f%%')
plt.title('Carta Pai Aktiviti\nAktiviti Harian 2020')
plt.show()