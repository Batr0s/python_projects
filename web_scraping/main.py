import requests
import bs4

# The code will get the books with five star rating of every page
page = 1
# This web page is made specifically to practice web scrapping
resultado = requests.get(f'https://books.toscrape.com/catalogue/page-{page}.html')
soup = bs4.BeautifulSoup(resultado.text, 'lxml')

while resultado.status_code != 404:
    five_star_element = soup.select('.Five + h3 a')
    print(f'Page nº{page}:')
    for book_title in five_star_element:
        print(book_title['title'])
    print('\n')
    page += 1
    resultado = requests.get(f'https://books.toscrape.com/catalogue/page-{page}.html')
    soup = bs4.BeautifulSoup(resultado.text, 'lxml')
