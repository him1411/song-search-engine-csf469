import bs4
import urllib3

def createDocumentForQuestion(docNum):
    site = open('w.html')

    stackSoup = bs4.BeautifulSoup(site.read(),"lxml")
    text = stackSoup.select('div.post-text p')
    fullText = ''
    for i in range(0,len(text)):
        fullText = fullText + text[i].getText()
    with open( str(docNum)+ '.html','w') as fid:
        fid.write(fullText)


i=0
with open('linksCorpus2.txt') as f:
    for line in f:
        i = i + 1
        http = urllib3.PoolManager()
        print(line.strip())
        question_page = http.request('get',line.strip())
        with open('w.html', 'w') as fid:
            fid.write(str(question_page.data))
        createDocumentForQuestion(str(i))
