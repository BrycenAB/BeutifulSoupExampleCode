import requests
from bs4 import BeautifulSoup
import csv


def scrape_books_titles(url):
    # Send an HTTP GET request to the specified URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the elements containing the books
        books = soup.find_all('article', class_='product_pod')

        # Prepare a list to store the book titles and prices
        data = []

        # Process and add the book titles and prices to the data list
        for book in books:
            title = book.h3.a['title']
            price = book.select_one('.price_color').text
            # replace letters in price
            price = price.replace('Â£', '')
            rating = book.select_one('.star-rating')['class'][1]
            stock = book.select_one('.instock.availability').text.strip()
            data.append([title, price, rating, stock])

        return data

    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None

def main():
    url = "http://books.toscrape.com/"
    all_data = []

    # Scrape the first page and add data to the list
    data = scrape_books_titles(url)
    if data:
        all_data.extend(data)

    # Scrape all pages for all books
    for i in range(2, 51):
        url = f"https://books.toscrape.com/catalogue/page-{i}.html"
        data = scrape_books_titles(url)
        if data:
            all_data.extend(data)

    # Write the data to a CSV file
    with open("Books.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["Title", "Price", "Rating", "Stock"])
        # Write the book data
        writer.writerows(all_data)


if __name__ == "__main__":
    main()

