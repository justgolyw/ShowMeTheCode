#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019-09-24
@FileName : 0001.py
"""
"""
第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
"""

import uuid
import os

def create_activation_code(num):
    code_list = [] # 保存生成的激活码
    for i in range(num):
        code_list.append(uuid.uuid4())

    return code_list

# 生成激活码并保存到txt文件中
def save_code_to_txt(file,num):
    # 目录不存在时创建目录
    os.makedirs('activation_code', exist_ok=True)
    true_path = os.path.join('activation_code', file)
    with open(true_path, "w") as f:
        for i in range(num):
            activation_code = uuid.uuid4()
            # 按行写入文件：加上'\n'换行
            f.write('\n' + str(activation_code))



if __name__ == "__main__":
    # print(uuid.uuid4())

    # for code in create_activation_code(20):
    #     print(code)

    save_code_to_txt('code.txt', 10)
