import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
from urllib.request import Request, urlopen
import io
from IPython.display import display as print_dataframe
from PIL import Image
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
import plotly.graph_objects as go
import plotly.express as px

info = pd.read_csv('fifa19_info.csv')
stats = pd.read_csv('fifa19_stats.csv')

# print(info.columns)
# print(stats.columns)

#1


# left = pd.DataFrame(info, columns=['ID','Club', 'Name'])
# right = pd.DataFrame(stats, columns=['ID','Agility'])
#
# resultado = pd.merge(left, right, how='inner')

# barcelona = resultado.sort_values(by=['Club', 'Agility'])
# barcelona2 = barcelona.groupby(by='Club').mean()
# display(barcelona2.filter(like='FC Barcelona', axis=0))
# display(barcelona2.filter(like='Real Madrid', axis=0))

#2


# left = pd.DataFrame(info, columns=['Club', 'Value'])
#
# left['Value'] = left['Value'].replace({'€':''}, regex=True)
# left['Value'] = left['Value'].replace({'M':'000000'}, regex=True)
# left['Value'] = left['Value'].replace({'K':''}, regex=True)
# left['Value'] = left['Value'].replace({'110.5':'110000000.5'}, regex=True)
# left['Value'] = left['Value'].replace({'118.5':'118000000.5'}, regex=True)
# left['Value'] = left['Value'].replace({'102.0':'102000000.0'}, regex=True)
# left['Value'] = left['Value'].astype(float)
# barcelona = (left.sort_values(by=['Value'], ascending=False))
# barcelona2 = barcelona.groupby(['Club']).sum()
# barcelona3 = barcelona2.sort_values(by=['Value'], ascending=False)[:10]
# barcelona3['Value'].plot(kind='bar', color=['Blue', 'Yellow', 'Red', 'Orange', 'Yellow', 'Red',
#                                                'Blue', 'Orange', 'Red', 'Orange'])
# plt.show()

#3


# left = pd.DataFrame(info, columns=['ID', 'Nationality'])
# right = pd.DataFrame(stats, columns=['ID'])
# barcelona = (left['Nationality']).value_counts()
# display(barcelona[:5])

#4


# left = pd.DataFrame(info, columns=['ID','Name', 'Photo'])
# right = pd.DataFrame(stats, columns=['ID','Overall'])
#
# resultado = pd.merge(left, right, how='inner')
# print_dataframe(resultado[:5])
# # img = resultado['Photo']
# req = Request('https://conteudo.imguol.com.br/c/esporte/50/2021/04/22/messi-fez-dois-gols-contra-o-getafe-no-campeonato-espanhol-1619131506857_v2_450x337.jpg',
#               headers={'User-Agent': 'Mozilla/5.0'})
# req2 = Request('https://conteudo.imguol.com.br/c/esporte/88/2021/04/07/cristiano-ronaldo-comemora-primeiro-gol-da-partida-entre-juventus-e-napoli-pelo-campeonato-italiano-1617819601477_v2_450x600.jpg',
#               headers={'User-Agent': 'Mozilla/5.0'})
# req3 = Request('https://ogimg.infoglobo.com.br/in/25009725-0eb-4cd/FT1086A/x92798487_FILE-PHOTO-Soccer-FootballChampions-LeagueSemi-Final-Second-LegManchester-City-v-P.jpg.pagespeed.ic.wAtxuz7Wgv.jpg',
#               headers={'User-Agent': 'Mozilla/5.0'})
# req4 = Request('https://images.daznservices.com/di/library/GOAL/31/d7/david-de-gea-manchester-united-2019-20_1pl4a0ujyb0uc1a8ca03kh1z0i.jpg?t=649687797&quality=100',
#               headers={'User-Agent': 'Mozilla/5.0'})
# req5 = Request('https://conteudo.imguol.com.br/c/esporte/21/2021/04/08/belga-kevin-de-bruyne-e-um-dos-titulares-da-selecao-da-europa-1617886889848_v2_450x600.jpg',
#               headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()
# webpage2 = urlopen(req2).read()
# webpage3 = urlopen(req3).read()
# webpage4 = urlopen(req4).read()
# webpage5 = urlopen(req5).read()
# webpage = Image.open(io.BytesIO(webpage))
# webpage2 = Image.open(io.BytesIO(webpage2))
# webpage3 = Image.open(io.BytesIO(webpage3))
# webpage4 = Image.open(io.BytesIO(webpage4))
# webpage5 = Image.open(io.BytesIO(webpage5))
# plt.imshow(webpage)
#plt.imshow(webpage2)
#plt.imshow(webpage3)
#plt.imshow(webpage4)
# plt.imshow(webpage5)
#plt.show()



#5


# left = pd.DataFrame(info, columns=['ID','Name', 'Age'])
# right = pd.DataFrame(stats, columns=['ID',])
#
# resultado = pd.merge(left, right, how='inner')
# barcelona2 = resultado.groupby(by='ID')
# barcelona3 = resultado.sort_values(by='Age')
# display(barcelona3.max())
# display(barcelona3.min())

