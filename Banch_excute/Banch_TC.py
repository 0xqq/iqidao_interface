# -*- coding: utf-8 -*-
# coding=utf-8

import requests
from unittesttool.Get_data import Getdata
from unittesttool.Operation_excel import oper_excel
from Banch_excute.Re_Post import requests_batch
class Run_case():
        def __init__(self, excelpath, file_path):
            self.data = Getdata(excelpath=excelpath)
            self.opexcel = oper_excel(filename=excelpath)
            self.file_path = file_path
        def banch_case(self):
            rows_count = self.data.get_case_lines()
            print("**********",rows_count)
            # print(rows_count)
            # 排除表头，从-1开始
            for i in range(1, rows_count):
                url = self.data.get_url(i)
                functionname = self.data.get_functionname(i)
                # method = self.data.get_method(i)
                isrun = self.data.get_is_run(i)
                # print("第", i, "条执行记录", isrun, functionname)
                # print("+++++++",url,isrun,functionname)
                # 查看运行状态是否运行
                if isrun:
                    # print("第", i, "条执行记录", isrun, functionname)
                    res = requests_batch(file_path=self.file_path+"/"+functionname+".json",params_name=functionname,url=url)
                    try:
                        print(res.json)
                    except Exception as e:
                        print("未返回数据")
if __name__ =='__main__':
    c = Run_case(excelpath="C://Iqidao_all//Test_Case//banch_param.xls",file_path="C:/Iqidao_all/data")
    c.banch_case()
