class UrlNode(object):
    def __init__(self, parent_id, current_id, url):
        self.parent_id = parent_id
        self.id = current_id
        self.url = url

    def __eq__(self, other):
        return self.url == other.url


class DataNode(object):
    def __init__(self, url_node, current_data):
        self.url_node = url_node
        self.current_data = current_data
