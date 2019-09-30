#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019-09-30
@FileName : 0020.py
"""
"""
第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，
然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，
就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，
对每月通话时间做个统计。
"""

import xlrd
import openpyxl
import os

def count_time(xls_name):
    minutes, seconds = 0,0
    total_time = 0
    with xlrd.open_workbook(xls_name) as wb:
        ws = wb.sheet_by_index(0)
        # total_time = 0
    for i in range(2, ws.nrows):
        time = str(ws.row(i)[3].value)
        if '分' in time:
            minute, second_str = time.split('分')
            second = second_str.split('秒')[0]
        else:
            minute, second = 0, time.split('秒')[0]
        print("minute,second", minute, second)

        minutes += int(minute)
        seconds += int(second)
    print("minutes,seconds", minutes, seconds)

    return minutes,seconds

if __name__ == "__main__":
    minutes,seconds = count_time('example.xls')
    minutes += seconds // 60
    seconds = seconds % 60
    print("通话时间总计：", minutes, "分", seconds, "秒")

