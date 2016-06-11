from spider_man.node import UrlNode


class UrlManager(object):
    def __init__(self, root_url, prefix):
        self.__total_id = 1
        self.__new_urls = list()
        self.__old_urls = list()
        self.__new_urls.append(UrlNode(-1, 0, root_url))
        self.__prefix = prefix

    def has_url_node(self):
        return len(self.__new_urls) > 0

    def get_url_node(self):
        url = self.__new_urls[0]
        self.__new_urls.remove(url)
        self.__old_urls.append(url)
        return url

    def add_url_node(self, url_node):
        if url_node not in self.__new_urls and url_node not in self.__old_urls:
            self.__new_urls.append(url_node)
            return True
        return False

    def add_urls(self, parent_id, new_urls):
        for url in new_urls:
            full_url = url.attrs["href"]
            if self.__prefix not in full_url:
                full_url = self.__prefix + full_url
            url_node = UrlNode(parent_id, self.__total_id, full_url)
            if self.add_url_node(url_node):
                self.__total_id += 1
        return self.__total_id