#6


# left = pd.DataFrame(info, columns=['ID','Name'])
# right = pd.DataFrame(stats, columns=['ID','Overall', 'Penalties'])
#
# resultado = pd.merge(left, right, how='inner')
#
# barcelona = (resultado.sort_values(by=['Overall', 'Name'], ascending=False))
# barcelona2 = barcelona.groupby(by='ID').sum()
# barcelona3 = barcelona2.sort_values(by='Overall', ascending=False)[:10]
# plt.scatter(barcelona3['Overall'], barcelona3['Penalties'],
#                                                             color=['Blue', 'Yellow', 'Red',
#                                                                    'Orange', 'Green', 'Grey',
#                                                                     'Blue', 'Brown', 'Black', 'Purple'])
# plt.show()

#7


# left = pd.DataFrame(info, columns=['ID','Club'])
# right = pd.DataFrame(stats, columns=['ID','Penalties'])
#
# resultado = pd.merge(left, right, how='inner')
#
# barcelona = resultado.sort_values(by=['Club', 'Penalties'])
# barcelona2 = barcelona.groupby(by='Club').mean()
# print(barcelona2.sort_values(by='Penalties', ascending=False)[:1])

#8


# left = pd.DataFrame(info, columns=['Club', 'Value'])
#
# left['Value'] = left['Value'].replace({'€':''}, regex=True)
# left['Value'] = left['Value'].replace({'M':'000000'}, regex=True)
# left['Value'] = left['Value'].replace({'K':''}, regex=True)
# left['Value'] = left['Value'].replace({'110.5':'110000000.5'}, regex=True)
# left['Value'] = left['Value'].replace({'118.5':'118000000.5'}, regex=True)
# left['Value'] = left['Value'].replace({'102.0':'102000000.0'}, regex=True)
# left['Value'] = left['Value'].astype(float)
# barcelona = (left.sort_values(by=['Value'], ascending=False))
# barcelona2 = barcelona.groupby(['Club']).mean()
# barcelona3 = barcelona2.sort_values(by=['Value'], ascending=False)[:1]
# print(barcelona3)

#9


# left = pd.DataFrame(info, columns=['ID','Name'])
# right = pd.DataFrame(stats, columns=['ID','Balance', 'Stamina', 'ShotPower',
#                                       'Marking', 'Dribling', 'SprintSpeed', 'Strength',
#                                       'SlidingTackle', 'GKReflexes'])
#
# resultado = pd.merge(left, right, how='inner')
# barcelona2 = resultado.groupby(by='Name').sum()
#
# messi = (barcelona2.filter(like='L. Messi', axis=0))
# ramos = (barcelona2.filter(like='Sergio Ramos', axis=0))
# gea = (barcelona2.filter(like='De Gea', axis=0))
# categorias = ('Balance', 'Stamina', 'ShotPower',
#                                       'Marking', 'Dribling', 'SprintSpeed', 'Strength',
#                                       'SlidingTackle', 'GKReflexes', 'Balance')
# messi = pd.DataFrame(messi, columns=['Balance', 'Stamina', 'ShotPower',
#                                       'Marking', 'Dribling', 'SprintSpeed', 'Strength',
#                                       'SlidingTackle', 'GKReflexes'])
# lista_messi = messi.values.tolist()
# ramos = pd.DataFrame(ramos, columns=['Balance', 'Stamina', 'ShotPower',
#                                       'Marking', 'Dribling', 'SprintSpeed', 'Strength',
#                                       'SlidingTackle', 'GKReflexes'])
# lista_ramos = ramos.values.tolist()
# gea = pd.DataFrame(gea, columns=['Balance', 'Stamina', 'ShotPower',
#                                       'Marking', 'Dribling', 'SprintSpeed', 'Strength',
#                                       'SlidingTackle', 'GKReflexes'])
# lista_gea = gea.values.tolist()
#
# nova_lista_messi = [95.0, 72.0, 85.0, 33.0, 80.0, 86.0, 59.0, 26.0, 8.0, 95.0]
# nova_lista_ramos = [66.0, 84.0, 79.0, 87.0, 30.0, 75.0, 83.0, 91.0, 11.0, 66.0]
# nova_lista_gea = [43.0, 43.0, 31.0, 15.0, 2.0, 58.0, 64.0, 13.0, 94.0, 43.0]
#
# label_placement = np.linspace(start=0, stop=2*np.pi, num=10)
#
# plt.figure(figsize=(6,6))
# plt.subplot(polar=True)
# plt.plot(label_placement, nova_lista_messi)
# plt.plot(label_placement, nova_lista_ramos)
# plt.plot(label_placement, nova_lista_gea)
#
# lines, labels = plt.thetagrids(np.degrees(label_placement), labels=categorias)
# plt.title('Compara Jogadores', y=1.1, fontdict={'fontsize': 18})
# plt.legend(labels=['Messi','S.Ramos', 'De Gea'],loc=(0.95, 0.8))
#
# plt.show()