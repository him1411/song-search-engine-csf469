## Song Search Engine for abpout 50000 Songs

A tf-idf based Search Engine for searching songs on. The main purpose of this project is understand how vector space based retrieval models work.
More on [Tf-Idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf). Install all the dependencies using pip3.



If you face any problem, install `nltk` separately.

#### Installing `nltk`

```
$ pip3 install nltk
$ python3
>>> import nltk
>>> nltk.download()
	Packages: all
```

## DATA STRUCTURES USED:

### Document_tokens_list 
Contains lists enclosed within a list
It will contain the stemmed tokens from each file in the corpus as individual lists. All are appended to
make a list. Example: 
```
[[‘i’,’play’,’cricket’],[‘sachin’,’tendulkar’],[‘india’,’is’,’best’]]
``` 
### Vocabulary
Will contain a dictionary of all the unique words in the corpus. Example: 
```
{‘i’: 1, ‘play’:2, ‘cricket’:3, ‘sachin’:4, ‘tendulkar’ :5, ‘india’:6 , ‘is’ :7, ‘best’:8]
```
### Prime Dictionary
A nested dictionary containing the following structure explained through the following example:(Numbers are just representational )

```
{‘i’:{‘0’: {‘TF’:1 ,“IDF”:0.8, ‘TF-IF’ : 0.8} , ‘1’:{‘TF’: 2 ,‘IDF’: 0.4, ‘TF-IDF’:0.8}, ‘2’:{‘TF’: 0 ,‘IDF’: 0.3,
‘TF-IDF’:0}} , ‘cricket’ :{‘0’: {‘TF’:2 ,“IDF”:0.6, ‘TF-IF’ :1.2} , ‘1’:{‘TF’: 0 ,‘IDF’: 0.4, ‘TF-IDF’:0}, ‘2’:{ ‘TF’: 1
,‘IDF’: 0.4, ‘TF-IDF’:0.4}}}
```
### Scores
A dictionary which will contain the scores of the documents after inputting the query and running cosine similarity algorithm. Example :
```
{‘0’: 0.2323 , ‘1’: 0.3125 , ‘2’ : 0.467 }
```
## Creating The GUI
GUI has been created using flask framework of python and the front end web pages have been designed using HTML, CSS and Bootstrap.

### The Search Engine Home page.

![](https://i.imgur.com/uIDeHaq.png?1)

### The Result page

![](https://i.imgur.com/LrN9dEA.png)
## Machine specs:
1. Processor: i7 4700HQ
2. Ram: 24 GB DDR3
3. OS: Ubuntu 16.04 LTS

## Results
Index building time:
- No stemming/lemmatization - 41.67s
- Lemmatized text - 76.97s
- Stemmed text - 146.13 s

Memory usage: around 410 MB.



## Members
[Shubadeep Jana](https://github.com/subhadip7879)

[Shardul Parab](https://github.com/shardulparab97)

[Himanshu Gupta](https://github.com/him1411)
