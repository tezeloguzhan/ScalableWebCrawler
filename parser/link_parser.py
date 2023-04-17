from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from config import CRAWLER_URL
from typing import List
import re

parsed_url = urlparse(CRAWLER_URL)
base_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"


class Parser:
    @staticmethod
    def get_links(html,logger) -> List[str]:
        try:
            soup = BeautifulSoup(html, 'html.parser')
            links = [link.get('href') for link in soup.find_all('a', href=True)]
            links = [link for link in links if re.match(r'^{}?://'.format(parsed_url.scheme), link)]
            return links

        except Exception as e:
            logger.exception( f'Get Links Func Exception in --> {e}')
