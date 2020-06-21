from bs4 import BeautifulSoup
import re
import urllib
import xlwt  # 导出excel
import sqlite3


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1、爬取网页
    datalist = getData(baseurl)
    savepath = ".\\test.xls"
    # 2、解析数据
    # 3、保存数据
    saveData(savepath)
    print("开始爬虫")


# 爬取网页
def getData(baseurl):
    datalist = []
    return datalist


def saveData():
    print("savedata")


if __name__ == "__main__":
    # 程序执行时调用函数
    main()
