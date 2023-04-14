# ScalableWebCrawler

# File Structure : 
<pre>
crawler/
    crawler.py --> Crawler class and process

network/
    client.py --> Client for making HTTP requests

parser/
    link_parser.py --> Link parser for extracting links from HTML

storage/
    redis.py --> Redis client for revisiting URL 

utils/
    logger.py --> Logger configiration and logger class

tests/
    unit.py --> Will be added soon
    integration.py --> Will be added soon

main.py --> Main file to run the crawler
config.py --> Redis configuration , Crawling configuration, Network configuration
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

# TO-DO :
<pre>

1-Exceptions will be handled .
2-Logging system will be improved.
3-Unit tests will be added.
4-Integration tests will be added.

</pre>



