import requests
from bs4 import BeautifulSoup

# Adding the url we want to scrape from
url = "https://books.toscrape.com/"

# Sending a GET request and saving it as response object
response = requests.get(url)

# Creating an instance of BeautifulSoup with parsed HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Finding all <div> elements that have class_name 'article'
books = soup.find_all("article")

#iterating each article to get the desired elements from them
for book in books:

    # Get the title from the website and print it
    title = book.h3.a["title"]
    print(f"Title:{title}")

    # Get rating of the book and print it
    rating = book.p["class"][1]
    print(f"Rating:{rating}")

    # Get price of the book and print it
    price = book.select_one(".price_color").get_text()
    print(f"Price:{price}")
    print("*******************")
