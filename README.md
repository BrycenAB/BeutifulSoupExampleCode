# Web Scraping with BeautifulSoup - books.toscrape.com

## Description

This is a simple Python script that demonstrates web scraping using the BeautifulSoup library to extract data from the website https://books.toscrape.com/. The extracted data is then saved to a CSV file for further analysis or storage.

## Prerequisites

- Python 3.x
- BeautifulSoup library (`beautifulsoup4`)
- Requests library (`requests`)

You can install the required libraries using the following command:

```console
pip install beautifulsoup4 requests
```

## Usage
1. Clone the repository or download the Main.py file.

2. Navigate to the project directory.

3. Run the script using Python:

```console
python Main.py
```

4. The script will start scraping the website https://books.toscrape.com/ and extract the book data.

5. The extracted data will be saved to a file named books_data.csv in the same directory.

## Output 
The script will create a CSV file named Books.csv, which will contain the following information for each book:
* Title
* Price
* Stock
* Rating

## Note
This script is provided for educational purposes only and is meant to demonstrate basic web scraping techniques. Before scraping any website, please review the website's Terms of Service and Robots.txt file to ensure you are not violating any rules or policies.
