import asyncio
from network.client import HttpClient
from storage.redis import Cache
from parser.link_parser import Parser
from utils.logger import create_logger
from crawlers.crawler import start_crawl
from config import CRAWLER_URL

async def test_crawler():
    http_client = HttpClient()
    parser = Parser()
    cache = Cache()
    await cache.connect()
    logger=create_logger('crawler_test', '../../logs')
    links = await start_crawl(CRAWLER_URL, http_client, parser, cache,logger)
    await cache.disconnect()


if __name__ == '__main__':
    asyncio.run(test_crawler())


