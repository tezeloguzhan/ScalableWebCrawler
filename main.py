import asyncio
from crawlers.crawler import start_crawl
from parser.link_parser import Parser
from storage.redis import Cache
from utils.logger import create_logger
from network.client import HttpClient
from config import CRAWLER_URL


async def main():
    crawler_url = CRAWLER_URL
    http_client = HttpClient()
    parser = Parser()
    cache = Cache()
    await cache.connect()
    logger = create_logger('crawler', 'logs')
    await start_crawl(crawler_url, http_client, parser, cache, logger)
    await cache.disconnect()


if __name__ == '__main__':
    asyncio.run(main())
