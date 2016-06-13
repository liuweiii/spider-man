# -*- coding: utf-8 -*-
class OutputManager(object):
    def __init__(self):
        self.nodes = []

    def add(self, node):
        self.nodes.append(node)

    def output(self):
        return self.nodes

    def points_and_edges(self):
        points = []
        edges = []
        for node in self.nodes:
            label = str(node.current_data[0].string.encode("utf-8"))
            points.append({"id": node.url_node.id, "label": label})
            edges.append({"from": node.url_node.parent_id, "to": node.url_node.id})
        return points, edges
