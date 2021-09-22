import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display as print_dataframe

df = pd.read_csv('googleplaystore.csv')
#print(df.columns)

#1
data = pd.DataFrame(df)
# x = list(df.sort_values(by=['Installs'], ascending=False)['App'][0:6])
# y = list(df.sort_values(by=['Installs'], ascending=False)['Installs'][0:6])
# plt.bar(x, y)
# plt.show()

#2
# y = data['Category'].value_counts()
# x = data['Category'].value_counts()
# dict = x.to_dict()
# plt.pie(y, labels=dict.keys(), autopct='%1.1f%%')
# plt.show()

#3
# data['Price'] = data['Price'].str.replace('[$, Everyone]', '', regex=True)
# print_dataframe(data.sort_values(by=['Price'], ascending=False)[['App', 'Price']][99:100])

#4
# lista = (df['Content Rating']).value_counts()
# print('Mature 17+' , '-->',lista[2])

#5
lista = (data[['Rating', 'App']])
lista2 = lista.sort_values(by=['Rating'], ascending=False)
print(lista2[:11])





