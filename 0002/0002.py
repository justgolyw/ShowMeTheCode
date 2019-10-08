#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019-09-24
@FileName : 0002.py
"""
"""
第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
"""
import pymysql

def save_code_to_mysql(filename):
    # 打开数据库连接
    conn = pymysql.Connect(user='root', password='', database='test')
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    # 使用execute方法执行SQL语句:建表
    cursor.execute("drop table if exists code_table")
    cursor.execute('create table code_table(id varchar(20) primary key, code varchar(100))')
    index = 0
    with open(filename, 'r') as f:
        code_list = f.readlines()
    for code in code_list:
        cursor.execute('insert into code_table(id,code) values(%s,%s)',[str(index),code])
        index += 1
        # 提交
        conn.commit()

    conn.close()
    print('success!!')

def open_mysql():
    # 打开数据库连接
    conn = pymysql.Connect(user='root', password='', database='test')
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("select * from code_table")
    # 使用fetchall获取所有的数据
    data = cursor.fetchall()
    # 使用fetchone获取某一条数据
    data = cursor.fetchone()
    print(data)
    # 关闭数据库连接
    conn.close()

if __name__ == '__main__':
    save_code_to_mysql('code.txt')