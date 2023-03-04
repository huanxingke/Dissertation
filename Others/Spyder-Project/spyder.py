import string
import json
import time
import os
import re

from lxml.html import tostring
from lxml import etree
import pandas as pd
import requests
import pygame

from fake_request import fakeRequests
from excel_manager import readExcel
from database import Database


def getHTMLTable():
    df = pd.DataFrame()
    for i in range(1, 190):
        url = "http://www.ichemistry.cn/weixianpin/index.asp"
        headers = {
            "Host": "www.ichemistry.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
            "Referer": "http://www.ichemistry.cn/weixianpin/"
        }
        params = {
            "Page": i
        }
        html = fakeRequests(url=url, headers=headers, params=params).text
        dataframe = pd.read_html(html, header=0)
        df = pd.concat([df, dataframe[0]])
        print(f"第{i}页采集完毕!")
        time.sleep(2)
    writer = pd.ExcelWriter("chemicals.xlsx")
    df.to_excel(writer)
    writer.save()


def excel2db():
    db = Database()
    excel_path = "chemicals.xlsx"
    dangerous_goods_number, category, secondary_category, cas_number = readExcel(excel_path, [0, 1, 2, 5])
    for i_index, i_dangerous_goods_number in enumerate(dangerous_goods_number):
        i_category = category[i_index]
        i_secondary_category = secondary_category[i_index]
        i_cas_number = str(cas_number[i_index])
        if not i_dangerous_goods_number:
            continue
        if len(i_cas_number.split("-")) == 3:
            db.insert(table="details", data=[int(i_dangerous_goods_number), i_cas_number, i_category, i_secondary_category, 0])
            print(i_cas_number)


def alterTable():
    db = Database()
    # db.add_column(table="details", column_name="chemical_id")
    # db.update(table="details", new_items=[("category", ""), ("secondary_category", "")], by_items=[])
    # add_columns = ["name", "enName", "weixianxingleibie", "xiangxingtu", "weixianxingshuoming", "lihuatexing", "zhuyaoyongtu", "ranshaoyubaozhaweixianxing", "huoxingfanying", "jinjiwu", "duxing", "zhongdubiaoxian", "zhiyejiechuxianzhi", "huanjingweihai", "jijiucuoshi", "xielouyingjichuzhi", "miehuofangfa", "ghsType", "ghsjingshici"]
    # for column_name in add_columns:
    #     db.add_column(table="details", column_name=column_name)
    db.add_column(table="details", column_name="critical_quantity")


def init404Pic(png_text, png_src):
    pygame.init()
    font = pygame.font.Font("simsun.ttc", 18)
    rtext = font.render(png_text, True, (0, 0, 0))
    pygame.image.save(rtext, png_src)


