import numpy as np
import pandas as pd
from pandas import DataFrame


#1.To find the mean using numpy
num = [56,65,78,76,56,79]
print(np.mean(num))

#2.To print 1 Dimentional array
ar = np.array([1,2,3,4,],float)
print(ar)

#3.To print 2 Dimentional array
twoD_array= np.array([[1,2,3],[4,5,6]],float)
print(twoD_array)

#4.Creating a DataFrame:
df = DataFrame({'name':['Braund','Cummings','Heikkinen','Allen'],
                'index':['a','b','c','c'],'age':[22,38,26,35],
                'fare':[7.25,71.83,8.05,86],'survived':[False,True,True,False]})
#setting index as the Index column:
df.set_index('index',inplace=True)

#5.To print objects in column wise fasion with default index.
series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
print(series)

#6.Conditional approch on series example:
cuteness = pd.Series([1, 2, 3, 4, 5], index=['Cockroach', 'Fish', 'Mini Pig',
                                                 'Puppy', 'Kitten'])
print(cuteness>3) #lists as per the condition.

#7.Data set meathod 2
data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data)
print(football)

#8.To call individual columns from df data set
print(df[['name','age']])
print(df[df['age']>=30]) #to extract elements as per condition
df['survived'][df['age']>=30] #,, ,, ,, ,, ,, ,, ,, ,, ,, ,, ,,

#9.Using the apply function on Dataframes
df2 = DataFrame({'one':[1,2,3],'index':['a','b','c'],'two':[1,2,3]})
df2.set_index('index',inplace=True)
print(df2)

#Finding the mean.
print(df2.apply(np.mean))

'''In the below code every single value in the 'one'
column is evaluated and as per the condition
a boolean operation is returned'''
print(df2['one'].map(lambda x: x>=1))

print(df2.applymap(lambda x:x>= 1)) #to all columns

#10.Dot product of two lists:
a = [1,2,3,4,5]
b = [2,3,4,5,6]
print(np.dot(a,b))
