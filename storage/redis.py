import aioredis
from config import REDIS_HOST, REDIS_PORT, REDIS_DB


class Cache:
    def __init__(self):
        self.redis = None

    async def connect(self):
        self.redis = await aioredis.from_url(f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}')

    async def disconnect(self):
        if self.redis:
            await self.redis.close()

    async def is_visited(self, url):
        return await self.redis.get(url)

    async def mark_visited(self, url):
        await self.redis.set(url, '1')
