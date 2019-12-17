#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89

import pandas as pd 
import numpy as np
df = pd.read_excel("survey.xls")
print(df)

#cross tabulation
#on pandas
#lets find the frequency of handedness vs nationality

cross_t1 = pd.crosstab(df.Nationality,df.Handedness) #pd.crosstab('1stcolumn','2ndcolumn')
print('\n',cross_t1)

#sex vs handedness

cross_t2 = pd.crosstab(df.Sex,df.Handedness)
print('\n',cross_t2)

#lets add total

cross_t2 = pd.crosstab(df.Sex,df.Handedness,margins=True) #total, set margins to true
print('\n',cross_t2)

#lets have multiple var/occurrences
#parsing as array []
#lets check handedness according to sex and nationality

cross_t2 = pd.crosstab(df.Sex,[df.Handedness,df.Nationality],margins=True)
print('\n',cross_t2)

#let's rearrange

cross_t2 = pd.crosstab(df.Handedness,[df.Sex,df.Nationality],margins=True)
print('\n',cross_t2)

cross_t2 = pd.crosstab([df.Handedness],[df.Sex,df.Nationality],margins=True)
print('\n',cross_t2)

#Normalize
#percentage of the occurences
#based on doc:
#normalize = all or True, norm over all values
#normalize = index, norm over each row
#normalize = columns, norm over each column
#if include margins=True, norm margin values

cross_t2 = pd.crosstab(df.Sex,df.Handedness,normalize='index') #by row
print('\n',cross_t2)

cross_t2 = pd.crosstab(df.Sex,df.Handedness,normalize='columns') #by column
print('\n',cross_t2)

cross_t2 = pd.crosstab(df.Sex,df.Handedness,normalize='all') #by all
print('\n',cross_t2)


#average of male is left handed

cross_t2 = pd.crosstab(df.Sex,df.Handedness,values=df.Age, aggfunc=np.average) 
print('\n',cross_t2) #age of female lhanded is 44.5

