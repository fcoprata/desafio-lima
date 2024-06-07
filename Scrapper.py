import requests
from bs4 import BeautifulSoup


class Scrapper:
    """
    A class that scrapes data from a BBC news article.

    Attributes:
        None

    Methods:
        bbc_scrapper(url): Scrapes data from the given URL and returns a list of dictionaries containing the scraped data.
    """

    def bbc_scrapper(self, url):
        """
        Scrapes data from the given URL and returns a list of dictionaries containing the scraped data.

        Args:
            url (str): The URL of the BBC news article to scrape.

        Returns:
            list: A list of dictionaries containing the scraped data. Each dictionary represents a single article and contains the following keys:
                - 'Title': The title of the article.
                - 'Body': The body text of the article.
                - 'Fonte': The source of the article.
                - 'Author': The author of the article.
                - 'URL': The URL of the article.
        """
        data = []
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        title = soup.find(id="content").text
        fonte = soup.find('span', class_='bbc-1y5sx98').text
        author = soup.find('span', class_='bbc-1ypcc2').text
        text = self.extract_body(soup)
        keyword = self.extract_key_words(soup)
        x = {
            'Title': title,
            'Body': text,
            'Fonte': fonte,
            'Author': author,
            'URL': url,
            'Keywords': keyword
        }
        data.append(x)
        return data

    def extract_key_words(self, soup):
        """
        Extracts key words from the given BeautifulSoup object.

        Args:
            soup (BeautifulSoup): The BeautifulSoup object representing the HTML content.

        Returns:
            list: A list of key words extracted from the HTML content.
        """
        keyword = []
        divs = soup.find_all('li', class_='bbc-1uuxkzb e2o6ii40')
        for div in divs:
            links = div.find_all('a')
            for link in links:
                keyword.append(link.text)
        return keyword

    def extract_body(self, soup):
        """
        Extracts the body text from the given BeautifulSoup object.

        Args:
            soup (BeautifulSoup): The BeautifulSoup object representing the HTML page.

        Returns:
            str: The extracted body text.
        """
        divs = soup.find_all('div', class_='bbc-19j92fr ebmt73l0')
        text = ''
        for div in divs:
            paragraphs = div.find_all('p')
            for paragraph in paragraphs:
                text += paragraph.text + '\n'
        return text
