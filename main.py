#-*-coding:utf-8-*-
__author__ = 'lixin'
import Spider
import Re


def main():
    url = "http://verycd.gdajie.com/music/page1"
    testRe = Re.Re(url)
    testRe.sortPage()

if __name__ == "__main__":
    main()