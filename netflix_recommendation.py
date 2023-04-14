from nltk.tokenize import word_tokenize
import numpy as np
import pandas as pd
import re
import nltk
import tkinter as tk
from nltk.corpus import stopwords
import streamlit as st
import sys


class Recommendation:
    def __init__(self):
        st.title('Netflix For Recommendation')
        user_text = st.text_input('Enter movie / TV Show on Netflix For Recommendations')
        nltk.download('stopwords')
        self.data()
        self.lists()

        if user_text:
            recommendation = self.netflix_recommender(user_text)
            number = 1
            for i in recommendation.iterrows():
                st.write(str(number) + '. ' + str(i[1][0]))
                number += 1
        

    def data(self):
        self.data = pd.read_csv('netflixData.csv')
        self.data = self.data.dropna(subset = ['Cast', 'Production Country','Rating'])

        self.movies = self.data[self.data['Content Type'] == 'Movie'].reset_index()
        self.movies = self.movies.drop(['index', 'Show Id', 'Content Type', 'Date Added',
                            'Release Date', 'Duration', 'Description'], axis=1)
        self.movies.head()

        self.tv = self.data[self.data['Content Type'] == 'TV Show'].reset_index()
        self.tv = self.tv.drop(['index', 'Show Id', 'Content Type', 'Date Added',
                    'Release Date', 'Duration', 'Description'], axis = 1)
        self.tv.head()


    def lists(self):

        actors = []
        for i in self.movies['Cast']:
            actor = re.split(r', \s*', i)
            actors.append(actor)

        flat_list = []
        for sublist in actors:
            for item in sublist:
                flat_list.append(item)

        actors_list = sorted(set(flat_list))
        binary_actors = [[0] * 0 for i in range(len(set(flat_list)))]
        for i in self.movies['Cast']:
            k = 0
            for j in actors_list:
                if j in i:
                    binary_actors[k].append(1.0)
                else:
                    binary_actors[k].append(0.0)
                k += 1

        binary_actors = pd.DataFrame(binary_actors).transpose()
        directors = []
        for i in self.movies['Director']:
            if pd.notna(i):
                director = re.split(r', \s*', i)
                directors.append(director)

        flat_list_2 = []
        for sublist in directors:
            for item in sublist:
                flat_list_2.append(item)

        directors_list = sorted(set(flat_list_2))
        binary_directors = [[0] * 0 for i in range(len(set(flat_list_2)))]
        for i in self.movies['Director']:
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
        for i in self.movies['Production Country']:
            country = re.split(r', \s*', i)
            countries.append(country)

        flat_list_3 = []
        for sublist in countries:
            for item in sublist:
                flat_list_3.append(item)

        countries_list = sorted(set(flat_list_3))
        binary_countries = [[0] * 0 for i in range(len(set(flat_list_3)))]
        for i in self.movies['Production Country']:
            k = 0
            for j in countries_list:
                if j in i:
                    binary_countries[k].append(1.0)
                else:
                    binary_countries[k].append(0.0)
                k += 1

        binary_countries = pd.DataFrame(binary_countries).transpose()

        genres = []
        for i in self.movies['Genres']:
            genre = re.split(r', \s*', i)
            genres.append(genre)

        flat_list_4 = []
        for sublist in genres:
            for item in sublist:
                flat_list_4.append(item)

        genres_list = sorted(set(flat_list_4))
        binary_genres = [[0] * 0 for i in range(len(set(flat_list_4)))]
        for i in self.movies['Genres']:
            k = 0
            for j in genres_list:
                if j in i:
                    binary_genres[k].append(1.0)
                else:
                    binary_genres[k].append(0.0)
                k += 1

        binary_genres = pd.DataFrame(binary_genres).transpose()

        ratings = []
        for i in self.movies['Rating']:
            ratings.append(i)

        ratings_list = sorted(set(ratings))
        binary_ratings = [[0] * 0 for i in range(len(set(ratings)))]
        for i in self.movies['Rating']:
            k = 0
            for j in ratings_list:
                if j in i:
                    binary_ratings[k].append(1.0)
                else:
                    binary_ratings[k].append(0.0)
                k += 1

        binary_ratings = pd.DataFrame(binary_ratings).transpose()
        self.binary = pd.concat([binary_actors, binary_directors, binary_countries, binary_genres], ignore_index = True)

        actors_2 = []
        for i in self.tv['Cast']:
            actor2 = re.split(r', \s*', i)
            actors_2.append(actor2)

        flat_list_5 = []
        for sublist in actors_2:
            for item in sublist:
                flat_list_5.append(item)

        actors_list_2 = sorted(set(flat_list_5))
        binary_actors_2 = [[0] * 0 for i in range(len(set(flat_list_5)))]
        for i in self.tv['Cast']:
            k = 0
            for j in actors_list_2:
                if j in i:
                    binary_actors_2[k].append(1.0)
                else:
                    binary_actors_2[k].append(0.0)
                k += 1

        binary_actors_2 = pd.DataFrame(binary_actors_2).transpose()

        countries_2 = []
        for i in self.tv['Production Country']:
            country2 = re.split(r', \s*', i)
            countries_2.append(country2)

        flat_list_6 = []
        for sublist in countries_2:
            for item in sublist:
                flat_list_6.append(item)

        countries_list_2 = sorted(set(flat_list_6))
        binary_countries_2 = [[0] * 0 for i in range(len(set(flat_list_6)))]
        for i in self.tv['Production Country']:
            k = 0
            for j in countries_list_2:
                if j in i:
                    binary_countries_2[k].append(1.0)
                else:
                    binary_countries_2[k].append(0.0)
                k += 1
            
        binary_countries_2 = pd.DataFrame(binary_countries_2).transpose()

        genres_2 = []
        for i in self.tv['Genres']:
            genre2 = re.split(r', \s*', i)
            genres_2.append(genre2)

        flat_list_7 = []
        for sublist in genres_2:
            for item in sublist:
                flat_list_7.append(item)

        genres_list_2 = sorted(set(flat_list_7))
        binary_genres_2 = [[0] * 0 for i in range(len(set(flat_list_7)))]
        for i in self.tv['Genres']:
            k = 0
            for j in genres_list_2:
                if j in i:
                    binary_genres_2[k].append(1.0)
                else:
                    binary_genres_2[k].append(0.0)
                k += 1

        binary_genres_2 = pd.DataFrame(binary_genres_2).transpose()

        ratings_2 = []
        for i in self.tv['Rating']:
            ratings_2.append(i)

        ratings_list_2 = sorted(set(ratings_2))
        binary_ratings_2 = [[0] * 0 for i in range(len(set(ratings_list_2)))]
        for i in self.tv['Rating']:
            k = 0
            for j in ratings_list_2:
                if j in i:
                    binary_ratings_2[k].append(1.0)
                else:
                    binary_ratings_2[k].append(0.0)
                
                k += 1

        binary_ratings_2 = pd.DataFrame(binary_ratings_2).transpose()
        self.binary_2 = pd.concat([binary_actors_2, binary_countries_2, binary_genres_2], axis = 1, ignore_index = True)

    def netflix_recommender(self, search):
        cs_list = []
        binary_list = []

        if search in self.movies['Title'].values:
            idx = self.movies[self.movies['Title'] == search].index.item()
            for i in self.binary.iloc[idx]:
                binary_list.append(i)

            point_1 = np.array(binary_list).reshape(1, -1)
            point_1 = [val for sublist in point_1 for val in sublist]
            for j in range(len(self.movies)):
                binary_list_2 = []
                for k in self.binary.iloc[j]:
                    binary_list_2.append(k)
                point_2 = np.array(binary_list_2).reshape(1, -1)
                point_2 = [val for sublist in point_2 for val in sublist]
                dot_product = np.dot(point_1, point_2)
                norm_1 = np.linalg.norm(point_1)
                norm_2 = np.linalg.norm(point_2)
                cos_sim = dot_product / (norm_1 * norm_2)
                cs_list.append(cos_sim)

            movies_copy = self.movies.copy() 
            movies_copy['cos_sim'] = cs_list
            results = movies_copy.sort_values('cos_sim', ascending = False )
            results = results[results['title'] != search]
            top_results = results.head(5)
            
            return (top_results)
        
        elif search in self.tv['Title'].values:
            idx = self.tv[self.tv['Title'] == search].index.item()
            for i in self.binary_2.iloc[idx]:
                binary_list.append(i)

            point_1 = np.array(binary_list).reshape(1, -1)
            point_1 = [val for sublist in point_1 for val in sublist]
            for j in range(len(self.tv)):
                binary_list_2 = []
                for k in self.binary_2.iloc[j]:
                    binary_list_2.append(k)

                point_2 = np.array(binary_list_2).reshape(1,-1)
                point_2 = [val for sublist in point_2 for val in sublist]
                dot_product = np.dot(point_1, point_2)
                norm_1 = np.linalg.norm(point_1)
                norm_2 = np.linalg.norm(point_2)
                cos_sim = dot_product / (norm_1 * norm_2)
                cs_list.append(cos_sim)

            tv_copy = self.tv.copy()
            tv_copy['cos_sim'] = cs_list
            results = tv_copy.sort_values('cos_sim', ascending = False)
            results = results[results['Title'] != search]
            top_results = results.head(5)

            return (top_results)
        
        else:
            st.write('Title not in dataset. Please check spelling.')
            sys.exit()


if __name__ == "__main__":
    r = Recommendation()



