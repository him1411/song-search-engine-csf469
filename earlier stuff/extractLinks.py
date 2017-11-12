import bs4
import urllib3
f = open("linksCorpus.txt","w")
f.close()
for x in range(1,900000):
    #save the page source
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
    }
    http = urllib3.PoolManager()
    question_page = http.request('get', 'https://stackoverflow.com/questions?page=' + str(x) + '&sort=votes')
    with open(str(x) + '.html', 'w') as fid:
        fid.write(str(question_page.data))
    site = open(str(x) + '.html')
    soup = bs4.BeautifulSoup(site.read(),"lxml")
    link = soup.select('a[class="question-hyperlink"]')
    print('page' + str(x))
    f = open("linksCorpus.txt","a")
    for y in range(0,len(link)):
        f.write('https://stackoverflow.com/' + str(link[y])[37:str(link[y]).find('>')-1] + '\n')
        print(link[y])
    f.close()
    #save the link to s file
