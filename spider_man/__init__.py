# -*- coding: utf-8 -*-

import zmq, time
from url_manager import UrlManager
from download_manager import DownloadManager
from parser_manager import ParserManager
from output_manager import OutputManager
from spider_man.node import DataNode, UrlNode


class SpiderMan(object):
    def __init__(self, prefix,root_url):
        self.url_manager = UrlManager(root_url, prefix)
        self.output_manager = OutputManager()

    def start_push(self):
        context = zmq.Context()
        sender = context.socket(zmq.PUSH)
        sender.bind("tcp://*:15677")

        while True:
            if self.url_manager.has_url_node():
                url_node = self.url_manager.get_url_node()
                sender.send_pyobj(url_node)
            time.sleep(1)

    def start_pull(self):
        context = zmq.Context()
        receiver = context.socket(zmq.PULL)
        receiver.connect("tcp://localhost:15678")
        while True:
            s = receiver.recv_pyobj()
            new_urls, new_data, url_node = s[0], s[1], s[2]
            if len(new_data) >= 1:
                current = DataNode(url_node, new_data)
                self.output_manager.add(current)
                self.url_manager.add_urls(url_node.id, new_urls)
                print "[" + str(url_node.parent_id) + "-->" + str(url_node.id) + "]" + new_data[0].string
            else:
                print "[" + str(url_node.parent_id) + "-->" + str(url_node.id) + "]" + "--"

    def get_points_and_edges(self):
        return self.output_manager.points_and_edges()
