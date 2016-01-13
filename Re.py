#-*-coding:utf-8-*-
__author__ = 'lixin'
import re
import Spider
import time

class Re:
    def __init__(self, url):
        self.Spider = Spider.Spider()
        self.url = url
        self.Filename = "./Page.htm"

    def sortPage(self):
        fp = open(self.Filename, 'w')
        self.FileInit(fp)
        page = self.Spider.getPage(self.url)
        # temp = page.read().decode("utf-8",'ignore').encode("gbk",'ignore')
        temp = page.read()
        pattern1 = re.compile('<div class="list_info">(.*?)</div>', re.S)
        pattern2 = re.compile('<a href=(.*?) title=',re.S)
        pattern3 = re.compile('<table id="emuleFile"><tbody>.*?<font color.*?">(.*?)</font>',re.S)
        pattern4 = re.compile('<div class="description">(.*?)</div>',re.S)
        pattern5 = re.compile('<div id="detail" style="display: block;">.*?href=(.*?)>',re.S)
        pattern6 = re.compile('href=(.*?)>',re.S)
        uwResult = re.findall(pattern1, temp)
        count = 0
        while count < 20:
            result1 = uwResult[count]
            url1 = re.search(pattern2,result1).group(1).strip('"')
            temp_page1 = self.Spider.getPage(url1).read()
            # result2 is a title including url
            result2 = re.search(pattern3,temp_page1).group(1)
            # result3 is a description
            result3 = re.search(pattern4,temp_page1).group(1)
            # url2 is a url included in result2
            url2 = re.search(pattern6,result2).group(1).strip('"')
            temp_page2 = self.Spider.getPage(url2).read()
            # url3 is the download url
            url3 = re.search(pattern5,temp_page2).group(1).strip('"')
            added = 'href="'+url3+'">'
            # result4 is the final title including download url
            result4 = re.sub(pattern6,added,result2)
            print (result4+'\n'+result3).decode("utf-8",'ignore').encode("gbk",'ignore')
            fp.write(result4+'\n'+result3)
            fp.write('\r\n<p>------------------------------------------------------------------------------</p>\r\n')
            count+=1
            time.sleep(1)
        # fp.write(result1.group(1).strip())
        self.FileEnd(fp)
        fp.close()

    def FileInit(self,file):
        file.write('<html>\r\n <head>\r\n  <meta http-equiv="Content Type" content="text/html"; charset="utf-8"/>\r\n </head>\r\n')
        file.write(' <body>\r\n')

    def FileEnd(self,file):
        file.write(' <body>\r\n')