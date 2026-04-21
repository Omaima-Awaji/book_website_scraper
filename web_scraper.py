import csv
import requests
from bs4 import BeautifulSoup


def scrape_books():
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    total_books = 0

    with open("book.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price"])

        for page in range(1,51):
            url = base_url.format(page)
            try:

                web_response = requests.get(url)
                web_response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Error connecting to website: {e}")
                continue
            soup = BeautifulSoup(web_response.content, "html.parser")
            books = soup.find_all("article", class_="product_pod")

            for book in books:
                title = book.find("img")["alt"]
                price = book.find("p", class_="price_color").text
                writer.writerow([title, price])
                total_books += 1
    print(f"Scraped {total_books} books and saved to book.csv")

if __name__ == "__main__":
    scrape_books()