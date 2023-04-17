import asyncio
from utils.logger import gather_with_concurrency, run_tasks

async def crawl(url, http_client, parser, cache, logger):
    """
    Crawl a URL and return linked URLs
    """
    try:

        html = await http_client.fetch(url,logger)
        if not html:
            logger.error(f'Failed to fetch --> {url}')
            return []
        links = parser.get_links(html,logger)
        visited = await cache.is_visited(url)
        if visited:
            logger.debug(f'Skipping {url} is already MARKED')
            return []
        logger.debug(f'Crawled {url}')
        await cache.mark_visited(url)
        return links
    except Exception as e:
        logger.exception( f'Crawl Func Exception in --> {url}--> {e}')


async def start_crawl(crawler_url, http_client, parser, cache, logger):
    """
    Crawl the CRAWLER URL to all linked URLs
    """

    try:

        tasks = []
        links = await crawl(crawler_url, http_client, parser, cache, logger)
        if links==[]:
            pass
        links=list(set(links))
        for link in links:
            tasks.append(asyncio.create_task(crawl(link, http_client, parser, cache, logger)))
        await run_tasks(tasks, logger)

        linked_urls = [link for task in tasks for link in task.result()]
        if linked_urls:
            linked_urls = list(set(linked_urls))
            await start_crawl(linked_urls[0], http_client, parser, cache, logger)
            if len(linked_urls) > 1:
                coroutines = [start_crawl(link, http_client, parser, cache, logger) for link in linked_urls[1:]]
                await gather_with_concurrency(coroutines)
    except Exception as e:
        logger.exception( f'Start Crawl Func Exception in --> {e}')

