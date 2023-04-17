# ScalableWebCrawler

# File Structure : 
<pre>
crawlers/
    crawler.py --> Crawler class and process

logs/
    crawler.log --> Log file includes exceptions , crawled and skipped situations of Urls

network/
    client.py --> Client for making HTTP requests

parser/
    link_parser.py --> Link parser for extracting links from HTML

storage/
    redis.py --> Redis client for revisiting URL 

utils/
    logger.py --> Logger configiration and logger class

tests/
    unit.py --> Includes Cache and Parser unit tests and work with both
    integration.py --> Integration tests general

main.py --> Main file to run the crawler
config.py --> Redis configuration , Crawling configuration, Network configuration
requirements.txt --> Requirements for the project
</pre>

# Installation :
<pre>
First of all : 

1. Install Redis : https://redis.io/topics/quickstart if you don't have it.

then :

1. Clone the repository : git clone
2. Install the requirements : pip install -r requirements.txt
3. Run the main file : python main.py
4. If you want to change the configuration, you can change it in config.py
5. Enjoy :)
</pre>






