import requests
import lxml.html as html


def get_all_post_in_page(page):
    posts = page.xpath('//div[@id="main_columns"]/article')
    links = posts[0].xpath('//a[@class="article-link"]/@href')

    for url in links:
        r = requests.get(url)
        tree = html.fromstring(r.text)

        article = tree.xpath('//article | //article/div')[0]

        title = article.xpath('.//div[@class="post-title"]/h1/text()')[0]
        body = article.xpath('.//div[contains(@class, "entry-container")]/div[@class="entry-content"]/p/text()')
        img_headers = article.xpath('.//div[@class="entry-image"]/img/@src')
        allImgs = article.xpath('.//img/@data-src')
        datePublished = article.xpath('.//div[@class="post-title"]/div[contains(@class, "post-meta")]/ul/li/time/text()')[0]
        datetimePublished = article.xpath('.//div[@class="post-title"]/div[contains(@class, "post-meta")]/ul/li/time/@datetime')[0]


def next_page(tree):
    nextPage = tree.xpath('//div[@id="content"]/div[@class="pagination"]/span')[0]
    try: 
        return nextPage.getnext().xpath('@href')[0]
    except AttributeError:
        raise AttributeError(f'This page is last. Current page - {nextPage.text}.')
     

def main():
    url = 'https://tproger.ru/'
    pages = 1

    for page in range(pages):
        print(f'CURRENT PAGE IS = {page+1}')

        r = requests.get(url)
        tree = html.fromstring(r.text)

        get_all_post_in_page(tree)

        url = next_page(tree)


if __name__ == '__main__':
    main()
