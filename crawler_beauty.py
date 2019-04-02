import requests, sys
import pandas as pd
from bs4 import BeautifulSoup
def crawl_beauty(page = 40):
    url = "https://www.ptt.cc/bbs/Beauty/index.html"

    titles = []
    times = []
    urls = []
    authors = []
    for i in range(page):
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        sel = soup.select("div.title")
        time = soup.select("div.date")
        author = soup.select("div.author")
        u = soup.select("div.btn-group.btn-group-paging a")
        url = "https://www.ptt.cc"+ u[1]["href"]
        urls.append(url)
        for s in sel:
            title = s.get_text().strip()
            titles.append(title)
        for w in time:
            time = w.get_text().strip()
            times.append(time)
        for e in author:
            author = e.get_text().strip()
            authors.append(author)

        df = pd.DataFrame(
            {'titles' : titles,
             'times'  : times,
             'authors': authors}
        )
    return df

if __name__ == '__main__':
    try:
        page = int(sys.argv[1])
        output = crawl_beauty(page = page)
    except:
        output = crawl_beauty()

    output.to_excel('beauty.xlsx')
    print(output)



# def to_df(title, time, author):
#     import pandas as pd
#     df = pd.DataFrame(
#         {'title' : title,
#          'time'  : time,
#          'author': author}
#     )
#     return df
