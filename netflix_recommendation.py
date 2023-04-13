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

genres = []
for i in movies['Genres']:
    genre = re.split(r', \s*', i)
    genres.append(genre)

flat_list_4 = []
for sublist in genres:
    for item in sublist:
        flat_list_4.append(item)

genres_list = sorted(set(flat_list_4))
binary_genres = [[0] * 0 for i in range(len(set(flat_list_4)))]
for i in movies['Genres']:
    k = 0
    for j in genres_list:
        if j in i:
            binary_genres[k].append(1.0)
        else:
            binary_genres[k].append(0.0)
        k += 1

binary_genres = pd.DataFrame(binary_genres).transpose()

ratings = []
for i in movies['Rating']:
    ratings.append(i)

ratings_list = sorted(set(ratings))
binary_ratings = [[0] * 0 for i in range(len(set(ratings)))]
for i in movies['Rating']:
    k =0
    for j in ratings_list:
        if j in i:
            binary_ratings[k].append(1.0)
        else:
            binary_ratings[k].append(0.0)
        k += 1

binary_ratings = pd.DataFrame(binary_ratings).transpose()
binary = pd.concat([binary_actors, binary_directors, binary_countries, binary_genres], ignore_index = True)

actors_2 = []
for i in tv['Cast']:
    actor2 = re.split(r', \s*', i)
    actors_2.append(actor2)

flat_list_5 = []
for sublist in actors_2:
    for item in sublist:
        flat_list_5.append(item)

actors_list_2 = sorted(set(flat_list_5))
binary_actors_2 = [[0] * 0 for i in range(len(set(flat_list_5)))]
for i in tv['Cast']:
    k = 0
    for j in actors_list_2:
        if j in i:
            binary_actors_2[k].append(1.0)
        else:
            binary_actors_2[k].append(0.0)
        k += 1

binary_actors_2 = pd.DataFrame(binary_actors_2).transpose()

countries_2 = []
for i in tv['Production Country']:
    country2 = re.split(r', \s*', i)
    countries_2.append(country2)

flat_list_6 = []
for sublist in countries_2:
    for item in sublist:
        flat_list_6.append(item)

countries_list_2 = sorted(set(flat_list_6))
binary_countries_2 = [[0] * 0 for i in range(len(set(flat_list_6)))]
for i in tv['Production Country']:
    k = 0
    for j in countries_list-2:
        if j in i:
            binary_countries_2[k].append(1.0)
        else:
            binary_countries_2[k].append(0.0)
        k += 1
    
binary_countries_2 = pd.DataFrame(binary_countries_2).transpose()

genres_2 = []
for i in tv['Genres']:
    genre2 = re.split(r', \s*', i)
    genres_2.append(genre2)

flat_list_7 = []
for sublist in genres_2:
    for item in sublist:
        flat_list_7.append(item)

genres_list_2 = sorted(set(flat_list_7))
binary_genres_2 = [[0] * 0 for i in range(len(set(flat_list_7)))]
for i in tv['Genres']:
    k = 0
    for j in genres_list_2:
        if j in i:
            binary_genres_2[k].append(1.0)
        else:
            binary_genres_2[k].append(0.0)
        k += 1

binary_genres_2 = pd.DataFrame(binary_genres_2).transpose()

ratings_2 = []
for i in tv['Rating']:
    ratings_2.append(i)

ratings_list_2 = sorted(set(ratings_2))
binary_ratings_2 = [[0] * 0 for i in range(len(set(ratings_list_2)))]
for i in tv['Rating']:
    k = 0
    for j in ratings_list_2:
        if j in i:
            binary_ratings_2[k].append(1.0)
        else:
            binary_ratings_2[k].append(0.0)
        
        k += 1

binary_ratings_2 = pd.DataFrame(binary_ratings_2).transpose()
binary_2 = pd.concat([binary_actors_2, binary_countries_2, binary_genres_2], axis = 1, ignore_index = True)







