# -*- coding: utf-8 -*-
from unittesttool.Operation_excel import oper_excel
# 依赖数据处理，数据来源为上一案例请求发出后的返回值，获取Data字典内容，保存至表格中
class depend_data_json:
    def __init__(self,depend_path= None):
        if depend_path:
            self.depen_path = depend_path
        else:
            self.depen_path = "C:/Iqidao_all/global_var/depend_data.xls"
    # 将接口返回字典数据存储到表格中用作公共变量
    def save_json(self,rejson):
        result = rejson["Data"][0]
        excel = oper_excel(filename=self.depen_path)
        i = len(result)
        j = 0
        key = []
        value = []
        for k in result:
            key.append(k)
            value.append(result[k])
        for i in range(len(key)):
            excel.write_value(i, 0, key[i])
            excel.write_value(i, 1, value[i])
# a = depend_data()
# re = {'Status': 0, 'Data': [{'Id': 844, 'Value': '活动99(2019-01-30-2019-02-10)赵老师1'}]}
# a.save_json(re)
