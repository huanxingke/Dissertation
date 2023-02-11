import re
from urllib import parse
import json

from lxml import etree

from fake_request import fakeRequests


headers = {
    "Host": "www.chemsrc.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}


def getChemicalHref(keyword):
    url = "https://www.chemsrc.com/searchResult/%s/" % keyword
    html = fakeRequests(url=url, headers=headers).text
    tree = etree.HTML(html)
    chemicals = tree.xpath("//tr[@class='rowDat']/td/a[contains(@href, '/cas/')]/@href")
    if chemicals:
        best_match_href = "https://www.chemsrc.com/%s" % chemicals[0]
    else:
        best_match_href = None
    return best_match_href


def getText(xpath_result, following_sibling=True):
    if xpath_result:
        if not following_sibling:
            return xpath_result[0].strip()
        else:
            xpath_result = "".join([i.strip() for i in xpath_result[0].xpath(".//text()")])
            return xpath_result
    else:
        return ""


def getMSDS(tree, title):
    tds = tree.xpath(".//tr/td")
    content = ""
    for td in tds:
        text = "".join([i.strip() for i in td.xpath(".//text()")])
        if re.findall(title, text):
            this_content = getText(td.xpath(f"./following-sibling::td"))
            if this_content:
                content = this_content
    return content


def getDetails(chemical_href):
    html = fakeRequests(url=chemical_href, headers=headers).text
    tree = etree.HTML(html)
    # ---------- MSDS ---------- #
    msds = tree.xpath("//table[@id='MSDSTbl']")
    if not msds:
        return None
    msds = msds[0]
    # ---------- 名称信息 ---------- #
    # 结构式图片
    structural_formula_pic = getText(tree.xpath("//div[@id='structdiv']/img/@src"), following_sibling=False)
    # 中文名
    Chinese_name = getText(tree.xpath("//tr[@class='detail']/th[contains(text(), '中文名')]/following-sibling::td"))
    # 英文名
    English_name = getText(tree.xpath("//tr[@class='detail']/th[contains(text(), '英文名')]/following-sibling::td"))
    # 中文别名
    Chinese_alias = getText(tree.xpath("//tr[@class='detail']/th[contains(text(), '中文别名')]/following-sibling::td"))
    # CAS号
    cas_number = getMSDS(tree=msds, title="CAS No.")
    # 分子式
    molecular_formula = getMSDS(tree=msds, title="分子式")
    # 分子量
    molecular_weight = getMSDS(tree=msds, title="分子量")
    # ---------- 物化性质 ---------- #
    # 外观与性状
    appearance_and_character = getMSDS(tree=msds, title="外观与性状")
    # 熔点(℃)
    melting_point = getMSDS(tree=msds, title="熔点")
    # 沸点(℃)
    boiling_point = getMSDS(tree=msds, title="沸点")
    # 相对密度(水=1)
    relative_density = getMSDS(tree=msds, title="相对密度")
    # 相对蒸气密度(空气=1)
    relative_air_density = getMSDS(tree=msds, title="相对蒸气密度")
    # 闪点(℃)
    flash_point = getMSDS(tree=msds, title="闪点")
    # 引燃温度(℃)
    ignition_temperature = getMSDS(tree=msds, title="引燃温度")
    # 爆炸上限 %(V/V)
    upper_explosion_limit = getMSDS(tree=msds, title="爆炸上限")
    # 爆炸下限 %(V/V)
    lower_explosion_limit = getMSDS(tree=msds, title="爆炸下限")
    # 溶解性
    solubility = getMSDS(tree=msds, title="溶解性")
    # 主要用途
    main_purpose = getMSDS(tree=msds, title="主要用途")
    # ---------- 危险性概述 ---------- #
    # 危险性类别
    hazard_category = getMSDS(tree=msds, title="危险性类别")
    # 侵入途径
    invasion_route = getMSDS(tree=msds, title="侵入途径")
    # 健康危害
    health_hazards = getMSDS(tree=msds, title="健康危害")
    # 环境危害
    environmental_hazards = getMSDS(tree=msds, title="环境危害")
    # 燃爆危险
    explosion_hazard = getMSDS(tree=msds, title="燃爆危险")
    # ---------- 急救措施 ---------- #
    # 皮肤接触
    skin_contact = getMSDS(tree=msds, title="皮肤接触")
    # 眼睛接触
    eye_contact = getMSDS(tree=msds, title="眼睛接触")
    # 吸入
    inhalation = getMSDS(tree=msds, title="吸入")
    # 食入
    ingestion = getMSDS(tree=msds, title="食入")
    # ---------- 消防措施 ---------- #
    # 危险特性
    hazard_characteristics = getMSDS(tree=msds, title="危险特性")
    # 有害燃烧产物
    hazardous_combustion_products = getMSDS(tree=msds, title="有害燃烧产物")
    # 灭火方法
    fire_extinguishing_method = getMSDS(tree=msds, title="灭火方法")
    # ---------- 泄漏应急处理 ---------- #
    # 应急处理
    emergency_management = getMSDS(tree=msds, title="应急处理")
    # ---------- 操作处置与储存 ---------- #
    # 操作注意事项
    precautions_for_operation = getMSDS(tree=msds, title="操作注意事项")
    # 储存注意事项
    precautions_for_storage = getMSDS(tree=msds, title="储存注意事项")
    # ---------- 防护措施 ---------- #
    # 工程控制
    engineering_control = getMSDS(tree=msds, title="工程控制")
    # 呼吸系统防护
    respiratory_system_protection = getMSDS(tree=msds, title="呼吸系统防护")
    # 眼睛防护
    eye_protection = getMSDS(tree=msds, title="眼睛防护")
    # 身体防护
    body_protection = getMSDS(tree=msds, title="身体防护")
    # 手防护
    hand_protection = getMSDS(tree=msds, title="手防护")
    # 其他防护
    other_protection = getMSDS(tree=msds, title="其他防护")
    # ---------- 废弃处置 ---------- #
    waste_disposal_method = getMSDS(tree=msds, title="废弃处置方法")
    # ---------- 运输信息 ---------- #
    # 包装标志
    packaging_mark = getMSDS(tree=msds, title="包装标志")
    # 包装方法
    packaging_method = getMSDS(tree=msds, title="包装方法")
    # 运输注意事项
    precautions_for_transportation = getMSDS(tree=msds, title="运输注意事项")
    # ---------- 法规信息 ---------- #
    regulatory_information = getMSDS(tree=msds, title="法规")
    details = {
        "name_information": {
            "name": "名称信息",
            "details": {
                "structural_formula_pic": {
                    "name": "结构式图片",
                    "details": structural_formula_pic
                },
                "Chinese_name": {
                    "name": "中文名",
                    "details": Chinese_name
                },
                "English_name": {
                    "name": "英文名",
                    "details": English_name
                },
                "Chinese_alias": {
                    "name": "中文别名",
                    "details": Chinese_alias
                },
                "cas_number": {
                    "name": "CAS号",
                    "details": cas_number
                },
                "molecular_formula": {
                    "name": "分子式",
                    "details": molecular_formula
                },
                "molecular_weight": {
                    "name": "分子量",
                    "details": molecular_weight
                },
            }
        },
        "physical_and_chemical_properties": {
            "name": "物化性质",
            "details": {
                "appearance_and_character": {
                    "name": "外观与性状",
                    "details": appearance_and_character
                },
                "melting_point": {
                    "name": "熔点(℃)",
                    "details": melting_point
                },
                "boiling_point": {
                    "name": "沸点(℃)",
                    "details": boiling_point
                },
                "relative_density": {
                    "name": "相对密度(水=1)",
                    "details": relative_density
                },
                "relative_air_density": {
                    "name": "相对蒸气密度(空气=1)",
                    "details": relative_air_density
                },
                "flash_point": {
                    "name": "闪点(℃)",
                    "details": flash_point
                },
                "ignition_temperature": {
                    "name": "引燃温度(℃)",
                    "details": ignition_temperature
                },
                "upper_explosion_limit": {
                    "name": "爆炸上限 %(V/V)",
                    "details": upper_explosion_limit
                },
                "lower_explosion_limit": {
                    "name": "爆炸下限 %(V/V)",
                    "details": lower_explosion_limit
                },
                "solubility": {
                    "name": "溶解性",
                    "details": solubility
                },
                "main_purpose": {
                    "name": "主要用途",
                    "details": main_purpose
                }
            }
        },
        "hazard_overview": {
            "name": "危险性概述",
            "details": {
                "hazard_category": {
                    "name": "危险性类别",
                    "details": hazard_category
                },
                "invasion_route": {
                    "name": "侵入途径",
                    "details": invasion_route
                },
                "health_hazards": {
                    "name": "健康危害",
                    "details": health_hazards
                },
                "environmental_hazards": {
                    "name": "环境危害",
                    "details": environmental_hazards
                },
                "explosion_hazard": {
                    "name": "燃爆危险",
                    "details": explosion_hazard
                }
            }
        },
        "first_aid_measures": {
            "name": "急救措施",
            "details": {
                "skin_contact": {
                    "name": "皮肤接触",
                    "details": skin_contact
                },
                "eye_contact": {
                    "name": "眼睛接触",
                    "details": eye_contact
                },
                "inhalation": {
                    "name": "吸入",
                    "details": inhalation
                },
                "ingestion": {
                    "name": "食入",
                    "details": ingestion
                }
            }
        },
        "fire_protection_measures": {
            "name": "消防措施",
            "details": {
                "hazard_characteristics": {
                    "name": "危险特性",
                    "details": hazard_characteristics
                },
                "hazardous_combustion_products": {
                    "name": "有害燃烧产物",
                    "details": hazardous_combustion_products
                },
                "fire_extinguishing_method": {
                    "name": "灭火方法",
                    "details": fire_extinguishing_method
                }
            }
        },
        "leakage_emergency_treatment": {
            "name": "泄漏应急处理",
            "details": {
                "emergency_management": {
                    "name": "应急处理",
                    "details": emergency_management
                }
            }
        },
        "handling_and_storage": {
            "name": "操作处置与储存",
            "details": {
                "precautions_for_operation": {
                    "name": "操作注意事项",
                    "details": precautions_for_operation
                },
                "precautions_for_storage": {
                    "name": "储存注意事项",
                    "details": precautions_for_storage
                }
            }
        },
        "protective_measures": {
            "name": "防护措施",
            "details": {
                "engineering_control": {
                    "name": "工程控制",
                    "details": engineering_control
                },
                "respiratory_system_protection": {
                    "name": "呼吸系统防护",
                    "details": respiratory_system_protection
                },
                "eye_protection": {
                    "name": "眼睛防护",
                    "details": eye_protection
                },
                "body_protection": {
                    "name": "身体防护",
                    "details": body_protection
                },
                "hand_protection": {
                    "name": "手防护",
                    "details": hand_protection
                },
                "other_protection": {
                    "name": "其他防护",
                    "details": other_protection
                }
            }
        },
        "waste_disposal": {
            "name": "废弃处置",
            "details": {
                "waste_disposal_method": {
                    "name": "废弃处置方法",
                    "details": waste_disposal_method
                }
            }
        },
        "transportation_information": {
            "name": "运输信息",
            "details": {
                "packaging_mark": {
                    "name": "包装标志",
                    "details": packaging_mark
                },
                "packaging_method": {
                    "name": "包装方法",
                    "details": packaging_method
                },
                "precautions_for_transportation": {
                    "name": "运输注意事项",
                    "details": precautions_for_transportation
                }
            }
        },
        "regulatory_information": {
            "name": "法规信息",
            "details": {
                "regulatory_information": {
                    "name": "法规信息",
                    "details": regulatory_information
                }
            }
        }
    }
    return details


if __name__ == '__main__':
    h = getChemicalHref("甘油")
    de = getDetails(h)
    print(de)