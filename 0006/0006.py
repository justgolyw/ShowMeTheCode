#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019-09-25
@FileName : 0006.py
"""

"""
**第 0006 题：**你有一个目录，放了你一个月的日记，
都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
"""

import os
import collections
import re


def count_word(path):
    most_import_word_list = []
    file_list = os.listdir(path)
    # print(file_list)
    for file in file_list:
        file_path = os.path.join(path, file)
        with open(file_path,'r') as f:
            word_list = re.findall('([a-zA-Z]+)', f.read().lower())
            most_import_word = collections.Counter(word_list).most_common(1)
            most_import_word_list.append(most_import_word)
    return most_import_word_list

def count_word2(path):
    most_import_word_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(path, file)
            with open(file_path, 'r') as f:
                word_list = re.findall('([a-zA-Z]+)', f.read().lower())
                most_import_word = collections.Counter(word_list).most_common(1)
                most_import_word_list.append(most_import_word)
        return most_import_word_list



if __name__ == "__main__":

    most_import_word_list = count_word2('diary')
    for word in most_import_word_list:
        print(word[0][0])


