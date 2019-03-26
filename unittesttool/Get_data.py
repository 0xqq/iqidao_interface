# coding=utf-8
#依照DataConfig.py文件中指定的各个字段所在列号，从表格中取出值
#特殊字段：
# 1.依赖数据，三种赋值方式
# a.select .......从数据库中获取某关键字段值，需要与依赖数据所属字段相结合组合成请求参数
# b.请求参数json文件中字典名，则是从json文件中获取到某一个案例的请求参数作为依赖数据
# c.depend[......]则从上面某一案例保存的返回json中Data中获取（该数据是通过Depend_data_json.py文件保存至表格中）
import json
import ast
from unittesttool.Operation_excel import oper_excel
from unittesttool.Operationon_datajson import opreation_json
import unittesttool.Data_config
from unittesttool.DB_Select_return import DataBase
from unittesttool.Depend_xls import get_data
class Getdata:
    def __init__(self,excelpath = None, jsonfilepath = None):
        if excelpath:
            self.excelpath = excelpath
        else:
            self.excelpath = "../Test_Case/TestCase.xls"
        if jsonfilepath:
            self.jsonpath = jsonfilepath
        else:
            self.jsonpath = "..//data//Tc_alldata.json"
        self.operation_excel = oper_excel(self.excelpath)
        self.operat_mysql = DataBase()
        self.depend = get_data()
    def get_case_lines(self):
        # 获取case表格的行数
        return self.operation_excel.get_line()
    def get_case_id(self,row):
        col = int(unittesttool.Data_config.get_caseid())
        return int(self.operation_excel.get_cell_value(row, col))
    def get_functionname(self,row):
        col = int(unittesttool.Data_config.get_functionname())
        return self.operation_excel.get_cell_value(row, col)
    def get_web_admin(self,row):
    #     获取接口属于前端或后端
        col = int(unittesttool.Data_config.get_web_admin())
        return self.operation_excel.get_cell_value(row,col)
    def get_is_run(self,row):
        flag = None
        col = int(unittesttool.Data_config.get_isrun())
        run_if = self.operation_excel.get_cell_value(row, col)
        if run_if.startswith("y") or run_if.startswith("Y"):
            flag = True
        else:
            flag = False
        return flag
    def get_files(self, row):
        filesline = int(unittesttool.Data_config.get_files())
        data = self.operation_excel.get_cell_value(row, filesline)
        return data
        # oper_json = opreation_json(self.jsonpath)
        # # print("获取数据",oper_json.get_data(self.get_request_data(row)),type(oper_json.get_data(self.get_request_data(row))))
        # return oper_json.get_data(data)
    def get_return_value(self,row):
        col = int(unittesttool.Data_config.get_return_value())
        return self.operation_excel.get_cell_value(row,col)
    def get_method(self,row):
        col = int(unittesttool.Data_config.get_method())
        return self.operation_excel.get_cell_value(row, col)
    def get_url(self, row):
        col = int(unittesttool.Data_config.get_url())
        return self.operation_excel.get_cell_value(row, col)
    def get_case_depen(self,row):
        col = int(unittesttool.Data_config.get_case_depend())
        data = self.operation_excel.get_cell_value(row, col)
        if data:
            return data
        else:
            return None
    def get_data_depen(self,row):
        col = int(unittesttool.Data_config.get_data_depend())
        data = self.operation_excel.get_cell_value(row, col)
        # try:
        # 若是select语句，则查询数据库
        if data.startswith("select") or data.startswith("SELECT") or data.startswith("Select"):
            return self.operat_mysql.selectvalue(data)
        # except Exception as e:
        #     print("非sql查询语句")
        # 若是从表格中获取保存的返回至
        if data.startswith("depend["):
        #分隔字段，获取到字段名称
            data= data.split('[')[1].split(']')[0]
            getdata = self.depend.get_content_line(data)
            return getdata
        return data
    def get_filed_depen(self,row):
        col = int(unittesttool.Data_config.get_file_depend())
        data = self.operation_excel.get_cell_value(row, col)
        if data:
            return data
        else:
            return None
    def get_request_data(self,row):
        col = int(unittesttool.Data_config.get_request_data())
        data = self.operation_excel.get_cell_value(row, col)
        if data == '':
            return None
        else:
            return data
    # 先获取到data,再data获取json
    def get_data_json(self,row):
        oper_json = opreation_json(self.jsonpath)
        # print("获取数据",oper_json.get_data(self.get_request_data(row)),type(oper_json.get_data(self.get_request_data(row))))
        return oper_json.get_data(self.get_request_data(row))
    def get_expect(self, row):
        col = int(unittesttool.Data_config.get_expect())
        expect = self.operation_excel.get_cell_value(row, col)
        if expect == '':
            return None
        else:
            return expect
    def get_db_value(self, row):
        # 获取sql对比值，直接指向入参或是空
        col = int(unittesttool.Data_config.get_db_value())
        expect = self.operation_excel.get_cell_value(row, col)
        # print("这个数据",expect,col)
        oper_json = opreation_json(self.jsonpath)
        if expect == None:
            return None
        else:
            return oper_json.get_data(expect)

    def get_web_expectvalu(self, row):
        col = int(unittesttool.Data_config.get_web_expectvalu())
        return self.operation_excel.get_cell_value(row, col)
# a = Getdata(excelpath= "..//Test_Case//Paper_Process.xls", jsonfilepath="C:/Iqidao_all/data/Paper_Process.json")
# a = Getdata(excelpath= "..//global_var//depend_data.xls", jsonfilepath="C:/Iqidao_all/data/Paper_Process.json")
# print(a.get_data_depen(73))
# print(a.get_data_json(5))
# print(a.get_filed_depen(4))
# print("shuju",a.get_data_depen(3))
# print("hhh",a.get_files(1))
# print("哈哈",a.get_db_value(3))
# print(a.get_db_value(9))
# print(a.get_expect(3))
# print(a.get_db_value(3))
# # print(a.get_DB_expect(3))
# print(a.get_data_json(1))
#
