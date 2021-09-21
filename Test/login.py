# @-*- coding: utf-8 -*-
# @Time: 2021-09-19 12:44
# @Author: 师玉幺叔
# @Software: Pycharm

import requests


# 封装一个登陆函数
def login():
    url = 'http://ip:端口号'
    payload = {'username': 'auto', 'password': 'sdfsdfsdf'}
    resp = requests.post(url, data=payload)
    # return resp.json()
    # return resp.cookies  # cookie对象---直接关联原始cookies
    # 如果项目需求，需要定制化cookies: sessionid + token----需要自己封装cookies
    # cookies里面就是sessionID---直接取出sessionID
    return resp.cookies['sessionid']


# 列出课程
def lesson_list(inDate, inCookie):
    url = 'http://ip:端口号'
    # 自己封装定制化的cookie
    user_cookie = {'sessionid':inCookie, 'token': 'sq'}
    payload = inDate
    resp = requests.get(url, params=payload, cookies=user_cookie)
    # header = {'Cookie': 'sessionid=ycpa2gpsc6ytn457pjhrctiw30uyx1yy; token=sq'}
    # 如果响应头出现编码不是你所需要的中文时，可以通过设置响应编码解决
    # 设置响应编码
    resp.encoding = 'unicode_escape'
    return resp.text
    # return resp.json()

if __name__ == '__main__':
    # 1.登陆
    res = login()
    print(res)
    # 2.列出课程
    res1 = lesson_list({'action': 'list_course', 'pagenum': 1, 'pagesize': 20}, res)
    print(res1)
