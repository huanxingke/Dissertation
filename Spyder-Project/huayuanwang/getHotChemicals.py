import json
import time
import os

from lxml import etree

from fake_request import fakeRequests
from spyder import getDetails


headers = {
    "Host": "www.chemsrc.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}


if not os.path.exists("msdsjson"):
    os.mkdir("msdsjson")
if not os.path.exists("structpic"):
    os.mkdir("structpic")
if not os.path.exists("error"):
    os.mkdir("error")


def getHotHref():
    href_list = []
    for i in range(1, 31):
        url = "https://www.chemsrc.com/HotList.jsp"
        params = {
            "page": i
        }
        html = fakeRequests(url=url, params=params, headers=headers).text
        tree = etree.HTML(html)
        hrefs = tree.xpath("//div[@class='widget-box']/ul/li/a/@href")
        for href in hrefs:
            href = "https://www.chemsrc.com" + href
            if href not in href_list:
                print(href)
                href_list.append(href)
    with open("hot.json", "w", encoding="utf-8") as fp:
        json.dump(href_list, fp)


def getHotDetails():
    with open("hot.json", "r", encoding="utf-8") as fp:
        hot_hrefs = json.load(fp)
    for hot_href_index, hot_href in enumerate(hot_hrefs):
        details = getDetails(chemical_href=hot_href)
        if details:
            chemical = details["name_information"]["details"]["Chinese_name"]["details"]
            structural_formula_pic = details["name_information"]["details"]["structural_formula_pic"]["details"]
            cas_number = details["name_information"]["details"]["cas_number"]["details"]
            if cas_number:
                with open("msdsjson/%s.json" % cas_number, "w", encoding="utf-8") as fp:
                    json.dump(details, fp)
                pic_data = fakeRequests(url=structural_formula_pic, headers=headers).content
                with open("structpic/%s.png" % cas_number, "wb") as fp:
                    fp.write(pic_data)
                print("[%s/%s]%s - %s" % (hot_href_index + 1, len(hot_hrefs), chemical, cas_number))
                time.sleep(2)
            else:
                with open("error/nocas.txt", "a", encoding="utf-8") as fp:
                    fp.write(hot_href + "\n")
        else:
            with open("error/nomsds.txt", "a", encoding="utf-8") as fp:
                fp.write(hot_href + "\n")


if __name__ == '__main__':
    getHotDetails()