#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019-09-25
@FileName : 0007.py
"""
'''
第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
包括空行和注释，但是要分别列出来
'''

import os


def count_code(path):
    file_list = os.listdir(path)
    for file in file_list:
        code_num = 0  # 代码行数
        empty_num = 0 # 空格行数
        note_num = 0 # 注释行数
        note_num_flag = False # 注释开始标志

        file_path = os.path.join(path, file)
        with open(file_path, 'r', encoding="utf-8") as f:
            for line in f.readlines():
                if (line.strip().startswith('"""') and not note_num_flag)\
                    or (line.strip().startswith("'''") and note_num_flag):
                    note_num += 1
                    note_num_flag = True  # 注释开始
                elif line.strip().startswith('"""') or line.strip().startswith("'''"):
                    note_num_flag = False # 注释结束
                    note_num += 1
                elif line.strip().startswith('#') or note_num_flag:
                    note_num += 1
                elif line.strip() == '':
                    empty_num += 1
                else:
                    code_num += 1

        # print("在%s中，有%d行代码，有%d行空行，有%d行注释" % (file, code_num, empty_num, note_num))
        print("在{0}中，有{1}行代码，有{2}行空行，有{3}行注释".format(file,code_num, empty_num, note_num))



if __name__ == "__main__":
    count_code('code')