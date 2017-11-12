from tkinter import *
from tkinter import ttk
import sys
import glob
import os
from math import log
import nltk
from nltk import word_tokenize
from nltk import FreqDist
import sys
import math
from nltk.stem.snowball import SnowballStemmer
from collections import defaultdict
import pickle
import json
import store_scores_gui
from store_scores_gui import main_class


#code in question
def process_function():
    abc = v.get()
    main_class.queryStr = abc
    main_class.terminal_function()
    
    #find max wala function#######################
    with open('savers/store.json') as json_data:
        score = json.load(json_data)
    sorted_score = sorted(score, key=score.get, reverse=True)
    docFiles = [f for f in os.listdir('./corpus') if f.endswith(".html")]
    docFiles.sort()
    for i in sorted_score[:10]:
        print(i)

    #end of find max################################

    linkNumber_list = sorted_score[:10]
    docList = []
    x=0
    f = open("linksCorpus.txt")
    data = f.read()
    data = data.split("\n")
    print(linkNumber_list)
    for linkNum in linkNumber_list:
        docList.append(data[int(linkNum)]);
    print(docList)
    

#Code in question

main = Tk()
main.title("Stackoverflow search engine")
main.geometry('800x600')

frame1 = ttk.Frame(main, height=4000, width=8000)
frame1.pack()

v = StringVar()
v.set("kindly enter your search query here")
entry = Entry(frame1, width=61000, textvariable=v)
entry.pack()
button1 = ttk.Button(frame1, text="Search", command=process_function )
button1.pack()
button1.bind ('<ButtonPress>', lambda e: progressbar.start())
   
button2 = ttk.Button(frame1, text="Quit")
button2.pack()
button2.bind ('<ButtonPress>', lambda e: exit())

progressbar = ttk.Progressbar(frame1, orient = HORIZONTAL, length = 200,      mode = 'indeterminate')
progressbar.pack()



listbox = Listbox(frame1, height =200, width=400)
listbox.pack()

progressbar.stop()

main.mainloop()


