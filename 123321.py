import PyPDF2
from pdfminer import high_level
import glob
import os
import pathlib
from datetime import datetime


onlyfiles = glob.glob('pdfs/*.pdf')  #creates a list of file paths to each pdf using glob.  https://docs.python.org/3/library/glob.html

for file in onlyfiles:                                     #for each file in the list - so all the things below will happen to each pdf file
    reader = PyPDF2.PdfReader(open(file,'rb'))             #open with pypdf
    meta = reader.metadata                                 #read the metadata
    pageObj = len(reader.pages)                            #count the pages
    page = reader.pages

#   print(meta.title)                                      #print statements were just for checking that various steps were working
#   print(meta.author)
#   print(pageObj)

    name = os.path.basename(file)                          #get the basename of the file using os so we can add it to the new text files
    path = pathlib.Path(name)                              
    filename_wo_ext = path.with_suffix('')                 #remove the file extension
#   print(filename_wo_ext)

#   print(meta.creation_date)
#  dateonly = meta.creation_date.strptime("%Y%m%d")     #reformat date/time info to remove hours and seconds
    text = high_level.extract_text(file)                              #extract text from the pdf
    all = (meta.title, meta.author, pageObj, meta.creation_date)  #combine all the metadata and text
#    all = (meta.title, meta.author, pageObj, text)  #combine all the metadata and text

    all = str(all)                                         #convert the metadata and text to a string so it can be written to the file
#    with open(f'texts/{filename_wo_ext}{dateonly}.txt', 'w') as fp:   #write to a text file named using the original file name and the creation date
#           fp.write(all)    
#    with open(f'texts/{dateonly}.txt', 'w') as fp:   #write to a text file named using the original file name and the creation date
#           fp.write(text)

    with open(f'texts/metadata.csv', 'a') as fp: #writes the metadata, a line break, and the text to a text file that we can now use for text analysis
        for file in onlyfiles: 
            fp.write(all)
#        fp.write("\n")
#        fp.write(text)