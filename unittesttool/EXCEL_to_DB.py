# -*- coding: utf-8 -*-

# 此文件为表格数据插入数据库的工具类，代码不完整。
from unittesttool.DB_CONNECT import DB_CONNECT
import xlrd
from unittesttool.Operation_excel import oper_excel
from unittesttool.Get_data import Getdata
# -*- coding: utf-8 -*-
import pymysql
import xlrd
# 获取glob_var.xls中的数据库链接数据
class Data:
    host = '0'
    port = '1'
    user = '2'
    password = '3'
    charset= '4'
    db = '5'
def get_host():
    return Data.host
def get_port():
    return Data.port
def get_user():
    return Data.user
def get_password():
    return Data.password
def get_charset():
    return Data.charset
def get_db():
    return Data.db
class Return_data:
    def __init__(self, filename=None, sheet_id=None):
        if filename:
            # print("打开的excel",filename)
            self.filename = filename
            self.sheet_id = 0
        else:
            # print("打开的excel",filename)
            self.filename = "../global_var/Data_connect.xls"
            self.sheet_id = 0
        self.data = self.get_excel()
        # 找到文件

    def get_excel(self):
        data = xlrd.open_workbook(self.filename, formatting_info=True)
        tables = data.sheet_by_index(self.sheet_id)
        # 返回查找的sheet表名
        return tables
    def get_cell_value(self, row, col):
        # 获取单元格内容
        return self.data.cell_value(row, col)
        # 根据对应的caseid找到对应的行号

    def return_host(self,row):
        col = int(get_host())
        return self.get_cell_value(row,col)
    def return_port(self,row):
        col = int(get_port())
        return int(self.get_cell_value(row,col))
    def return_user(self,row):
        col = int(get_user())
        return self.get_cell_value(row,col)
    def return_password(self,row):
        col = int(get_password())
        return self.get_cell_value(row,col)
    def return_charset(self,row):
        col = int(get_charset())
        return self.get_cell_value(row,col)
    def return_db(self,row):
        col = int(get_db())
        return self.get_cell_value(row, col)
class DB_CONNECT:
    def __init__(self,i):
        self.data = Return_data()
        self.i = i
    def connect_db(self):
        # 连接数据库
        connect = pymysql.connect(
            host=self.data.return_host(self.i),
            port=self.data.return_port(self.i),
            user=self.data.return_user(self.i),
            # passwd='123456',
            passwd=self.data.return_password(self.i),
            charset=self.data.return_charset(self.i),
            db=self.data.return_db(self.i),
            # 查询结果转换为数据字典类型
            cursorclass=pymysql.cursors.DictCursor
        )
        # 获取游标
        self.cursor = connect.cursor()
        return self.cursor,connect
# if __name__ =='__main__':
#     a = DB_CONNECT(2)
#     a.connect_db()


class exceltodb:
    def __init__(self):
        self.excelpath= "../Test_Case/Paper_Process.xls"
        self.db,self.connect  = DB_CONNECT(2).connect_db()
        self.excel = oper_excel(filename="../Test_Case/Paper_Process.xls")
        self.data = Getdata(excelpath=self.excelpath)
    def read_excel(self):
        print("开始")
        workbook =xlrd.open_workbook("../Test_Case/Paper_Process.xls")
        table = workbook.sheet_by_index(0)
            # 获取数据
        rows_count = self.data.get_case_lines()
        print("hangshu",rows_count)
        for i in range(30,rows_count):
            v1 = int(self.excel.get_cell_value(i,0))
            v2=str(self.excel.get_cell_value(i,1))
            v3 = int(self.excel.get_cell_value(i, 2))
            v4 = str(self.excel.get_cell_value(i, 3))
            v5= str(self.excel.get_cell_value(i, 4))
            v6 = str(self.excel.get_cell_value(i, 5))
            v7 = str(self.excel.get_cell_value(i,6))
            v8 = str(self.excel.get_cell_value(i, 7))
            v9 = self.excel.get_cell_value(i, 8)
            v10 = str(self.excel.get_cell_value(i, 9))
            v11 = self.excel.get_cell_value(i, 10)
            v12 = str(self.excel.get_cell_value(i, 11))
            v13 = str(self.excel.get_cell_value(i, 12))
            v14 = self.excel.get_cell_value(i, 13)
            v15 = self.excel.get_cell_value(i, 14)
            v16 = self.excel.get_cell_value(i, 15)
            v17 = self.excel.get_cell_value(i, 16)
            sql = "INSERT INTO Paper_Process VALUES(%s,'%s',%s,'%s','%s','%s','%s','%s',%s,'%s','%s','%s','%s','%s','%s','%s','%s')"%(v1,v2,v3,v4,v5,v6,v7,v8,v9,pymysql.escape_string(v10),v11,v12,v13,v14,v15,v16,v17)
            print(sql)
            # print(sql)
            # self.db.execute(sql)
            # self.connect.commit()
# if __name__ == '__main__':
#     a = exceltodb().read_excel()