# Book Web Scraper 📚

A command-line web scraper that collects book titles and prices from books.toscrape.com and saves them to a CSV file.

## Features
- Scrapes all 50 pages of books.toscrape.com
- Collects book title and price for each book
- Saves data to a CSV file automatically
- Handles connection errors gracefully

## How to Use
Run the script:

python web_scraper.py

The script runs automatically with no prompts. When finished it will print:

Scraped 1000 books and saved to book.csv

## Output
A file called book.csv will be created in the same folder with the following columns:

Title, Price
A Light in the Attic, £51.77
Tipping the Velvet, £53.74
...

## Requirements
- Python 3.x
- requests
- beautifulsoup4

## Installation
pip install requests beautifulsoup4

## Data Source
http://books.toscrape.com
