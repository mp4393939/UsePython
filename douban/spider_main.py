#!/usr/bin/python
# -*- coding: UTF-8 -*-
import douban.html_parser
import douban.html_outputer
import douban.html_downloader


class SpiderMain(object):

    def __init__(self):
        self.parser = douban.html_parser.HtmlParser()
        self.outputer = douban.html_outputer.HtmlOutputer()
        self.downloader = douban.html_downloader.HtmlDownloader()

    def craw(self, url):
        html_cnt = self.downloader.downlod(url)
        movie_data = self.parser.parser_html(html_cnt)
        self.outputer.collect_data(movie_data)


if __name__ == '__main__':
    url = 'https://movie.douban.com/tag/2018?start=100&type=T'
    spider = SpiderMain()
    spider.craw(url)
