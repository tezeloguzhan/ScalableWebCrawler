import asyncio
import aiohttp
from config import REQUEST_TIMEOUT, MAX_RETRIES
class HttpClient:
    def __init__(self, user_agent=None, headers=None):
        self.user_agent = user_agent or 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
        self.headers = headers or {}

    async def fetch(self, url):
        retry_count = 0
        while retry_count < MAX_RETRIES:
            try:
                async with aiohttp.ClientSession(headers=self.headers) as session:
                    async with session.get(url, timeout=REQUEST_TIMEOUT, verify_ssl=False,
                                           headers={'User-Agent': self.user_agent}) as response:
                        return await response.text()
            except Exception as e:
                print(e)
                retry_count += 1
        return None
