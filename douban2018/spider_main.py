#!/usr/bin/python
# -*- coding: UTF-8 -*-
import douban2018.html_parser
import douban2018.html_outputer
import douban2018.html_downloader


class SpiderMain(object):

    def __init__(self):
        self.parser = douban2018.html_parser.HtmlParser()
        self.outputer = douban2018.html_outputer.HtmlOutputer()
        self.downloader = douban2018.html_downloader.HtmlDownloader()

    def craw(self, url):
        html_cnt = self.downloader.downlod(url)
        movie_data = self.parser.parser_html(html_cnt)
        self.outputer.collect_data(movie_data)


if __name__ == '__main__':
    url = 'https://movie.douban.com/tag/2018?start=100&type=T'
    spider = SpiderMain()
    spider.craw(url)
