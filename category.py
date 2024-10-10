from book_information import get_book_infos, fill_csv
import requests
from bs4 import BeautifulSoup

def get_url_book_list(category_url):

    url = category_url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    books = soup.find_all("h3")
    book_url_list = []
    for book in books:
        link = book.find("a")['href']   
        slice = link[8:len(link)]
        full_link = "http://books.toscrape.com/catalogue" + slice 
        book_url_list.append(full_link)  
         
    return book_url_list
 
def get_category_url_list(category_url):
    list = [category_url] 
    next = next_page(category_url)
    base = category_url[0:len(category_url)-11]+ "/"
    while True:
        if next:
            list.append(base + next)
            next = next_page(base + next)
        else:
            break
    return (list)

def next_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    next = soup.find(class_= "next")
    if next:
        next_url =next.find("a")['href']   
        return next_url
    else:
        return None




