import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display as print_dataframe

df = pd.read_csv('actors.csv')

#1
#print_dataframe(df.sort_values(by=['Number of Movies'], ascending=False)[['Actor','Number of Movies']][:1])

#2
# soma = (df['Number of Movies'])
# print(soma.sum())

#3
#print_dataframe(df.sort_values(by=['Average per Movie'], ascending=False)[['Actor','Average per Movie']][:1])

#4
filmes = (df['#1 Movie'])
print(filmes.value_counts())

