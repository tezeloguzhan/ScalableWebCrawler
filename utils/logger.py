import logging
from logging.handlers import RotatingFileHandler
import os
import asyncio
from config import MAX_CONCURRENT_REQUESTS


def create_logger(name, log_dir):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(os.path.join(log_dir, f'{name}.log'), maxBytes=10*1024*1024, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


async def gather_with_concurrency(coros, limit=MAX_CONCURRENT_REQUESTS):

    sem = asyncio.Semaphore(limit)

    async def sem_wrapper(coro):
        async with sem:
            return await coro
    tasks = [sem_wrapper(coro) for coro in coros]
    return await asyncio.gather(*tasks)


async def run_tasks(tasks, logger):

    try:
        await asyncio.gather(*tasks)
    except Exception as e:
        logger.exception(e)