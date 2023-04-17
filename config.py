import os

CRAWLER_URL=os.getenv('CRAWLER_URL', 'http://example.com')
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
REDIS_DB = os.getenv('REDIS_DB', 0)

MAX_CONCURRENT_REQUESTS = 100
REQUEST_TIMEOUT = 10
MAX_RETRIES = 3