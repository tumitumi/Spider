#-*-coding:utf-8-*-
__author__ = 'lixin'
import re
import Spider

class Re:
    def __init__(self, url):
        self.Spider = Spider.Spider()
        self.url = url
        self.Filename = "./Page.htm"

    def sortPage(self):
        fp = open(self.Filename, 'w')
        page = self.Spider.getPage(self.url)
        temp = page.read().decode("utf-8",'ignore').encode("gbk",'ignore')
        pattern1 = re.compile('<div class="list_info">(.*?)</div>', re.S)
        result = re.search(pattern1, temp)
        fp.write(result.group(1).strip())
        fp.close()
