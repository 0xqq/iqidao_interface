# coding=utf-8
# 导入excel操作包
import xlrd


#取出TestCase.xls中的数据
# 测试文件名大写
class global_var:
    user_phone = '0'
    password = '1'
    captcha = '2'
    url = '3'
def get_username():
    return global_var.user_phone
def get_password():
    return global_var.password
def get_captcha():
    return global_var.captcha

# 获取url
def get_url():
    return global_var.url
class Return_global_var:
    def __init__(self, filename=None, sheet_id=None):
        if filename:
            # print("打开的excel",filename)
            self.filename = filename
            self.sheet_id = 0
        else:
            # print("打开的excel",filename)
            self.filename = "../global_var/global_var.xls"
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

    def return_username(self,row):
        col = int(get_username())
        return int(self.get_cell_value(row,col))
    def return_password(self,row):
        col = int(get_password())
        return int(self.get_cell_value(row,col))
    def return_captcha(self,row):
        col = int(get_captcha())
        return int(self.get_cell_value(row,col))
    def return_url(self,row):
        col = int(get_url())
        return self.get_cell_value(row,col)
# a = Return_global_var()
# print(a.return_url(1))
