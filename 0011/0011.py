#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019-09-26
@FileName : 0011.py
"""

"""
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，
则打印出 Freedom，否则打印出 Human Rights
"""

def filter_words(path):
    sensitive_words = []  # 存放敏感词语
    # 对文件的处理，最好加上try,except 处理异常
    try:
        with open(path,'r',encoding='utf-8') as f:
            sensitive_words.append(f.readline().strip())
        while True:
            # 从键盘输入词语
            word = input('输入词语:')
            if word == 'exit':
                break
            elif word in sensitive_words:
                print("Freedom")
            else:
                print("Human Rights")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    filter_words('filtered.txt')