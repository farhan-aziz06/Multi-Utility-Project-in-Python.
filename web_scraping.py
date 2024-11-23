import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self):
        pass

    def get_website_content(self, url):
        """Fetches the content of the webpage."""
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page: {e}")
            return None

    def parse_html(self, html_content):
        """Parses the HTML content using BeautifulSoup."""
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup

    def scrape_headlines(self, soup):
        """Scrapes news headlines or titles from the page."""
        headlines = []
        for headline in soup.find_all('h2'):  # Assuming headlines are in <h2> tags
            headlines.append(headline.text.strip())
        return headlines

    def display_headlines(self, headlines):
        """Displays the scraped headlines."""
        print("\nScraped Headlines:")
        for idx, headline in enumerate(headlines, 1):
            print(f"{idx}. {headline}")

    def scrape_website(self, url):
        """Main method to scrape a website."""
        html_content = self.get_website_content(url)
        if html_content:
            soup = self.parse_html(html_content)
            headlines = self.scrape_headlines(soup)
            self.display_headlines(headlines)

# Main method
def main():
    print("Welcome to the Web Scraping Module!")
    url = input("Enter the URL of the website you want to scrape: ")
    scraper = WebScraper()  # Create an instance of the WebScraper class
    scraper.scrape_website(url)  # Call scrape_website with the URL argument

if __name__ == "__main__":
    main()
