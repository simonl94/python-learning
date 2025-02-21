# Imports
import requests
import config
from bs4 import BeautifulSoup

# Get URL from config file
url = config.WEBSITE_URL

# Send GET request
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract H3 elements
books = soup.find_all("h3")

# Extract and print book titles from the H3 element variable
book_titles = [book.a.attrs["title"] for book in books]
for title in book_titles:
    print(title)
