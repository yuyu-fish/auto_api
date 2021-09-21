# @-*- coding: utf-8 -*-
# @Time: 2021/9/18 22:11
# @Author: 师玉幺叔
# @Software: Pycharm

import requests
from configs.config import HOST
from lib.login import Login


# 店铺的模块
class Shop:
    # 每一次或者每一个店铺的实例，都只需要鉴权一次
    def __init__(self, inTokrn):
        self.header = {"Authorization": inTokrn}

    # 1.列出店铺
    def shop_list(self, inData):
        # 1.url配置，get请求的参数是在url中的，即url?xxx=xxx
        url = '{}/shopping/myShop'.format(HOST)
        # 2.参数
        payload = inData
        # 3.发送请求
        # params 会把数据拼接到url后面，例如：http:/ip:端口号/shopping/myShop?page=1&limit=10
        res = requests.get(url=url, params=payload, headers=self.header)
        # 打印url
        # print(res.request.url)
        # 4.返回响应体
        return res.text


if __name__ == '__main__':
    # 1.登录
    token = Login().login({'username': 'ka0560', 'password': '23477'})
    re = Shop(token).shop_list({'page': 1, 'limit': 10})
    print(re)



"""
1.token：一般需要账号与密码通过特定的接口(登录/获取token的接口)去服务器访问，才能返回一个token值 
2.cookie--sessionID：会话id，只要访问这个浏览器，就会返回一个session，一般在响应头里(set-cookies: jsessionid=xxxxxx)
"""