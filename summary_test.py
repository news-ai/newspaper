from newspaper.article import Article


def read_article_without_author(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    # print article.text
    print article.opening_paragraph


url = 'http://www.nydailynews.com/news/crime/slain-va-trooper-made-arrest-woman-dead-son-car-article-1.2585840'
read_article_without_author(url)
