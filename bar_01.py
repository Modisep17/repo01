# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 14:47:08 2024

@author: Phenyo Modise
"""

#how to pt a barchat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
import plotly.express as px
df=pd.read_csv('desco.csv')
print(df.info())
df.drop(['Unnamed: 4'],inplace=True,axis=1)
print(df.info())
df.drop(['Unnamed: 6'],inplace=True,axis=1)
df.drop(['Unnamed: 5'],inplace=True,axis=1)
print(df.info())
print(df.describe())
print(df.info())
#Another attempt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
import plotly.express as px
X = ['BD1','BD1-BL','H-BD1'] 
IP = [3.23, 6.5, 4.5] 
Viscosity = [1.45,1.80,3.45]
n=3
r = np.arange(n) 
width = 0.25
plt.bar(r, IP, color = 'b',width = width, edgecolor = 'black',label='IP(h)'),plt.bar(r + width, Viscosity, color = 'g',width = width, edgecolor = 'black',label='Kinematic viscosity(mm2/s'), plt.xlabel("Fuel sample"),plt.ylabel("Value"), plt.title("Fuel properties of the samples"), plt.xticks(r + width/2,['BD1','BD1-BL','H-BD1']),plt.legend() 
plt.show()







  