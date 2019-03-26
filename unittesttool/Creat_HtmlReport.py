# coding=utf-8
import pandas as pd
import codecs
import os
import xlrd
from unittesttool.Get_data import Getdata
from unittesttool.Case_Table import Case_Table


class report():
    def __init__(self,filename = None,new_filename= None,report_path= None):
        self.tablename= Case_Table().get_tablename()
        if filename:
            self.filename = filename
        else:
            self.filename = "../Test_Case/"+self.tablename+".xls"
        if new_filename:
            self.new_filename = new_filename
        else:
            self.new_filename = "../Test_Case/"+self.tablename+"_bk.xls"
        if report_path:
            self.report_path = report_path
        else:
            self.report_path = "../Test_Case/TestCase.html"
        self.data =Getdata()
    def order_excel(self):
        read_excel= xlrd.open_workbook(self.filename)
        # 借助辅助数组，rows_mark
        rows_mark = []
        #遍历是否执行列数据
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            isrun = self.data.get_is_run(i)
            #如果不执行，则将该行数记录
            if isrun == False:
                rows_mark.append(i)
        return rows_mark
    #生成报告
    def creat_report(self):
        # 获取不执行案例所在行数
        rows = self.order_excel()
        #读取测试案例表格文件，跳过不执行的行数
        xd = pd.read_excel(self.filename, skiprows=rows,
                           usecols=[0,1, 4, 12, 13, 15, 16])  # 指定读取列
        # print(xd)
        #摘取所需要内容生成新的xls文件
        xd.to_excel(self.new_filename, index=False)
        #将excel转换为html
        to_html = pd.ExcelFile(self.new_filename)
        pd.set_option('display.max_colwidth', 1000)  # 设置列的宽度，以防止出现省略号
        df = to_html.parse()
        with codecs.open(self.report_path, 'w') as html_file:
            html_file.write(df.to_html(header=True, index=False,table_id="Test_Report"))
        # 将多余文件删除
        os.remove(self.new_filename)
        #自动打开报告文件
        # webbrowser.open(self.report_path)
# 案例表格、数据文件路径

# case_excelpath = "..//Test_Case//Paper_Process.xls"
# data_jsonpath="../data/Paper_Process.json"
# # # 定义报告文件
# excel_copy = "..//Test_Case//Paper_Process_bk.xls"
# html_path = "../Test_Case/Paper_Process.html"
# a = report(case_excelpath,excel_copy,html_path)
# a.creat_report()