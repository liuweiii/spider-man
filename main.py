# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from spider_man.portal import app


if __name__ == '__main__':
    app.run("0.0.0.0", port=15673, debug=True)
