# coding=utf8
import sqlite3
import os

import streamlit as st


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class Database(object):
    def __init__(self):
        self.conn = sqlite3.connect(r"./pw.s3db", check_same_thread=False)
        self.conn.row_factory = dict_factory
        self.c = self.conn.cursor()
        self.tableKeys = {
            # 流域, 行政区, 河名, 库名, 库水位(米), 蓄水量(百万³), 流量(米³/秒), 发布日期, 标识日期
            "daxingshuiku": ["watershed", "administrative_district", "river_name",
                             "reservoir_name", "reservoir_water_level", "storage_capacity",
                             "flow", "public_time", "datetime"],
            # 流域, 行政区, 河名, 站名, 时间, 水位(米), 流量(米²/秒), 警戒水位(米), 发布日期, 标识日期
            "dajiangdahe": ["watershed", "administrative_district", "river_name",
                            "station_name", "time", "water_level",
                            "flow", "warning_water_level", "public_time", "datetime"],
            # 流域, 行政区, 河名, 站名, 日期, 日雨量(毫米), 天气, 发布日期, 标识日期
            "zhongdianyushuiqing": ["watershed", "administrative_district", "river_name",
                                    "station_name", "date", "daily_rainfall",
                                    "weather", "public_time", "datetime"],
            "finished": ["tablename", "datetime"]
        }
        self.create()
        self.c.execute("PRAGMA synchronous = OFF;")

    def select(self, table, key=None, items=None):
        if not key:
            sql = '''select * from {}'''.format(table)
        else:
            where = []
            for by_data_key, by_data_value in items:
                where.append('''{}="{}"'''.format(
                    by_data_key.replace('\\', "").replace('"', "'"),
                    by_data_value.replace('\\', "").replace('"', "'")
                ))
            sql = '''select {} from {} where {};'''.format(
                key.replace('\\', "").replace('"', "'"),
                table, " and ".join(where)
            )
        cursor = self.c.execute(sql)
        result = cursor.fetchall()
        return result

    def insert(self, table, data):
        sql = '''insert into %s(%s) values(%s);''' % (
            table,
            ", ".join(self.tableKeys[table]),
            '"' + '", "'.join([str(i).replace('\\', "").replace('"', "'") for i in data]) + '"'
        )
        self.c.execute(sql)
        self.conn.commit()

    def update(self, table, new_items, by_items):
        update = []
        for new_data_key, new_data_value in new_items:
            update.append('''{}="{}"'''.format(
                new_data_key.replace('\\', "").replace('"', "'"),
                new_data_value.replace('\\', "").replace('"', "'")
            ))
        where = []
        for by_data_key, by_data_value in by_items:
            where.append('''{}="{}"'''.format(
                by_data_key.replace('\\', "").replace('"', "'"),
                by_data_value.replace('\\', "").replace('"', "'")
            ))
        sql = '''update {} set {} where {};'''.format(table, ", ".join(update), " and ".join(where))
        self.c.execute(sql)
        self.conn.commit()

    def create(self):
        try:
            for table, fields in self.tableKeys.items():
                sql = '''create table {} (id INTEGER PRIMARY KEY, {});'''.format(table, ", ".join(
                    [i + " text" for i in fields]))
                self.c.execute(sql)
                self.conn.commit()
        except:
            pass


db = Database()
date_exist = db.select(
    table="finished",
    key="*",
    items=[
        ("tablename", "daxingshuiku"),
        ("datetime", "20230128")
    ]
)
if date_exist:
    st.write("已有数据, 无需重复采集!")
else:
    st.write("无数据!")
st.write(os.path.abspath("./pw.s3db"))