from unittest import IsolatedAsyncioTestCase
from storage.redis import Cache


class TestCache(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.cache = Cache()
        await self.cache.connect()

    async def asyncTearDown(self):
        await self.cache.disconnect()

    async def test_mark_visited(self):
        url = 'https://www.example.com'
        await self.cache.mark_visited(url)
        result = await self.cache.is_visited(url)
        self.assertEqual(str(result,'utf-8'), "1")

    async def test_is_visited(self):
        url = 'https://www.example.com'
        await self.cache.mark_visited(url)
        result = await self.cache.is_visited(url)
        self.assertEqual(str(result,'utf-8'), "1")
        result = await self.cache.is_visited('https://www.example2.com')
        self.assertIsNone(result)
