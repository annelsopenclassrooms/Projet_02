from book_information import get_book_infos, fill_csv
 
import requests
from bs4 import BeautifulSoup
from category import get_category_url_list, get_url_book_list
# Get dictionnary with Name : URL for categories


def main():


    category_dict = get_categories("http://books.toscrape.com/index.html")
    
    for category, url in category_dict.items():

        get_category_url_list(url)
        all_url_from_category = get_category_url_list(url)    

        all_books=[]
        for url in all_url_from_category:
            #extend : Append list elements to list
            all_books.extend(get_url_book_list(url))

        all_info_in_category=[]
        for book in all_books:
            all_info_in_category.append(get_book_infos(book))

                 
        fill_csv(all_info_in_category, category)

def get_categories(home_url):

    page = requests.get(home_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    list = soup.find(class_= "nav nav-list").find_all("li")
    category_dict = {}
    for category_html in list:
        category_name = category_html.find("a").get_text().strip()
        link = category_html.find("a")['href'] 

        category_dict[category_name] = "http://books.toscrape.com/" + link
    del category_dict["Books"]
    return category_dict

if __name__=="__main__":
    main()