# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print ("hello Phenyo")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
df= pd.read_csv('rancimat.csv')
print(df.info())
print(df.describe())
data1=(df['IP'])
data2=(df['BD1'])
data3=(df['H-BD1'])
data4=(df['BD1-BL'])
data5=(df['LP5'])
plt.scatter(data1, data2),plt.xlabel("Induction period"),plt.ylabel("Conductivity"),
plt.scatter(data1, data3),plt.xlabel("Induction period"),plt.ylabel("Conductivity"),plt.title("Hydrogenated Jatrophabiodiesel")
plt.scatter(data1, data4),plt.xlabel("Induction period"),plt.ylabel("Conductivity"),plt.title("Jatropha biodiesel blended with 20% LP5")
plt.scatter(data1, data5),plt.xlabel("Induction period"),plt.ylabel("Conductivity"),plt.title("LP5 diesel")
plt.scatter(data1, data4),plt.xlabel("Induction period"),plt.ylabel("Conductivity"),
plt.scatter(data1, data2),plt.xlabel("Induction period"),plt.ylabel("Conductivity"),
plt.scatter(data1, data2),plt.xlabel("Induction period"),plt.ylabel("Conductivity"),plt.title("Jatropha biodiesel")
#Attempt to fit curves
df = pd.DataFrame(list(zip( BD1 , H-BD1 , BD1-BL , LP5)), index = IP ,columns = [ 'BD1' , 'H-BD1' , 'BD1-BL' , 'LP5' ])
df.plot(),
df.plot() , plt.xlabel("Induction period (h)"),plt.ylabel("Conductivity(µs/cm)")
#Codes to plot a combined visualisation
import plotly.express as px
df = px.data.gapminder().query("rancimat.csv")
fig = px.line(df, x='year', y='lifeExp', color='country', markers=True)
fig.show()
#second attemp to code
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
import plotly.express as px
df = px.data.gapminder()
gapminder_data = pd.read_csv('rancimat.csv', index_col='IP')
gapminder_data.head()
fig.show()
#third attempt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
import plotly.express as px
df= pd.read_csv('rancimat.csv')
print(df.info())
print(df.describe())
plot_df = df.pivot(index=["IP"],columns=("LP5"))
plot_df.plot()
plt.tight_layout()
plt.show()
#attempt at bar charts and analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
import plotly.express as px
d1f=pd.read_csv('desco.csv')
print(df1.info())
df1.drop(['Unnamed: 4'],inplace=True,axis=1)
print(df1.info())
df1.drop(['Unnamed: 6'],inplace=True,axis=1)
df1.drop(['Unnamed: 5'],inplace=True,axis=1)
print(df1.info())
print(df1.describe())
print(df1.info())
df1= pd.DataFrame(df1,columns=['Induction time', 'Viscosity' , 'Calorific value'], index = ['BD1', 'BD1-BL', 'HBD1'])
df1.plot.bar()
