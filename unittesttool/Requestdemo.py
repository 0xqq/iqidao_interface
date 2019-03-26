# coding=utf-8
import requests
from  unittesttool.Operation_excel import oper_excel
import json
class inter():
#     构造函数
#     def __init__(self, url, data, method):
#         res = self.run_main(url, data, method)
#         return res

# post接口结构
        # post请求，参数：data(设计参数)，url指定
    def send_post(self, url, data, cookies = None,files= None):
        # allow_redirects=False：禁止重定向的自动跳转
        if files:
            res = requests.post(url=url, data=data, cookies=cookies, verify=False, allow_redirects=False,files = files)

        else:
            res = requests.post(url=url, data=data, cookies=cookies, verify=False, allow_redirects=False,files = None)
        if str(res.status_code).startswith('2'):
            # 201、202等，请求连接成功
            print('接口连接状态', res.status_code, '接口状态正常')
            return res.json(),res.url
        elif str(res.status_code).startswith('3'):
            # 301、302等，重定向
            # response的header中获取重定向指向地址-location
            direct_url = res.headers["Location"]
            print("数据重定向指向该网址",direct_url)
            print('接口连接状态', res.status_code, ',————')
            return res,direct_url
        else:
            print('______接口连接状态', res.status_code,',接口状态异常')
        # return res.json()
    # get接口结构
    def send_get(self, url,params, cookies = None,return_value=None):
        # if header != None:
        # print("---",params,type(params))
        res = requests.get(url=url, params=params, cookies = cookies, verify=False,allow_redirects=False)
        # else:
        #     res = requests.get(url=url, params=params, verify=False,allow_redirects=False)
        if str(res.status_code).startswith('2'):
            # 201、202等，请求连接成功
            print('接口连接状态', res.status_code, '接口状态正常')
            if return_value.startswith("y") or return_value.startswith("Y"):
                # 获取返回的data数据
                try:
                    result = res.json()["Data"][0]
                    excel = oper_excel(filename="../global_var/depend_data.xls")
                    i = len(result)
                    j = 0
                    key= []
                    value = []
                    for k in result:
                        key.append(k)
                        value.append(result[k])
                    for i in range (len(key)):
                        excel.write_value(i,0,key[i])
                        if type(value[i]) == dict:
                            excel.write_value(i,1,str(value[i]))
                        else:
                            excel.write_value(i, 1,value[i])
                except Exception as e:
                    print(e)
            # print("返回",res,res.url)
            return res,res.url
        elif str(res.status_code).startswith('3'):
            # 301、302等，重定向
            # response的header中获取重定向指向地址-location
            direct_url = res.headers["Location"]
            print("数据重定向指向该网址", direct_url)
            print('接口连接状态', res.status_code)
            return res, direct_url
        else:
            print('接口连接状态', res.status_code, ',接口状态异常')

    def run_main(self, url, method, data=None, files= None, cookies = None,return_value=None):
        if method == 'GET':
            res,url = self.send_get(url,data,cookies,return_value=return_value)
        else:
            res,url = self.send_post(url, data,cookies, files)
        # res为json可以做断点检查 ,重新处理为非json格式
        # return json.dumps(res, ensure_ascii=False)
        try:
            return res.json(),url
        except Exception as e:
            print("未返回json格式数据",e)
            return res,url
