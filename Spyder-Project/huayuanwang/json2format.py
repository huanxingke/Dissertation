import json
import os
import re

from excel_manager import writeExcel


type = {
    "-": "-",
    "1": "[1]爆炸品",
    "2.1": "[2.1]易燃气体",
    "2.2": "[2.2]不燃气体",
    "2.3": "[2.3]有毒气体",
    "3.1": "[3.1]易燃液体（低闪点）",
    "3.2": "[3.2]易燃液体（中闪点）",
    "3.3": "[3.3]易燃液体（高闪点）",
    "4.1": "[4.1]易燃固体",
    "4.2": "[4.2]自燃物品",
    "4.3": "[4.3]遇湿易燃物品",
    "5.1": "[5.1]氧化剂",
    "5.2": "[5.2]有机过氧化物",
    "6.1": "[6.1]毒害品",
    "6.2": "[6.2]感染性物质",
    "7": "[7]放射性物品",
    "8.1": "[8.1]腐蚀品（酸性）",
    "8.2": "[8.2]腐蚀品（碱性）",
    "8.3": "[8.3]腐蚀品（其他）",
    "9": "[9]磁性物品",
}
json_list = ["msdsjson/" + i for i in os.listdir("msdsjson")]
header = ["名称", "别名", "分子式", "分类", "物化性质", "危险特性", "防护措施", "应急措施", "储运须知", "废弃物处理", "结构式图片", "CAS号"]
rows = []
for json_file in json_list:
    with open(json_file, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    # 结构式图片
    structural_formula_pic = data["name_information"]["details"]["structural_formula_pic"]["details"]
    # CAS
    cas_number = data["name_information"]["details"]["cas_number"]["details"]
    # 名称
    name = data["name_information"]["details"]["Chinese_name"]["details"]
    # 别名
    alias = data["name_information"]["details"]["Chinese_alias"]["details"]
    if alias:
        alias = alias.split("|")
        alias_string = ""
        for i in range(1, len(alias) + 1):
            alias_string += f"（{i}）{alias[i-1]}。\n"
    else:
        alias_string = "-"
    # 分子式
    molecular_formula = data["name_information"]["details"]["molecular_formula"]["details"]
    # 分类
    regulatory_information = data["regulatory_information"]["details"]["regulatory_information"]["details"]
    chemical_type = re.compile(r"第(.*?)类").findall(regulatory_information)
    chemical_type = chemical_type[0] if chemical_type else "-"
    chemical_type = type[chemical_type.strip()] if chemical_type.strip() in type else "-"
    # 物化性质
    # 外观性状
    appearance_and_character = data["physical_and_chemical_properties"]["details"]["appearance_and_character"]["details"]
    # 物理性质
    relative_density = data["physical_and_chemical_properties"]["details"]["relative_density"]["details"]
    relative_air_density = data["physical_and_chemical_properties"]["details"]["relative_air_density"]["details"]
    melting_point = data["physical_and_chemical_properties"]["details"]["melting_point"]["details"]
    boiling_point = data["physical_and_chemical_properties"]["details"]["boiling_point"]["details"]
    flash_point = data["physical_and_chemical_properties"]["details"]["flash_point"]["details"]
    ignition_temperature = data["physical_and_chemical_properties"]["details"]["ignition_temperature"]["details"]
    # 溶解性
    solubility = data["physical_and_chemical_properties"]["details"]["solubility"]["details"]
    properties_string = f"（1）外观与性状：{appearance_and_character or '无资料。'}\n"
    properties_string += f"（2）相对密度（水=1）：{relative_density or '无资料'}。"
    properties_string += f"相对蒸气密度（空气=1）：{relative_air_density or '无资料'}。"
    properties_string += f"熔点（℃）：{melting_point or '无资料'}。"
    properties_string += f"沸点（℃）：{boiling_point or '无资料'}。"
    properties_string += f"闪点（℃）：{flash_point or '无资料'}。"
    properties_string += f"引燃温度（℃）：{ignition_temperature or '无资料'}。\n"
    properties_string += f"（3）溶解性：{solubility or '无资料。'}"
    # 危险特性
    # 环境
    explosion_hazard = data["hazard_overview"]["details"]["explosion_hazard"]["details"]
    hazard_characteristics = data["fire_protection_measures"]["details"]["hazard_characteristics"]["details"]
    # 健康
    health_hazards = data["hazard_overview"]["details"]["health_hazards"]["details"]
    hazard_string = f"（1）环境：{explosion_hazard + hazard_characteristics}\n"
    hazard_string += f"（2）健康：{health_hazards}"
    # 防护措施
    engineering_control = data["protective_measures"]["details"]["engineering_control"]["details"]
    respiratory_system_protection = data["protective_measures"]["details"]["respiratory_system_protection"]["details"]
    eye_protection = data["protective_measures"]["details"]["eye_protection"]["details"]
    body_protection = data["protective_measures"]["details"]["body_protection"]["details"]
    hand_protection = data["protective_measures"]["details"]["hand_protection"]["details"]
    other_protection = data["protective_measures"]["details"]["other_protection"]["details"]
    protect_method = f"{engineering_control}{respiratory_system_protection}{eye_protection}{body_protection}{hand_protection}{other_protection}"
    # 应急措施
    fire_extinguishing_method = data["fire_protection_measures"]["details"]["fire_extinguishing_method"]["details"]
    skin_contact = data["first_aid_measures"]["details"]["skin_contact"]["details"]
    eye_contact = data["first_aid_measures"]["details"]["eye_contact"]["details"]
    inhalation = data["first_aid_measures"]["details"]["inhalation"]["details"]
    ingestion = data["first_aid_measures"]["details"]["ingestion"]["details"]
    measures_string = f"（1）消防：{fire_extinguishing_method}\n"
    measures_string += f"（2）急救：若有皮肤接触，{skin_contact}"
    measures_string += f"若有眼睛接触，{eye_contact}"
    measures_string += f"若有吸入的情况，{inhalation}"
    measures_string += f"若有食入的情况，{ingestion}"
    # 储运须知
    packaging_method = data["transportation_information"]["details"]["packaging_method"]["details"]
    precautions_for_storage = data["handling_and_storage"]["details"]["precautions_for_storage"]["details"]
    precautions_for_transportation = data["transportation_information"]["details"]["precautions_for_transportation"]["details"]
    leakage_emergency_treatment = data["leakage_emergency_treatment"]["details"]["emergency_management"]["details"]
    known_string = f"（1）包装方法：{packaging_method}\n"
    known_string += f"（2）储运条件：{precautions_for_storage + precautions_for_transportation}\n"
    known_string += f"（3）泄漏处理：{leakage_emergency_treatment}"
    # 废弃物处理
    waste_disposal = data["waste_disposal"]["details"]["waste_disposal_method"]["details"] or "-"
    row = [name, alias_string, molecular_formula, chemical_type, properties_string, hazard_string, protect_method, measures_string, known_string, waste_disposal, structural_formula_pic, cas_number]
    rows.append(row)
writeExcel(sheet_name="Chemicals", header=header, data=rows, excel_path="chemicals.xlsx")