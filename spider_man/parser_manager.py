import re
from bs4 import BeautifulSoup


class ParserManager(object):

    @staticmethod
    def parse(content, url_keys, context_keys):
        soup = BeautifulSoup(content, "html.parser", from_encoding="utf-8")
        links = soup.find_all("a", href=re.compile(url_keys))
        data = soup.select(context_keys)
        return links, data
