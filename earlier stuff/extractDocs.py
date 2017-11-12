import bs4
import urllib3

def createDocumentForQuestion(docNum):
    site = open('w.html')

    stackSoup = bs4.BeautifulSoup(site.read(),"lxml")
    text = stackSoup.select('p.label-key')
    label = text[1].getText() + '_' + text[3].getText()[40:text[3].getText().find('t')]
    text = stackSoup.select('div.post-text p')
    label = label + '_' + str(len(text))
    fullText = ''
    for i in range(0,len(text)):
        fullText = fullText + text[i].getText()
    with open( str(docNum) + '_' + label + '_' + '.html','w') as fid:
        fid.write(fullText)


i=0
with open('linksCorpus.txt') as f:
    for line in f:
        i = i + 1
        http = urllib3.PoolManager()
        print(line.strip())
        question_page = http.request('get',line.strip())
        with open('w.html', 'w') as fid:
            fid.write(str(question_page.data))
        createDocumentForQuestion(str(i))

