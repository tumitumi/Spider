#-*-coding:utf-8-*-
__author__ = 'lixin'
import urllib2
import time

class Spider:
    def __init__(self):
        self.page_num = 1
        self.total_num = 0
        self.header = { 'Host' : 'verycd.gdajie.com',
                        'Referer' : 'http://verycd.gdajie.com/music/page',
                        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
        self.data = None

    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

    def getCurrentDate(self):
        return time.strftime('%Y-%m-%d',time.localtime(time.time()))

    def getPage(self, url):
        try:
            request = urllib2.Request(url, headers= self.header)
            response = urllib2.urlopen(request)
            time.sleep(2)
            return response
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print "Something Error!Reason:", e.code, e.reason
                time.sleep(2)
                return None
