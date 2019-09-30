#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。
密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
"""

import os
from hashlib import sha256
from hmac import HMAC

def encrypt_pwd(password, salt=None):
    if salt is None:
        salt = os.urandom(8) # 64 bits

    password = password.encode("utf-8")

    result = password
    for i in range(10):
        result = HMAC(result, salt,sha256).digest()

    return salt + result


# 验证函数
def validate_pwd(hashed_pwd, input_pwd):
    return hashed_pwd == encrypt_pwd(input_pwd,salt=hashed_pwd[:8])


if __name__ == "__main__":
    hashed_pwd = encrypt_pwd('pwd123')
    assert validate_pwd(hashed_pwd,'pwd123')

















