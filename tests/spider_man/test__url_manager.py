import unittest2
from bs4 import Tag
from spider_man.url_manager import UrlManager


class TestUrlManager(unittest2.TestCase):
    def test__has_url_if_has(self):
        um = UrlManager("111", "xxx")
        self.assertTrue(um.has_url_node())

    def test__has_url_if_not_has(self):
        um = UrlManager("111", "xxx")
        um.get_url_node()
        self.assertFalse(um.has_url_node())

    def test__get_url_if_has(self):
        um = UrlManager("111", "xxx")
        url = um.get_url_node()
        self.assertEqual("111", url.url)

    def test__add_urls_if_give_2(self):
        um = UrlManager("111", "xxx")
        um.add_urls(1, (Tag(name="a",attrs={'href':'222'}),
                        Tag(name="a", attrs={'href':'333'})))
        self.assertEqual(um.get_url_node().url, "111")
        self.assertEqual(um.get_url_node().url, "xxx222")
        self.assertEqual(um.get_url_node().url, "xxx333")
