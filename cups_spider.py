#!/usr/bin/python
# _*_coding:utf-8 _*_
import csv
import json
from codecs import open
from pprint import pprint
import requests


class Cups():
    def __init__(self, url, page, path):
        self._url = url
        self._page = page
        self._path = path
        self._result = set()

    def run(self):
        """ 启动爬虫 """
        headers = {'X-Requested-With': 'XMLHttpRequest',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/56.0.2924.87 Safari/537.36'}
        urls = []
        urls.extend([self._url.format(1, p, 0) for p in range(1, self._page)])
        urls.extend([self._url.format(1, p, 1) for p in range(1, self._page)])
        urls.extend([self._url.format(3, p, 0) for p in range(1, self._page)])
        urls.extend([self._url.format(3, p, 1) for p in range(1, self._page)])
        for i, u in enumerate(urls):
            try:
                j = json.loads(requests.get(u, headers=headers, timeout=2).text[15:])
                for i, v in enumerate(j['rateList']):
                    goods = (v['rateDate'], v['auctionSku'],
                             v['rateContent'].replace("<b>", "").replace("</b>", "").replace("&hellip", ""))
                    self._result.add(goods)
                    print(i)
            except Exception as e:
                print(e)
        pprint(self._result)
        print(len(self._result))
        self.save()

    def save(self):
        """ 保存数据到本地 """
        with open(self._path, "w+") as f:
            f_csv = csv.writer(f)
            f_csv.writerows(self._result)

    def clear(self):
        """ 数据去重 """
        s = set()
        with open(self._path, "r") as f:
            fin_csv = csv.reader(f)
            for row in fin_csv:
                if len(row) == 0:
                    continue
                s.add(tuple(row))
        with open("data/cup_all.csv", "w+") as f:
            fout_csv = csv.writer(f)
            fout_csv.writerows(s)
        print(len(s))

    @staticmethod
    def extract():
        """ 提取数据 """
        datelst, size_colorlst, commentlst = [], [], []
        with open("data/cup_all.csv", "r") as f:
            fin_csv = csv.reader(f)
            i = 0
            for row in fin_csv:
                if len(row) == 0:
                    continue
                i += 1
                datelst.append(row[0])
                size_colorlst.append(row[1])
                commentlst.append(row[2])
                # print('去除重复后共有%d条数据' % i)

        with open("data/comment.txt", "w+", encoding="utf-8") as f:
            for r in commentlst:
                f.write(r + "\r")

        with open("data/size_color.txt", "w+", encoding="utf-8") as fin:
            for r in size_colorlst:
                # print(r)
                fin.write(r + "\r")
        with open("data/size_color.txt", "r", encoding="utf-8") as fin:
            rows = fin.readlines()
            size_lst = []
            corlor_lst = []
            for row in rows:
                corlor_lst.append((row.split(";")[0]))
                size_lst.append((row.split(";")[1]))
            with open("data/size.txt", "w+", encoding="utf-8") as f_size:
                f_size.writelines(size_lst)
            with open("data/corlor.txt", "w+", encoding="utf-8") as f_corlor:
                for corlor in corlor_lst:
                    f_corlor.writelines(corlor + '\r')


if __name__ == "__main__":
    url = "https://rate.tmall.com/list_detail_rate.htm?itemId=37457670144&spuId=249827344&" \
          "sellerId=470355944&order={}&currentPage={}&append=0&content={}"
    cups = Cups(url, 101, "data\cups.csv")
    cups.run()
    cups.clear()
    cups.extract()
