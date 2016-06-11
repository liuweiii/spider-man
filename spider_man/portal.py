# -*- coding: utf-8 -*- 
from flask import Flask, render_template
from spider_man import SpiderMan

app = Flask(__name__)


@app.route("/crawl/<total>")
def crawl(total):
    sm = SpiderMan("http://baike.baidu.com/view/1458275.htm",
                   "http://baike.baidu.com", r"/view/\d+\.htm",
                   ".main-content dl dd h1")
    points, edges = sm.crawl(int(total))
    return render_template("network.html", points=points, edges=edges)
