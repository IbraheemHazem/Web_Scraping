# import requests
# from bs4 import BeautifulSoup

# url = "https://books.toscrape.com/"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")

# for book in soup.find_all("article"):
#     title = book.h3.a["title"]
#     rating = book.select_one("p[class^='star-rating']")["class"][1]
#     price = book.select_one(".price_color").get_text()
    
#     print(f"Title: {title}\nRating: {rating}\nPrice: {price}\n{'*' * 20}")






# #another refactoring but with verifying that it's acceptable to scrape from this website and adding comments
# import requests
# from bs4 import BeautifulSoup

# # Define the URL of the website to scrape
# url = "https://www.amazon.eg/-/en/"

# # Send an HTTP GET request to the website
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.content, "html.parser")

#     # Extract information from the parsed HTML
#     for article in soup.find_all("article"):
#         # Extract the title of the book
#         title = article.h3.a["title"]

#         # Find the class of the star rating
#         star_rating_class = article.select_one("p[class^='star-rating']")["class"][1]

#         # Find the price of the book
#         price_element = article.select_one(".price_color")
#         price = price_element.get_text() if price_element else "Price not available"

#         # Display book details
#         print(f"Title: {title}\nStar Rating: {star_rating_class}\nPrice: {price}\n{'*' * 20}")
# else:
#     # Display an error message if the request was not successful
#     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")





