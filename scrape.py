# python3 -m venv path/to/venv
# source path/to/venv/bin/activate

import requests  
from bs4 import BeautifulSoup
import csv


url ="http://books.toscrape.com/"

def scrape_books(url):
  response = requests.get(url)
  if response.status_code != 200:
    return
  
  #set encoding explicitly to handle special characters c
  response.encoding = response.apparent_encoding

  print(response.text)
  soup = BeautifulSoup(response.text, "html.parser")
  books = soup.find_all("article", class_="product_pod")
  all_books = []
  for book in books:
    title = book.h3.a["title"]
    
    price_text = book.find("p", class_="price_color").text
    currency = price_text[0]
    price = float(price_text[1:])
    book = {
     "title" :title,
     "currency" :currency,
     "price" : price,
    }

    all_books.append(book)
  return(all_books)


all_books = scrape_books(url)

   










with open('books.json', 'w', encoding='utf-8') as f:
  import json

  json.dump(all_books, f, indent = 2,ensure_ascii=False)
# 🔹 save to CSV
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["title", "currency", "price"]
    )
    writer.writeheader()
    writer.writerows(all_books)


 

