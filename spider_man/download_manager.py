import urllib2


class DownloadManager(object):
    def download(self, url):
        try:
            response = urllib2.urlopen(url)
            if response.getcode() is 200:
                return response.read()
        except Exception as e:
            print e
        raise Exception("response failed. code["+response.getcode()+"]")
