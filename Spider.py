#-*-coding:utf-8-*-
__author__ = 'lixin'
import urllib2
import time
import re

class Spider:
    def __init__(self):
        self.page_num = 1
        self.total_num = 0
        self.page_spider = page.Page()

    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

    def getCurrentDate(self):
        return time.strftime('%Y-%m-%d',time.localtime(time.time()))

    def getPage(self, url):
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode("utf-8")
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print "Something Error!Reason:",e.reason
                return None
