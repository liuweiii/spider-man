import unittest2
from spider_man.download_manager import DownloadManager


class TestDownloadManager(unittest2.TestCase):
    def test__download_baidu_baike(self):
        dm = DownloadManager()
        content = dm.download("http://baike.baidu.com/view/1458275.htm")
        print content
        self.assertNotEqual(content.find("Dynamic Programming Language"), -1)
