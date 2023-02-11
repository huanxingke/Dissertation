import json
import time
import os

from spyder import getChemicalHref, getDetails
from fake_request import fakeRequests


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


with open("catalogue.json", "r", encoding="utf-8") as fp:
    chemicals = json.load(fp)


for stroke_index, chemical in enumerate(chemicals):
    name = chemical[0]
    href = getChemicalHref(keyword=name)
    if href:
        details = getDetails(chemical_href=href)
        if details:
            structural_formula_pic = details["name_information"]["details"]["structural_formula_pic"]["details"]
            cas_number = details["name_information"]["details"]["cas_number"]["details"]
            if cas_number:
                with open("msdsjson/%s.json" % cas_number, "w", encoding="utf-8") as fp:
                    json.dump(details, fp)
                pic_data = fakeRequests(url=structural_formula_pic, headers=headers).content
                with open("structpic/%s.png" % cas_number, "wb") as fp:
                    fp.write(pic_data)
                print("[%s/%s]%s - %s" % (stroke_index+1, len(chemicals), chemical, cas_number))
                time.sleep(2)
            else:
                with open("error/nocas.txt", "a", encoding="utf-8") as fp:
                    fp.write(name + "\n")
        else:
            with open("error/nomsds.txt", "a", encoding="utf-8") as fp:
                fp.write(name + "\n")
    else:
        with open("error/nohref.txt", "a", encoding="utf-8") as fp:
            fp.write(name + "\n")
