from newspaper.article import Article

def read_article(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    print(article.text)
    # print 'SUMMARY'
    print(article.summary)


# url = 'http://espn.go.com/blog/new-york/mets/post/_/id/116024/series-preview-mets-at-royals'
url = 'http://espn.go.com/mlb/story/_/page/seasonpreview_wsbluejays/why-toronto-blue-jays-win-world-series'
url = 'http://www.nydailynews.com/news/crime/slain-va-trooper-made-arrest-woman-dead-son-car-article-1.2585840'
url = 'http://www.bbc.com/news/magazine-35942519'
url = 'http://www.bbc.com/news/uk-35948256'
url = 'http://www.bbc.com/news/world-europe-35948009'
url = 'http://observer.com/2016/03/rogerebert-com-holds-women-writers-week-to-celebrate-diversity/'
read_article(url)