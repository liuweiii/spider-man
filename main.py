# -*- coding: utf-8 -*-
from spider_man.portal import app
import sys
reload(sys)
sys.setrecursionlimit(1000000)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    app.run("0.0.0.0", port=15673, debug=True, threaded=False)
