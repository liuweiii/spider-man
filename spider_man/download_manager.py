import threadpool
import zmq
import urllib2
from spider_man.parser_manager import ParserManager

THREAD_COUNT = 10


class DownloadManager(object):
    @staticmethod
    def download(data):
        url_node, url_keys, context_keys = data["url_node"], data["url_keys"], data["context_keys"]
        try:
            context = zmq.Context()
            sender_url = context.socket(zmq.PUSH)
            sender_url.bind("tcp://*:15678")

            response = urllib2.urlopen(url_node.url)
            if response.getcode() is 200:
                s = response.read()
                links, data = ParserManager.parse(s, url_keys, context_keys)
                sender_url.send_pyobj((links, data, url_node))
        except Exception as e:
            print e

    @staticmethod
    def start_work(url_keys, context_keys):
        pool = threadpool.ThreadPool(THREAD_COUNT)

        context = zmq.Context()
        receiver = context.socket(zmq.PULL)
        receiver.connect("tcp://localhost:15677")
        while True:
            url_node = receiver.recv_pyobj()
            print "[dm from sm] receive: " + str(url_node)
            requests = threadpool.makeRequests(DownloadManager.download,
                                               [{
                                                   "url_node": url_node,
                                                   "url_keys": url_keys,
                                                   "context_keys": context_keys
                                               }]
                                               )
            pool.putRequest(requests[0])
            # [pool.putRequest(request) for request in requests]
            pool.wait()
