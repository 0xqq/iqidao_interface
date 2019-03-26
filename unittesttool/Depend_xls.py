# -*- coding: utf-8 -*-
import xlrd
import os
# 获取Depend_data.xls中的数据，该表格中的数据为某一案例请求返回的参数保存的Data数据，用于依赖案例使用
class get_data:
    # 根据内容获取行号,返回所在行指定列的值
    def __init__(self,depend_excel= None):
        if depend_excel:
            self.depend_excel = depend_excel
        else:
            self.depend_excel = "../global_var/depend_data.xls"
            # 找到文件
        # self.data = self.get_excel()
    # def get_excel(self):
    #     book = xlrd.open_workbook(self.depend_excel, formatting_info=True)
    #     tables = book.sheet_by_index(0)
    #     # 返回查找的sheet表名
    #     return tables
        # 根据值获取所在行指定列的值
    def get_content_line(self, content):
        # print(self.data.nrows)
        book = xlrd.open_workbook(self.depend_excel, formatting_info=True)
        tables = book.sheet_by_index(0)
        data_dict= {}
        data_list = []
        # for i in range(tables.nrows):
        #     data = tables.cell_value(i, 0)
        #     print("去找dataa",data,tables.nrows,i)
        #     # print(data)
        #     if data == content:
        #         print("找到了",data)
        #         data_dict[content] = int(tables.cell_value(i, 1))
        #         return data_dict
        #     else:
        #         print("未找到字段名称为", content, "的数据，请检查是否存在错误")
        #         return None
        i =0
        while i < tables.nrows:
            data = tables.cell_value(i, 0)
            if data == content:
                data_dict[content] = int(tables.cell_value(i, 1))
                return data_dict
            else:
                i=i+1
        if data!= content:
            print("没有找到",data)
            return None
        # 清除掉缓存
        del book
        del tables
# a = get_data()
# print(a.get_content_line("Id"))