def searchByCAS(cas_number):
    url = "http://hxp.nrcc.com.cn/anxin/chem/highlist"
    params = {
        "chname": "",
        "enname": "",
        "casnum": cas_number,
        "py": "",
        "hes": "",
        "envs": "",
        "type": "0",
        "pageIndex": "0",
        "pageSize": "10"
    }
    headers = {
        "Host": "hxp.nrcc.com.cn",
        "Referer": "http://hxp.nrcc.com.cn/hc_safe_info_search.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    response = fakeRequests(url=url, params=params, headers=headers).json()
    if response.get("errCode") == 0:
        if isinstance(response.get("count"), int) and response.get("count") >= 1:
            chemical_id = response.get("data")[0].get("id")
            return chemical_id
    return None


def insertChemicalId():
    db = Database()
    data = db.select(table="details")
    for chemical_index, chemical in enumerate(data):
        cas_number = chemical["cas_number"]
        status = chemical["status"]
        if str(status) != "0":
            print(f"[{chemical_index + 1}/{len(data)}]{cas_number}-已有记录")
            continue
        chemical_id = searchByCAS(cas_number=cas_number)
        if chemical_id is not None:
            db.update(
                table="details",
                new_items=[
                    ("status", 1),
                    ("chemical_id", chemical_id)
                ],
                by_items=[("cas_number", cas_number)]
            )
            print(f"[{chemical_index + 1}/{len(data)}]{cas_number}-{chemical_id}")
        else:
            db.update(
                table="details",
                new_items=[("status", -1)],
                by_items=[("cas_number", cas_number)]
            )
            print(f"[{chemical_index + 1}/{len(data)}]{cas_number}-无结果")


def getChemCatalogList():
    url = "http://hxp.nrcc.com.cn/anxin/chemcatalog/list"
    headers = {
        "Host": "hxp.nrcc.com.cn",
        "Referer": "http://hxp.nrcc.com.cn/laws_chemicals_list.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    response = fakeRequests(url=url, headers=headers).json()
    with open("chemCatalogList.json", "w", encoding="utf-8") as fp:
        json.dump(response, fp)


def getChemicalFromCatalog():
    db = Database()
    with open("chemCatalogList.json", "r", encoding="utf-8") as fp:
        data = json.load(fp)
    for catalog in data["data"][1:]:
        print(catalog["title"])
        catalog_id = catalog["id"]
        chem_id = catalog["chemId"]
        url = "http://hxp.nrcc.com.cn/anxin/chemcatalog/detail"
        params = {
            "id": chem_id,
            "pageIndex": "0",
            "pageSize": "15",
            "type": "0",
            "content": "",
            "ids": catalog_id,
            "typesId": "false"
        }
        headers = {
            "Host": "hxp.nrcc.com.cn",
            "Referer": f"http://hxp.nrcc.com.cn/laws_chemicals_detail.html?id={chem_id}&ids={catalog_id}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
        }
        response = fakeRequests(url=url, headers=headers, params=params).json()
        count = response["count"]
        params = {
            "id": chem_id,
            "pageIndex": "0",
            "pageSize": count,
            "type": "0",
            "content": "",
            "ids": catalog_id,
            "typesId": "false"
        }
        response = fakeRequests(url=url, headers=headers, params=params).json()
        for chemical in response["data"]:
            chemical_id = chemical.get("chemId")
            cas_number = chemical.get("casNum")
            if not chemical_id or not cas_number:
                continue
            is_exist = db.select(table="details", items=[("cas_number", cas_number), ("chemical_id", chemical_id)])
            if not is_exist:
                getStructPic(cas_number=cas_number)
                db.insert(
                    table="details",
                    data=["", cas_number, "", "", 1, chemical_id]
                )
                print(f"新建: {cas_number}-{chemical_id}")
            else:
                print(f"已存在: {cas_number}-{chemical_id}")


def formatDatabase():
    db = Database()
    data = db.select(table="details")
    exist_cas_number = []
    exist_chemical_id = []
    for i in data:
        i_id = i["id"]
        cas_number = i["cas_number"]
        chemical_id = i["chemical_id"]
        # 删除无 chemical_id 的项
        if not cas_number or not chemical_id:
            db.delete(table="details", by_items=[("id", i_id)])
            print(f"删除 id: {i_id}")
        # 去重
        if cas_number not in exist_cas_number and chemical_id not in exist_chemical_id:
            exist_cas_number.append(cas_number)
            exist_chemical_id.append(chemical_id)
        else:
            db.delete(table="details", by_items=[("id", i_id)])
            print(f"去重 cas: {cas_number} | chemId: {chemical_id}")
    data = db.select(table="details")
    print(f"最后的数据量: {len(data)}")


def getChemicalInfo(chemical_id):
    db = Database()
    url = "http://hxp.nrcc.com.cn/anxin/chemcatalog/chemInfo"
    params = {
        "id": chemical_id,
        "pageIndex": "0",
        "pageSize": "15"
    }
    headers = {
        "Host": "hxp.nrcc.com.cn",
        "Referer": f"http://hxp.nrcc.com.cn/hc_safe_info_search_detail.html?id={chemical_id}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    data = fakeRequests(url=url, params=params, headers=headers).json()["data"]
    if not data.get("name") or not data.get("casNum"):
        db.delete(table="details", by_items=[("chemical_id", chemical_id)])
        return False
    name = data.get("name") or "-"
    enName = data.get("enName") or "-"
    weixianxingleibie = data.get("weixianxingleibie") or "-"
    xiangxingtu = data.get("xiangxingtu") or "-"
    weixianxingshuoming = data.get("weixianxingshuoming") or "-"
    lihuatexing = data.get("lihuatexing") or "-"
    zhuyaoyongtu = data.get("zhuyaoyongtu") or "-"
    ranshaoyubaozhaweixianxing = data.get("ranshaoyubaozhaweixianxing") or "-"
    huoxingfanying = data.get("huoxingfanying") or "-"
    jinjiwu = data.get("jinjiwu") or "-"
    duxing = data.get("duxing") or "-"
    zhongdubiaoxian = data.get("zhongdubiaoxian") or "-"
    zhiyejiechuxianzhi = data.get("zhiyejiechuxianzhi") or "-"
    huanjingweihai = data.get("huanjingweihai") or "-"
    jijiucuoshi = data.get("jijiucuoshi") or "-"
    xielouyingjichuzhi = data.get("xielouyingjichuzhi") or "-"
    miehuofangfa = data.get("miehuofangfa") or "-"
    ghsType = data.get("ghsType") or "-"
    un = data.get("un") or "-"
    ghsjingshici = data.get("ghsjingshici") or "-"
    # 更新
    casNum = data.get("casNum") or "-"
    dangerous_goods_number = un.split(",")[0]
    categories = weixianxingleibie.split(",")
    category, secondary_category = "", ""
    if categories:
        first_category = categories[0].split("-")
        if len(first_category) == 1:
            category = first_category[0]
        elif len(first_category) == 2:
            category, secondary_category = first_category
        else:
            category = "-".join(first_category[:len(first_category) - 1])
            secondary_category = first_category[-1]
    db.update(
        table="details",
        new_items=[
            ("dangerous_goods_number", dangerous_goods_number),
            ("cas_number", casNum),
            ("category", category),
            ("secondary_category", secondary_category),
            ("status", 200),
            ("name", name),
            ("enName", enName),
            ("weixianxingleibie", weixianxingleibie),
            ("xiangxingtu", xiangxingtu),
            ("weixianxingshuoming", weixianxingshuoming),
            ("lihuatexing", lihuatexing),
            ("zhuyaoyongtu", zhuyaoyongtu),
            ("ranshaoyubaozhaweixianxing", ranshaoyubaozhaweixianxing),
            ("huoxingfanying", huoxingfanying),
            ("jinjiwu", jinjiwu),
            ("duxing", duxing),
            ("zhongdubiaoxian", zhongdubiaoxian),
            ("zhiyejiechuxianzhi", zhiyejiechuxianzhi),
            ("huanjingweihai", huanjingweihai),
            ("jijiucuoshi", jijiucuoshi),
            ("xielouyingjichuzhi", xielouyingjichuzhi),
            ("miehuofangfa", miehuofangfa),
            ("ghsType", ghsType),
            ("ghsjingshici", ghsjingshici)
        ],
        by_items=[("chemical_id", chemical_id)]
    )
    return True


def startGatherDetails():
    db = Database()
    data = db.select(table="details")
    for i_index, i in enumerate(data):
        chemical_id = i["chemical_id"]
        print(chemical_id)
        status = i["status"]
        if str(status) == "200":
            print(f"[{i_index + 1}/{len(data)}]已录入: {chemical_id}")
            continue
        state = getChemicalInfo(chemical_id=chemical_id)
        if state:
            print(f"[{i_index+1}/{len(data)}]成功录入: {chemical_id}")
        else:
            print(f"[{i_index + 1}/{len(data)}]无数据: {chemical_id}")


def excel2db2():
    db = Database()
    excel_path = "envchem.xlsx"
    cas_number, critical_quantity = readExcel(excel_path, [1, 2])
    for i_index, i_cas_number in enumerate(cas_number):
        i_cas_number = i_cas_number.replace("\n", "").strip().replace(" ", "")
        i_critical_quantity = critical_quantity[i_index]
        is_exist = db.select(table="details", items=[("cas_number", i_cas_number)])
        if is_exist:
            db.update(table="details", by_items=[("cas_number", i_cas_number)], new_items=[("critical_quantity", i_critical_quantity)])
            print(f"更新: {i_cas_number} | {i_critical_quantity}")
        else:
            db.insert(table="details", data=[
                ("dangerous_goods_number", ""),
                ("cas_number", i_cas_number),
                ("category", ""),
                ("secondary_category", ""),
                ("status", 0),
                ("name", ""),
                ("enName", ""),
                ("weixianxingleibie", ""),
                ("xiangxingtu", ""),
                ("weixianxingshuoming", ""),
                ("lihuatexing", ""),
                ("zhuyaoyongtu", ""),
                ("ranshaoyubaozhaweixianxing", ""),
                ("huoxingfanying", ""),
                ("jinjiwu", ""),
                ("duxing", ""),
                ("zhongdubiaoxian", ""),
                ("zhiyejiechuxianzhi", ""),
                ("huanjingweihai", ""),
                ("jijiucuoshi", ""),
                ("xielouyingjichuzhi", ""),
                ("miehuofangfa", ""),
                ("ghsType", ""),
                ("ghsjingshici", ""),
                ("critical_quantity", i_critical_quantity)
            ])
            print(f"新建: {i_cas_number} | {i_critical_quantity}")


def db2json():
    db = Database()
    chemicals_data = db.select(table="details")
    chemicals_names = []
    # 处理名称
    for chemical_index, chemical in enumerate(chemicals_data):
        # 提取出所有名称
        chemical_name = chemical["name"]
        # 首先处理 [] 中的备注
        pattern = re.compile(r"\[(.*?)\]")
        remarks = pattern.findall(chemical_name)
        for remark in remarks:
            new_remark = remark.replace(",", "，")
            chemical_name = chemical_name.replace(remark, new_remark)
        # 然后分割出每个名称
        chemical_name = chemical_name.split(",")
        chemical_name = [n.replace("；", ";").replace("＇", "'") for n in chemical_name]
        while True:
            b = False
            for n_index, n in enumerate(chemical_name):
                if n and (n[-1] in list(string.digits + string.ascii_letters + "αβγ'")):
                    if n_index < len(chemical_name) - 1:
                        if (chemical_name[n_index + 1]) and (
                                chemical_name[n_index + 1][0] in list(string.digits + string.ascii_letters + "αβγ-'")):
                            new_n = f"{n},{chemical_name[n_index + 1]}"
                            del chemical_name[n_index]
                            chemical_name[n_index] = new_n
                            break
                    else:
                        if n_index == len(chemical_name) - 1:
                            b = True
                else:
                    if n_index == len(chemical_name) - 1:
                        b = True
            if b:
                break
        # 去除无效名称
        valid_chemical_name = []
        for n in chemical_name:
            if not n or n in list(string.digits + string.ascii_letters + "αβγ-"):
                continue
            else:
                # 继续分隔
                n = n.split(";")
                for m in n:
                    # 恢复备注
                    for remark in remarks:
                        new_remark = remark.replace(",", "，")
                        m = m.replace(new_remark, remark).strip()
                    valid_chemical_name.append(m)
        # 去重
        chemical_name = list(set(valid_chemical_name))
        # 更新字典
        chemical["name"] = chemical_name
        chemical["cas_number"] = chemical["cas_number"].replace(";", "；").split("；")
        chemical["enName"] = [enName.strip() for enName in chemical["enName"].replace(";", "；").split("；")]
        chemical["weixianxingleibie"] = [i for i in chemical["weixianxingleibie"].split(",") if i]
        chemical["xiangxingtu"] = [f"GHS{ghs.strip()}" for ghs in chemical["xiangxingtu"].split("GHS") if ghs]
        chemical["weixianxingshuoming"] = [f"H{i.strip()}" for i in chemical["weixianxingshuoming"].split("H") if i]
        lihuatexing = []
        for chemical_property in chemical["lihuatexing"].split(";"):
            if chemical_property:
                chemical_property = chemical_property.split(":")
                chemical_property_name = chemical_property[0]
                chemical_property_property = chemical_property[1] if len(chemical_property) > 1 else "无资料"
                if re.compile("无资料").findall(chemical_property_property) or not chemical_property_property:
                    chemical_property_property = "无资料"
                if re.compile("无意义").findall(chemical_property_property):
                    chemical_property_property = "无意义"
                chemical_property_dict = {
                    "name": chemical_property_name,
                    "property": chemical_property_property
                }
                lihuatexing.append(chemical_property_dict)
        chemical["lihuatexing"] = lihuatexing
        chemicals_data[chemical_index] = chemical
    with open("chemicals.json", "w", encoding="utf-8") as fp:
        json.dump(chemicals_data, fp)


def getStructPic(cas_number):
    if os.path.exists(f"struct_pic/{cas_number}.png"):
        print(f"CAS-{cas_number}结构式图片已存在！")
        return
    headers = {
        "Host": "www.ichemistry.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        "Referer": "http://www.ichemistry.cn/weixianpin/"
    }
    pic_url = f"http://ichemistry.cn/png_structures/{cas_number}.png"
    response = fakeRequests(url=pic_url, headers=headers)
    if response.status_code != 200:
        init404Pic(f"CAS-{cas_number}结构式图片未找到！", f"struct_pic/{cas_number}.png")
        print(f"CAS-{cas_number}结构式未找到！")
    else:
        with open(f"struct_pic/{cas_number}.png", "wb") as fp:
            fp.write(response.content)
        print(f"CAS-{cas_number}结构式图片已下载！")


def getAllStructPic():
    if not os.path.exists("struct_pic"):
        os.mkdir("struct_pic")
    db = Database()
    data = db.select(table="details")
    fails = []
    for chemical in data:
        cas_number = chemical["cas_number"]
        if not os.path.exists(f"struct_pic/{cas_number}.png"):
            getStructPic(cas_number=cas_number)


def getStructPic2(cas_numbers, chemical_index, counts):
    cas_numbers = cas_numbers.replace(";", "；").split("；")
    for cas_number in cas_numbers:
        chemicals_struct = {}
        if os.path.exists("chemicals-struct.json"):
            with open("chemicals-struct.json", "r", encoding="utf-8") as fp:
                chemicals_struct = json.load(fp)
        if cas_number in chemicals_struct:
            print(f"【{chemical_index+1}/{counts}】【{cas_number}】已采集")
            continue
        if os.path.exists(f"struct_pic/{cas_number}.png"):
            print(f"【{chemical_index+1}/{counts}】【{cas_number}】已采集")
            continue
        url = f"http://cheman.chemnet.com/dict/supplier.cgi?terms={cas_number}&exact=dict&f=plist&hidden=markf"
        response = fakeRequests(url=url)
        response.encoding = "gb2312"
        html = response.text
        tree = etree.HTML(html)
        # 分子式
        molecular_formula = ""
        molecular_formula_td = tree.xpath("//td[contains(text(), '分子式')]/following-sibling::td")
        if molecular_formula_td:
            molecular_formula_td = molecular_formula_td[0]
            molecular_formula_html = tostring(molecular_formula_td, encoding="utf-8").decode("utf-8").replace("\n", "")
            molecular_formula = re.compile(r"<td.*?>(.*?)</td>").findall(molecular_formula_html)[0]
        # 结构式图片
        struct = ""
        struct_img = tree.xpath("//td[contains(text(), '分子结构')]/following-sibling::td//img/@src")
        if struct_img:
            struct = struct_img[0]
            img = fakeRequests(url=struct).content
            with open(f"struct/{cas_number}.png", "wb") as fp:
                fp.write(img)
        chemicals_struct[cas_number] = {
            "struct": struct,
            "molecular_formula": molecular_formula
        }
        with open("chemicals-struct.json", "w", encoding="utf-8") as fp:
            json.dump(chemicals_struct, fp)
        print(f"【{chemical_index+1}/{counts}】【{cas_number}】{molecular_formula} - {struct}")


def getAllStructPic2():
    if not os.path.exists("struct"):
        os.mkdir("struct")
    db = Database()
    data = db.select(table="details")
    counts = len(data)
    for chemical_index, chemical in enumerate(data):
        if chemical_index != 1813:
            continue
        print(chemical["name"])
        cas_number = chemical["cas_number"]
        getStructPic2(cas_numbers=cas_number, chemical_index=chemical_index, counts=counts)


if __name__ == '__main__':
    # db2json()
    getAllStructPic2()