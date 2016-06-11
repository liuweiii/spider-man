import re
from bs4 import BeautifulSoup


class ParserManager(object):
    def __init__(self, url_keys, content_keys):
        self.url_keys = url_keys
        self.content_keys = content_keys

    def parse(self, content):
        soup = BeautifulSoup(content, "html.parser", from_encoding="utf-8")
        links = soup.find_all("a", href=re.compile(self.url_keys))
        data = soup.select(self.content_keys)
        return links, data
