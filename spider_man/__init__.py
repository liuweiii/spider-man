# -*- coding: utf-8 -*-

from url_manager import UrlManager
from download_manager import DownloadManager
from parser_manager import ParserManager
from output_manager import OutputManager
from spider_man.node import DataNode, UrlNode


class SpiderMan(object):
    def __init__(self, root_url, prefix, url_keys, content_keys):
        self.url_manager = UrlManager(root_url, prefix)
        self.download_manager = DownloadManager()
        self.parser_manager = ParserManager(url_keys, content_keys)
        self.output_manager = OutputManager()

    def crawl(self, total):
        count = 0
        while self.url_manager.has_url_node() and count <= total:
            count += 1
            url_node = self.url_manager.get_url_node()
            try:
                content = self.download_manager.download(url_node.url)
            except Exception as e:
                continue
            new_urls, new_data = self.parser_manager.parse(content)
            if len(new_data) >= 1:
                current = DataNode(url_node, new_data)
                self.output_manager.add(current)
                self.url_manager.add_urls(url_node.id, new_urls)
                print "[" + str(url_node.parent_id) + "-->" + str(url_node.id) + "]" + new_data[0].string
            else:
                print "[" + str(url_node.parent_id) + "-->" + str(url_node.id) + "]" + "--"
        return self.output_manager.points_and_edges()
