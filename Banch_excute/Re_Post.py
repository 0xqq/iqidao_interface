# -*- coding: utf-8 -*-
# coding=utf-8
import requests
import json
def getfile(file_path):
    try:
        with open(file_path,"r") as f:
            data = json.load(f)
    except Exception as e:
        print("无法找到参数文件", file_path)
    return data
def requests_batch(file_path,params_name,url):
    # data2 = {
    #             'password': '111111',
    #             'captcha': '666666',
    #             'key':'13811469892',
    #             "rememberMe": 1
    #         }
    data2 = {
                'phone': '15865701027',
                'password': 'wawdj255357',
                'captcha': '666666'
            }
    r1 = requests.post("https://testing.iqidao.com/admin001/signin", verify=False, data=data2)
    # r1 = requests.post("https://testing.iqidao.com/json/user/signin", verify=False, data=data2)
    # print("r1执行了",r1.text)
    cookies1 = r1.cookies
    # 获取文件中的参数
    data = getfile(file_path)
    #判断参数个数
    # 多个参数值
    if len(data[params_name]) > 1:
        # print("---",type(data),data["children"])
        for i in range(len(data[params_name])):
            di = {}
            data_i = data[params_name][i]
            print(data_i, type(data_i))
            # "https://testing.iqidao.com/admin001/activity/user/add"
            r2 = requests.post(url, cookies=cookies1, verify=False,data=data_i)
            # print(r2.text)
        return r2.status_code
    # 无参数
    elif len(data[params_name]) <= 0:
        print("未找到数据")
    # 有且仅有一条参数
    else:
        r2 = requests.post(url, cookies=cookies1, verify=False,data=data[params_name][0])
        print("***响应结果***",r2.text)
        return r2.status_code

# a = requests_batch(file_path="C:/Iqidao_all/data/Paper_assign1.json",params_name="Paper_assign1",url="https://testing.iqidao.com/papers_t/cast/add")