import urllib.request
from pathlib import Path
import nltk

filenames = ['texts/02.txt', 'texts/02a.txt', 'texts/02a01.txt','texts/02a02.txt','texts/03.txt','texts/04.txt','texts/04a.txt','texts/05.txt','texts/10.txt','texts/10a.txt','texts/10a01.txt','texts/10a02.txt', 'texts/10a03.txt']
with open('texts/onefile.txt', 'w', encoding="utf-8") as outfile:
    for fname in filenames:
        with open(fname, encoding="utf-8") as infile:
            for line in infile:
                outfile.write(line)


with open("./texts/onefile.txt", encoding="utf-8") as f:
    file_contents = f.read()

nltk.download('punkt', download_dir='./data/nltk_data')
file_contents = file_contents.lower()
tokens = nltk.word_tokenize(file_contents)
text = nltk.Text(tokens)

type(text)

annex1_list = text.concordance_list(['annex', 'i'], width=300, lines=2000)
annex2_list = text.concordance_list(['annex', 'ii'], width=300, lines=336)
nonannex_list = text.concordance_list('non-annex', width=300, lines=476)

with open('./data/annex2_list.txt', 'w') as f:
    for i in range(len(annex2_list)):
        f.write(annex2_list[i].line)
        f.write('\n')

with open('./data/annex1_list.txt', 'w') as f:
    for i in range(len(annex1_list)):
        f.write(annex1_list[i].line)
        f.write('\n')

with open('./data/nonannex_list.txt', 'w') as f:
    for i in range(len(nonannex_list)):
        f.write(nonannex_list[i].line)
        f.write('\n')        

#https://stackoverflow.com/questions/72982502/how-to-do-sentiment-analysis-on-a-txt-using-stanford-nlp