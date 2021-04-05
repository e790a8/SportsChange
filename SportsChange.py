#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author   : lisztomania
# @Date     : 2021/4/3
# @Software : Pycharm
# @Version  : Python 3.8.5
# @File     : SportsChange.py
# @Function :

import time
import requests
from urllib.parse import urlparse, parse_qs
from random import randint
from typing import Tuple


def access(phone: str, password: str) -> Tuple:
    """
    获取access

    :param phone: 小米运动注册手机号
    :param password: 密码
    :return:
        bool: 是否成功
        access: access值
    """
    url = f'https://api-user.huami.com/registrations/+86{phone}/tokens'
    header = {
        'app_name': 'com.xiaomi.hm.health',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    data = {
        'password': password,
        'client_id': 'HuaMi',
        'token': 'access',
        'redirect_uri': 'https://s3-us-west-2.amazonaws.com/hm-registration'
                        '/successsignin.html'
    }

    html = requests.post(url=url, headers=header, data=data,
                         allow_redirects=False)
    if html.status_code == 303:
        if html.headers.get('Location'):
            return True, parse_qs(qs=urlparse(url=html.headers.get('Location'))
                                  .query).get('access')[0]
    return False, ''


def token_id(access: str) -> Tuple:
    """
    获取token与userid

    :param access: access值
    :return:
        bool: 是否成功
        token: token值
        userid: 用户id
    """
    url = 'https://account.huami.com/v2/client/login'
    header = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    data = {
        'app_name': 'com.xiaomi.hm.health',
        'country_code': 'CN',
        'code': access,
        'device_id': f'{hex(randint(16, 255))[2:]}:'
                     f'{hex(randint(16, 255))[2:]}:'
                     f'{hex(randint(16, 255))[2:]}:'
                     f'{hex(randint(16, 255))[2:]}:'
                     f'{hex(randint(16, 255))[2:]}:'
                     f'{hex(randint(16, 255))[2:]}',
        'device_model': 'android_phone',
        'app_version': '5.0.0',
        'grant_type': 'access_token',
        'third_name': 'huami_phone'
    }
    html = requests.post(url=url, headers=header, data=data)
    if html.status_code == 200:
        temp = html.json().get('token_info')
        if temp:
            return True, temp.get('app_token'), temp.get('user_id')
    return False, '', ''


def update(app_token: str, user_id: str, number: int) -> bool:
    """
    更新步数

    :param app_token: token值
    :param user_id: 用户id
    :param number: 步数
    :return:
        bool: 是否成功
    """
    url = 'https://api-mifit-cn2.huami.com/v1/data/band_data.json?'
    header = {
        'apptoken': app_token,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    date = time.strftime('%Y-%m-%d')
    json = r'''[{"summary":"{\"sn\":\"\",\"slp\":{\"ss\":0,\"lt\":0,\"dt\":0,\"st\":1616169600,\"lb\":0,\"dp\":0,\"is\":0,\"rhr\":0,\"stage\":[],\"ed\":1616169600,\"wk\":0,\"wc\":0},\"stp\":{\"runCal\":0,\"cal\":82,\"conAct\":0,\"stage\":[{\"stop\":723,\"mode\":1,\"dis\":221,\"step\":333,\"cal\":7,\"start\":718},{\"stop\":707,\"mode\":1,\"dis\":301,\"step\":453,\"cal\":9,\"start\":701},{\"stop\":685,\"mode\":1,\"dis\":272,\"step\":409,\"cal\":5,\"start\":679},{\"stop\":485,\"mode\":1,\"dis\":705,\"step\":983,\"cal\":27,\"start\":469}],\"ttl\":%s,\"dis\":2250,\"rn\":0,\"wk\":46,\"runDist\":0,\"ncal\":0},\"tz\":\"28800\",\"v\":6,\"goal\":8000}","data":[{"stop":1439,"value":"fv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Jfv8Lfv8Afv9Ofv9Mfv9Mfv9Mfv8Afv8Nfv9Yfv9Yfv9Yfv8sfv+Sfv8Afv8Afv8Afv+Mfv8Afv9Gfv8Ofv8Afv8Afv8Afv8Afv8Afv8\/fv8Afv9Lfv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Cfv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Rfv8Afv8Afv8Afv8Afv8Afv8kfv8Qfv8Bfv8Afv8Afv8Afv8Mfv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Ufv8Afv8Zfv8Afv8Hfv8Afv8ifv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Zfv8Gfv8gfv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv9Ifv8Pfv8Afv8Nfv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Rfv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv9Pfv8Afv8ufv8Afv8Afv8Afv8Afv9Jfv84fv84fv84fv84fv84fv84fv8Afv8Afv8Afv8Afv8Afv8Afv8Ofv8Afv8Afv8Afv8Bfv8Afv8Afv8Afv8Afv8tfv9Efv9Efv9Efv9Efv9Efv9Efv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv9Ofv8+fv8+fv8+fv8+fv8Hfv9ifv8Afv81fv8Nfv8Afv8Afv8Afv8Afv8Afv8Afv8Afv+Mfv8Afv8Afv8Wfv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Ifv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Cfv8Gfv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8afv8Afv8Bfv8Afv8Afv8Afv8Afv8Afv8Afv8Ofv8WfgAAfgAAfgAAfgAAfgAAfv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8Afv8QfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAA","did":"-1","tz":0,"src":7,"start":0}],"data_hr":"","summary_hr":"","date":"%s"}]'''
    data = {
        'data_json': json % (str(number), date),
        'device_type': '2',
        'last_deviceid': '-1',
        'last_source': '7',
        'last_sync_data_time': int(time.time()),
        'userid': user_id
    }
    html = requests.post(url=url, headers=header, data=data)
    if html.status_code == 200:
        if html.json().get('code') == 1:
            return True
    return False


def main():
    phone = input('请输入小米运动注册手机号:').strip()
    password = input('请输入密码:').strip()
    on, access1 = access(phone, password)
    if on:
        on, token, userid = token_id(access1)
        if on:
            number = int(input('请输入步数:').strip())
            if update(token, userid, number):
                print('更新成功')
            else:
                print('更新失败')
        else:
            print('token获取失败')
    else:
        print('账号或密码输入错误,请重新输入')


main()
