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

