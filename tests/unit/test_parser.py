from parser.link_parser import Parser
from unittest import TestCase
from config import CRAWLER_URL
class TestParser(TestCase):
    def test_get_links(self):
        parser = Parser()
        html = '''
        <html>
            <head>
                <title>Example</title>
            </head>
            <body>
                <a href="https://www.trendyol.com/page1">Page 1</a>
                <a href="https://www.trendyol.com/page2">Page 2</a>
            </body>
        </html>
        '''

        expected_links = ['https://www.trendyol.com/page1', 'https://www.trendyol.com/page2']
        assert parser.get_links(html) == expected_links
