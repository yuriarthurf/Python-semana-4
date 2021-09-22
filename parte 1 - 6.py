import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import csv
import collections

#1
def cinco_maiores_downloads():
    with open('googleplaystore.csv', 'r', encoding='utf8') as f:
        conteudo = []
        indices = []
        arquivo_csv = csv.reader(f, delimiter=',', quotechar='"')
        arquivo_organizado = sorted(arquivo_csv, key=lambda row: row[5], reverse=True)
        for i, row in enumerate(arquivo_organizado):
            conteudo.append(row[5])
            indices.append(row[0])
        conteudo = [item.replace("Free", "0") for item in conteudo]
        conteudo = [item.replace("+", "") for item in conteudo]
        conteudo = [item.replace(",", "") for item in conteudo]
        conteudo = [item.replace("Installs", "0") for item in conteudo]
        resultado = list(map(int, conteudo))
        arquivo_organizado2 = sorted(resultado, reverse=True)
        indices2 = indices[8216], indices[8217], indices[8218],indices[8219],indices[8220]
        print(indices[8216], indices[8217], indices[8218],indices[8219],indices[8220])
        print(arquivo_organizado2[0:5])

    plt.bar(indices2, arquivo_organizado2[0:5])
    plt.show()

    return arquivo_organizado2


#2
def categoria_de_apps():
    with open('googleplaystore.csv', 'r', encoding='utf8') as f:
        conteudo = []
        indices = []
        arquivo_csv = csv.reader(f, delimiter=',', quotechar='"')
        arquivo_organizado = sorted(arquivo_csv, key=lambda row: row[1], reverse=True)
        for i, row in enumerate(arquivo_organizado):
            conteudo.append(row[1])
            indices.append(i)

    contador = collections.Counter(conteudo)
    categorias = sorted(contador, key=contador.get, reverse=True)
    indices = contador.values()
    plt.pie(indices, labels=categorias, autopct='%1.1f%%')
    plt.show()


#3
def app_mais_caro():
    with open('googleplaystore.csv', 'r', encoding='utf8') as f:

        conteudo = []
        indices = []
        arquivo_csv = csv.reader(f, delimiter=',', quotechar='"')
        arquivo_organizado = sorted(arquivo_csv, key=lambda row: row[7], reverse=False)
        for i, row in enumerate(arquivo_organizado):
            conteudo.append(row[7])
            indices.append(row[0])
        novo = []
        for x in conteudo:
            novo.append(x.replace("$", ''))
        novo.remove(novo[-1])
        novo.remove(novo[-1])
        nova_lista = map(float, novo)
        lista_completa = list(nova_lista)
        lista_completa2 = sorted(lista_completa, reverse=False)

    print(indices[700], '  ', lista_completa2[-1])



#4
def apps_mais_17():
    with open('googleplaystore.csv', 'r', encoding='utf8') as f:
        conteudo = []
        indices = []
        numero = 0
        arquivo_csv = csv.reader(f, delimiter=',', quotechar='"')
        arquivo_organizado = sorted(arquivo_csv, key=lambda row: row[8], reverse=False)
        for i, row in enumerate(arquivo_organizado):
            conteudo.append(row[8])
            indices.append(row[0])
    print(conteudo.count('Mature 17+'))


#5
def maiores_likes():
    with open('googleplaystore.csv', 'r', encoding='utf8') as f:
        conteudo = []
        indices = []
        arquivo_csv = csv.reader(f, delimiter=',', quotechar='"')
        arquivo_organizado = sorted(arquivo_csv, key=lambda row: row[3], reverse=True)
        for i, row in enumerate(arquivo_organizado):
            indices.append(row[0])
            conteudo.append(row[3])
        conteudo = [item.replace("M", "000") for item in conteudo]
        conteudo = [item.replace("Reviews", "0") for item in conteudo]
        resultado = list(map(float, conteudo))
        arquivo_organizado2 = sorted(resultado, reverse=True)
    print(arquivo_organizado2[0:10])
    print(indices[1010], '-' ,indices[1016], '-' , indices[1549],'-' , indices[1552],'-' , indices[1694]
          ,'-' , indices[1695],'-' , indices[1697],'-' , indices[2396])


