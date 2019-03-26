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

