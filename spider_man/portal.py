# -*- coding: utf-8 -*- 
from flask import Flask, render_template
from spider_man import SpiderMan
from spider_man.download_manager import DownloadManager
import thread

app = Flask(__name__)

sm = SpiderMan("http://baike.baidu.com","http://baike.baidu.com/view/1458275.htm")


@app.route("/crawl")
def crawl():
    points, edges = sm.get_points_and_edges()
    return render_template("network.html", points=points, edges=edges)


@app.route("/start")
def start():
    print "starting SpiderMan ..."
    thread.start_new_thread(sm.start_push, ())

    thread.start_new_thread(sm.start_pull, ())

    print "starting DownloadManager ..."
    thread.start_new_thread(DownloadManager.start_work, (r"/view/\d+\.htm",
                   ".main-content dl dd h1"))
    return "started ..."
    #
