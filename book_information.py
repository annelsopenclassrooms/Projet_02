import requests
from bs4 import BeautifulSoup
import csv
import os


""" 
ok ● product_page_url
ok ● universal_ product_code (upc)
ok ● title
ok● price_including_tax
ok● price_excluding_tax
ok● number_available
ok● product_description
ok● category
ok● review_rating
ok● image_url 

individuel
● product_page_url
● product_description
● category
● review_rating
● image_url 

tableau
● title
● universal_ product_code (upc)
● price_including_tax
● price_excluding_tax
● number_available


"""

def main():

    all_info_in_category=[]
    #print(get_book_infos("http://books.toscrape.com/catalogue/life-the-universe-and-everything-hitchhikers-guide-to-the-galaxy-3_189/index.html"))
    get_book_infos("http://books.toscrape.com/catalogue/life-the-universe-and-everything-hitchhikers-guide-to-the-galaxy-3_189/index.html")

    all_info_in_category.append(get_book_infos("http://books.toscrape.com/catalogue/life-the-universe-and-everything-hitchhikers-guide-to-the-galaxy-3_189/index.html"))


    fill_csv(all_info_in_category, "SF")

def get_book_infos(book_url):
    url = book_url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    informations = {}

    title = soup.find(class_="active").string
    informations["title"] = title
    product_information_html = soup.find(class_= "table table-striped").find_all("tr")

    for i in product_information_html:
        key = i.find("th").string
        value = i.find("td").string
        informations[key] = value
        
    #Get number_available
    text =  (informations["Availability"])
    number = ""

    for char in text:
        if char.isdigit():
            number = number + char
            
    informations["number_available"] = number

    #Delete unused infos from (class_= "table table-striped").find_all("tr")
    informations.pop("Product Type", None)
    informations.pop("Tax", None)
    informations.pop("Availability", None)
    informations.pop("Number of reviews", None)
    
    #Get product_page_url
    informations["product_page_url"] = book_url

    #Get description
    description = soup.find("meta", attrs={"name": "description"}).get("content")
    informations["description"] = description

    #Get category
    results= soup.find_all('a')

    for result in results:
        result_str = str(result)
        #if "category" in result:
        if "/category/books/" in result_str:
            category = result.string
        
    informations["category"] = category

    #get rating

    star = str(soup.find(class_= "star-rating"))
    line = star.split('\n', 1)[0]
    slice = line[22:len(line)-2]
    match slice:
        case "Zero":
            rating = 0
        case "One":
            rating = 1
        case "Two":
            rating = 2
        case "Three":
            rating = 3
        case "Four":
            rating = 4
        case "Five":
            rating = 5

    informations["review_rating"] = rating

    #Get image_url
    image_html = soup.find(class_= "item active").find("img")["src"]
    slice = image_html[5:len(image_html)]
    img_url = "http://books.toscrape.com" + slice
    informations["image_url"] = img_url
    image_url = img_url
    download_image(image_url, "images")

    #reorder infomations
    reordered_informations = {}
    print(informations.keys())

    reordered_informations["product_page_url"] = informations["product_page_url"]
    reordered_informations["UPC"] = informations["UPC"]
    reordered_informations["title"] = informations["title"]
    reordered_informations["price_including_tax"] = informations["Price (incl. tax)"]
    reordered_informations["price_excluding_tax"] = informations["Price (excl. tax)"]
    reordered_informations["number_available"] = informations["number_available"]
    reordered_informations["product_description"] = informations["description"]
    reordered_informations["category"] = informations["category"]
    reordered_informations["review_rating"] = informations["review_rating"]
    reordered_informations["image_url"] = informations["image_url"]


    print(reordered_informations.keys())
    return reordered_informations

#Mettre les données dans un csv
def fill_csv(book_infos_list, category):

    if not os.path.exists("extracts"):
        os.makedirs("extracts")  # Create directory if it does not exist
    field_names = list(book_infos_list[0].keys())

    with open(f"extracts/{category}.csv", "w") as csv_file: 
        writer = csv.DictWriter(csv_file, fieldnames = field_names, extrasaction='ignore') 
        writer.writeheader() 
        writer.writerows(book_infos_list) 

def download_image(url,directory):
    if not os.path.exists(directory):
        os.makedirs(directory)  # # Create directory if it does not exist
    file_name = os.path.basename(url)  # Extract the file name from the URL
    save_path = os.path.join(directory, file_name)
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

if __name__=="__main__":
    main()