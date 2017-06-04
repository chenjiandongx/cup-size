import csv
import json
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
        with open(self._path, "w+", encoding="utf-8") as f:
            f_csv = csv.writer(f)
            f_csv.writerows(self._result)

    def clear(self):
        """ 数据去重 """
        s = set()
        with open(self._path, "r", encoding="utf-8") as f:
            fin_csv = csv.reader(f)
            for row in fin_csv:
                s.add(tuple(row))
        with open("cup_all.csv", "w+", encoding="utf-8") as f:
            fout_csv = csv.writer(f)
            fout_csv.writerows(s)
        print(len(s))

    @staticmethod
    def extract():
        """ 提取数据 """
        # datelst, size_colorlst, commentlst = [], [], []
        # with open("cup_all.csv", "r", encoding="utf-8") as f:
        #     fin_csv = csv.reader(f)
        #     for row in fin_csv:
        #         date, size_color, comment = row
        #         # datelst.append((date))
        #         # size_colorlst.append((size_color))
        #         commentlst.append((comment))
        # with open("comment.txt", "w+", encoding="utf-8") as f:
        #     for r in commentlst:
        #         f.write(r + "\n")
        with open(r"data_/size_color.txt", "r", encoding="utf-8") as fin:
            rows = fin.readlines()
            lst = []
            for row in rows:
                lst.append((row.split(";")[1]))
        with open(r"data_/size.txt", "w+", encoding="utf-8") as fout:
            fout.writelines(lst)

if __name__ == "__main__":

    url = "https://rate.tmall.com/list_detail_rate.htm?itemId=37457670144&spuId=249827344&" \
          "sellerId=470355944&order={}&currentPage={}&append=0&content={}"
    cups = Cups(url, 101, "cups.csv")
    # cups.run()
    # cups.clear()
    cups.extract()