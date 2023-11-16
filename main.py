'''
import csv
from pathlib import Path
from pdfminer.high_level import extract_text


folder = Path('pdfs')
csv_file = Path('output.csv')

with csv_file.open('w', encoding='utf-8') as f:
    writer = csv.writer(f, csv.QUOTE_ALL)

    writer.writerow(['FileName', 'Text'])

    for pdf_file in folder.glob('*.pdf'):
        pdf_text = extract_text(pdf_file).replace('\n', '|')
        writer.writerow([pdf_file.name, pdf_text])
'''


# packages to store and manipulate data
import pandas as pd
import numpy as np

# plotting packages
import matplotlib.pyplot as plt
import seaborn as sns

# model building package
import sklearn

# package to clean text
import re

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


papers = pd.read_csv('output.csv')

print(papers.head())

# Remove punctuation
papers['paper_text_processed'] = \
papers['Text'].map(lambda x: re.sub('[,\.!?]', '', x))# Convert the titles to lowercase
papers['paper_text_processed'] = \
papers['paper_text_processed'].map(lambda x: x.lower())# Print out the first rows of papers
papers['paper_text_processed'].head()

print(papers['paper_text_processed'].head)

# Import the wordcloud library
from wordcloud import WordCloud # Join the different processed titles together.
long_string = ','.join(list(papers['paper_text_processed'].values))# Create a WordCloud object
wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')# Generate a word cloud
wordcloud.generate(long_string)# Visualize the word cloud
wordcloud.to_image()

