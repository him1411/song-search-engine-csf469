import bs4, sys

with open(sys.argv[1], 'r') as f:
    webpage = f.read().decode('utf-8')

soup = bs4.BeautifulSoup(webpage)
for node in soup.findAll('html'):
    print u''.join(node.findAll(text=True)).encode('utf-8')

