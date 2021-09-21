# @-*- coding: utf-8 -*-
# @Time: 2021/9/18 22:11
# @Author: 师玉幺叔
# @Software: Pycharm

import requests
from configs.config import HOST
import hashlib


def get_md5(password):
    # 1.实例化md5对象
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    # 2.返回加密后的结果
    return md5.hexdigest()


class Login:

    def login(self, inData, get_token=True):
        # 1.url
        # url = f'{HOST}/路径'
        url = '{}/account/sLogin'.format(HOST)
        # 2.请求体--字典格式编辑
        inData['password'] = get_md5(inData['password'])
        payload = inData
        res = requests.post(url, data=payload)
        # 3.返回响应数据
        if get_token:
            return res.json()['data']['token']
        else:
            # 返回的是json格式--前提：响应的数据(响应体)一定要是json才可以使用，返回的是字典
            return res.json()


if __name__ == '__main__':
    re = Login().login({'username': 'ka0560', 'password': '23477'}, False)
    print(re)
