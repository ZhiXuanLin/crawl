from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
def crawl_feder(page = 87):
    re_a = re.compile('</?\w+[^>]*>')
    re_b = re.compile('&/?\w+[^>]*;')
    url = 'http://www.let.rug.nl/usa/documents/1786-1800/the-federalist-papers/the-federalist-1.php'
    text = []
    for i in range(1,page):
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        sel = soup.select('p')
        newurl = soup.select('div.prevnext a')
        url = 'http://www.let.rug.nl/usa/documents/1786-1800/the-federalist-papers/'+newurl[1]['href']
        result = re_a.sub('', str(sel))
        result1 = re_b.sub(' ',result)
        text.append(result1)
    url2 = 'http://www.let.rug.nl/usa/documents/1786-1800/the-federalist-papers/?fbclid=IwAR0da_aaLdG4Rxw98d2mUfXlIdHcV8yor772gBWlQ7T9q7n0bDfbDfvkaBU'
    r1 = requests.get(url2)
    soup = BeautifulSoup(r1.text,"html.parser")
    re_label = re.compile('</?\w+[^>]*>')
    re_author = re.compile(r'[(](.*?)[)]', re.S)
    title = []
    author = []
    for i in range(1,page,1):
        titles = soup.select('li:nth-of-type(%d)'%(i+1))
        result = re_label.sub('', str(titles))
        title.append(result)
    for w in range(0,len(title),1):
        authors = min(re.findall(re_author, title[w]),key=lambda x:len(x))
        author.append(authors.replace(' ',''))


    alldata = {
                'title': title,
                'author':author,
                'text':text
    }
    feder = pd.DataFrame(alldata)
    return feder

if __name__ == '__main__':
    try:
        page = int(sys.argv[1])
        output = crawl_feder(page = page)
    except:
        output = crawl_feder()

    output.to_excel('feder.xlsx')
    print(output)
