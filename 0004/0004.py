#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019-09-24
@FileName : 0004.py
"""
"""
**第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。
"""
import collections
import re

def count_word(file):
    with open(file, 'r') as f:
        word_list = []
        for line in f:
            line_words = line.lower().split() # 默认为所有的空字符，包括空格、换行(\n)、制表符(\t)
            word_list.extend(line_words) # 列表扩展

    words_dict = dict((collections.Counter(word_list)))
    return words_dict

# 正则表达式查找
def count_word2(file):
    with open(file, 'r') as f:
        word_list = re.findall('([a-zA-Z]+)', f.read().lower())
        words_dict = dict((collections.Counter(word_list)))
        return words_dict



if __name__ == "__main__":
    words_dict = count_word2('0004.txt')
    total_counts = 0
    for k, v in words_dict.items():
        total_counts+=v
        print(k,v)
    print("totalCount:",total_counts)

