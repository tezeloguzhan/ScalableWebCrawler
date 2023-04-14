from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from config import CRAWLER_URL
from typing import List

parsed_url = urlparse(CRAWLER_URL)
base_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"


class Parser:
    @staticmethod
    def get_links(html)-> List[str]:
        soup = BeautifulSoup(html, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a', href=True)]
        links = [urljoin(base_url, link) for link in links if link.startswith('/')]
        return links
