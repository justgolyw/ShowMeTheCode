#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019-09-26
@FileName : 0012.py
"""

def filter_replace_words(path):
    sensitive_words = []  # 存放敏感词语
    # 对文件的处理，最好加上try,except 处理异常
    try:
        with open(path,'r',encoding='utf-8') as f:
            for line in f:
                sensitive_words.append(line.strip())
        print(sensitive_words)
        while True:
            s = input('输入语句:\n')
            if s == 'exit':
                break
            for x in sensitive_words:
                if x in s:
                    # str.replace(old, new[, max])
                    s = s.replace(x, '*'*len(x))
            print(s)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    filter_replace_words('filtered.txt')