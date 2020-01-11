from bs4 import BeautifulSoup
import requests

def get_all_post_in_page(soup):
    posts = soup.find('div', id="main_columns").find_all('article')
    
    for post in posts:
        
        url_post = post.find('a', class_='article-link').get('href')
        r = requests.get(url_post)
        soup = BeautifulSoup(r.text, 'lxml')

        title = soup.find('div', class_='post-title').find('h1', class_='entry-title').text
        body = soup.find('div', class_='entry-content').text
        images = soup.find_all('img')
        datePublished = soup.find('div', class_='post-meta').find('time', class_='entry-date').text


def next_page(soup):
    return soup.find('div', class_='pagination').find('span').findNextSibling().get('href')

def main():
    ''' URL = NONE IF PAGES ARE OVER '''
    url = 'https://tproger.ru/'
    pages = 3

    for page in range(pages):
        print(f'CURRENT PAGE IS = {page+1}')

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')

        get_all_post_in_page(soup)

        url = next_page(soup)


if __name__ == '__main__':
    main()