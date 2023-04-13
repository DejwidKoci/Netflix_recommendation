from nltk.tokenize import word_tokenize
import numpy as np
import pandas as pd
import re
import nltk
import tkinter as tk
from nltk.corpus import stopwords

nltk.download('stopwords')

data = pd.read_csv('netflixData.csv')
data = data.dropna(subset = ['Cast', 'Production Country','Rating'])

movies = data[data['Content Type'] == 'Moive'].reset_index()
movies = movies.drop(['index', 'Show Id', 'Content Type', 'Date Added', 'Release Date', 'Duration', 'Description'], axix = 1)
movies.head()

tv = data[data['Content Type'] == 'TV Show'].reset_index()
tv = tv.drop(['index', 'Show Id', 'Content Type', 'Date Added', 'Release Date', 'Duration', 'Description'], axix = 1)
tv.head()

actors = []
for i in movies['Cast']:
    actor = re.split(r', \s*', i)
    actors.append(actor)

flat_list = []
for sublist in actors:
    for item in sublist:
        flat_list.append(item)

actors_list = sorted(set(flat_list))
binary_actors = [[0] * 0 for i in range(len(set(flat_list)))]
for i in movies['Cast']:
    k = 0
    for j in actors_list:
        if j in i:
            binary_actors[k].append(1.0)
        else:
            binary_actors[k].append(0.0)
        k += 1

binary_actors = pd.DataFrame(binary_actors).transpose()
directors = []
for i in movies['Director']:
    if pd.notna(i):
        director = re.split(r', \s*', i)
        directors.append(director)

flat_list_2 = []
for sublist in directors:
    for item in sublist:
        flat_list_2.append(item)

directors_list = sorted(set(flat_list_2))
binary_directors = [[0] * 0 for i in range(len(set(flat_list_2)))]
for i in movies['Director']:
    k = 0
    for j in directors_list:
        if pd.isna(i):
            binary_directors[k].append(0.0)
        elif j in i:
            binary_directors[k].append(1.0)
        else:
            binary_directors[k].append(0.0)
        k += 1

binary_directors = pd.DataFrame(binary_directors).transpose()

countries = []
for i in movies['Production Country']:
    country = re.split(r', \s*', i)
    countries.append(country)

flat_list_3 = []
for sublist in countries:
    for item in sublist:
        flat_list_3.append(item)

countries_list = sorted(set(flat_list_3))
binary_countries = [[0] * 0 for i in range(len(set(flat_list_3)))]
for i in movies['Production Country']:
    k = 0
    for j in countries_list:
        if j in i:
            binary_countries[k].append(1.0)
        else:
            binary_countries[k].append(0.0)
        k += 1

binary_countries = pd.DataFrame(binary_countries).transpose()


