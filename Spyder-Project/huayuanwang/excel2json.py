import json
import re

from excel_manager import readExcel


def getJSONCatalogue():
    excel_path = "catalogue.xlsx"
    column_0 = readExcel(excel_path=excel_path)
    column_1 = readExcel(excel_path=excel_path, column_index=1)
    column_0 = ["".join([re.sub(r"\s+", "", j) for j in i]).split("…")[0] for i in column_0]
    data = []
    for i_index, i in enumerate(column_0):
        i = i.split("...")[0].replace("\n", "")
        j = column_1[i_index]
        data.append((i, j))
    data = sorted(list(set(data)), key=lambda x: column_0.index(x[0]))
    with open("catalogue.json", "w", encoding="utf-8") as fp:
        json.dump(data, fp)


if __name__ == '__main__':
    getJSONCatalogue()