import urllib.request
from pathlib import Path
import nltk
nltk.download('punkt')

import os

# Specify the directory path
directory = 'docs/textfiles'

# Initialize an empty list to store file names
file_list = []


# Iterate over each file in the directory
for filename in os.listdir(directory):
    # Check if the file is a regular file (not a directory)
    full_path = os.path.join(directory, filename)
    file_list.append(full_path)

# Print the list of file names
print(file_list)

with open('docs/onefile.txt', 'w', encoding="utf-8") as outfile:
    for fname in file_list:
        print(fname)
        with open(fname, encoding="utf-8") as infile:
            for line in infile:
                outfile.write(line)

with open("docs/onefile.txt", encoding="utf-8") as f:
    file_contents = f.read()

nltk.download('punkt', download_dir='./data/nltk_data')
file_contents = file_contents.lower()
tokens = nltk.word_tokenize(file_contents)
text = nltk.Text(tokens)

type(text)

annex1_list = text.concordance_list(['annex', 'i'], width=300, lines=2000)
annex2_list = text.concordance_list(['annex', 'ii'], width=300, lines=336)
nonannex_list = text.concordance_list('non-annex', width=300, lines=476)

#Words of persuasion: 
invites_list = text.concordance_list(['invites'], width=300, lines=2000)
persuades = text.concordance_list(['persuades'], width=300, lines=2000)
stresses = text.concordance_list(['stresses'], width=300, lines=2000)
encourages = text.concordance_list(['encourages'], width=300, lines=2000)
requests = text.concordance_list(['requests'], width=300, lines=2000)
urges = text.concordance_list(['urges'], width=300, lines=2000)
recommends = text.concordance_list(['recommends'], width=300, lines=2000)
considers = text.concordance_list(['considers'], width=300, lines=2000)
calls_upon = text.concordance_list(['calls', 'upon'], width=300, lines=2000)

#Words of assertion: 
adopts = text.concordance_list(['adopts'], width=300, lines=2000)
decides = text.concordance_list(['decides'], width=300, lines=2000)

#Words of coercion: 
mandates = text.concordance_list(['mandates'], width=300, lines=2000)

#Other words: 
developing_countries = text.concordance_list(['developing', 'countries'], width=300, lines=2000)
developed_countries = text.concordance_list(['developed', 'countries'], width=300, lines=2000)
african_countries = text.concordance_list(['African', 'countries'], width=300, lines=2000)
the_least_developed_countries = text.concordance_list(['the', 'least', 'developed', 'countries'], width=300, lines=2000)
small_island_developing_states = text.concordance_list(['small', 'island', 'developing', 'states'], width=300, lines=2000)

with open('./data/annex2_list.txt', 'w', encoding="utf-8") as f:
    for i in range(len(annex2_list)):
        f.write(annex2_list[i].line)
        f.write('\n')

with open('./data/annex1_list.txt', 'w', encoding="utf-8") as f:
    for i in range(len(annex1_list)):
        f.write(annex1_list[i].line)
        f.write('\n')

with open('./data/nonannex_list.txt', 'w', encoding="utf-8") as f:
    for i in range(len(nonannex_list)):
        f.write(nonannex_list[i].line)
        f.write('\n')   

with open('./data/invites_list.txt', 'w', encoding="utf-8") as f:
    for i in range(len(invites_list)):
        f.write(invites_list[i].line)
        f.write('\n')   

with open('./data/persuades.txt', 'w', encoding="utf-8") as f:
    for i in range(len(persuades)):
        f.write(persuades[i].line)
        f.write('\n')           

with open('./data/decides.txt', 'w', encoding="utf-8") as f:
    for i in range(len(decides)):
        f.write(decides[i].line)
        f.write('\n')   

with open('./data/encourages.txt', 'w', encoding="utf-8") as f:
    for i in range(len(encourages)):
        f.write(encourages[i].line)
        f.write('\n')  

with open('./data/stresses.txt', 'w', encoding="utf-8") as f:
    for i in range(len(stresses)):
        f.write(stresses[i].line)
        f.write('\n')  

with open('./data/requests.txt', 'w', encoding="utf-8") as f:
    for i in range(len(requests)):
        f.write(requests[i].line)
        f.write('\n')  

with open('./data/urges.txt', 'w', encoding="utf-8") as f:
    for i in range(len(urges)):
        f.write(urges[i].line)
        f.write('\n')  

with open('./data/recommends.txt', 'w', encoding="utf-8") as f:
    for i in range(len(recommends)):
        f.write(recommends[i].line)
        f.write('\n')  
        
with open('./data/considers.txt', 'w', encoding="utf-8") as f:
    for i in range(len(considers)):
        f.write(considers[i].line)
        f.write('\n')  

with open('./data/adopts.txt', 'w', encoding="utf-8") as f:
    for i in range(len(adopts)):
        f.write(adopts[i].line)
        f.write('\n')  

with open('./data/mandates.txt', 'w', encoding="utf-8") as f:
    for i in range(len(mandates)):
        f.write(mandates[i].line)
        f.write('\n')  

with open('./data/developing_countries.txt', 'w', encoding="utf-8") as f:
    for i in range(len(developing_countries)):
        f.write(developing_countries[i].line)
        f.write('\n')  

with open('./data/developed_countries.txt', 'w', encoding="utf-8") as f:
    for i in range(len(developed_countries)):
        f.write(developed_countries[i].line)
        f.write('\n')  

with open('./data/african_countries.txt', 'w', encoding="utf-8") as f:
    for i in range(len(african_countries)):
        f.write(african_countries[i].line)
        f.write('\n')  

with open('./data/the_least_developed_countries.txt', 'w', encoding="utf-8") as f:
    for i in range(len(the_least_developed_countries)):
        f.write(the_least_developed_countries[i].line)
        f.write('\n')  

with open('./data/small_island_developing_states.txt', 'w', encoding="utf-8") as f:
    for i in range(len(small_island_developing_states)):
        f.write(small_island_developing_states[i].line)
        f.write('\n')  

#https://stackoverflow.com/questions/72982502/how-to-do-sentiment-analysis-on-a-txt-using-stanford-nlp