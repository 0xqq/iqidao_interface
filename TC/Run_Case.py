# coding=utf-8
import requests
import os
import sys
rootpath=str("unittesttool")
syspath=sys.path
sys.path=[]
sys.path.append(rootpath)#将工程根目录加入到python搜索路径中
# sys.path.extend([rootpath+"."+i for i in os.listdir(rootpath) if i[0]!="."])#将工程目录下的一级目录添加到python搜索路径中
sys.path.extend(syspath)
print(sys.path)
from unittesttool.Requestdemo import inter
from unittesttool.Get_data import Getdata
from unittesttool.Expect_IsEqual import isequal
from unittesttool.Send_email import sendmail
from unittesttool.WebPageCheck import PageCheck
from unittesttool.Oper_depend_data import dependata
from unittesttool.Get_cookies import Get_cookies
from TC.Case_judgement import Case
from unittesttool.Creat_HtmlReport import report
from unittesttool.Operation_excel import oper_excel
import xlrd
from Get_Case.DB_Case import Get_case
from Get_Case.Case_Table import Case_Table
class Run_case():
    # class执行前执行，且一个class只执行一次
    # @classmethod
    # def setupClass(cls):
    #     print('class执行前执行')
    # # 每个方法执行前执行一次
    # def setUp(self):
    #     print('test前执行')
    def __init__(self,excelpath = None,jsonpath = None):
        self.tablename= Case_Table().get_tablename()
        if excelpath:
            self.excelpath = excelpath
        else:
            self.excelpath = "../Test_Case/"+self.tablename+".xls"
        if jsonpath:
            self.jsonpath = jsonpath
        else:
            self.jsonpath = "../data/"+self.tablename+".json"
        self.run_method = inter()
        self.data = Getdata(self.excelpath,self.jsonpath)
        self.result = isequal()
        self.sendmail = sendmail()
        self.page_check = PageCheck()
        self.de_data = dependata(self.excelpath,self.jsonpath)
        self.caserun = Case(excelpath=self.excelpath,jsonpath=self.jsonpath)
        self.opexcel = oper_excel(filename=excelpath)
        self.DBCASE = Get_case()
    # 学生登陆cookies
    def student_cookies(self):
        cookies = Get_cookies(2)
        return cookies.getcookies_web()
    #admin登陆cookies
    def admin_cookies(self):
        cookies = Get_cookies(1)
        return cookies.get_cookies_admin()
    # 教师登陆cookies
    def teacher_cookies(self):
        cookies = Get_cookies(3)
        return cookies.getcookies_web()
    def go_run(self):
        # pass_count = []
        # fail_count = []
        res = None
        # 数据库中获取案例，写至表格中
        self.DBCASE.create_excel()
        # 获取需执行案例总数量
        rows_count = self.data.get_case_lines()
        # book = xlrd.open_workbook(filename=self.excelpath, formatting_info=True).sheet_by_index(0)
        # # 将上次的执行结果清除
        # for i in range(1, rows_count):
        #     self.opexcel.write_value(i, 13, "")
        #     self.opexcel.write_value(i, 16, "")
        # del book
        # print("清除原测试结果数据")
        # 排除表头，从-1开始
        for i in range(1, rows_count):
            caseid = self.data.get_case_id(i)
            url = self.data.get_url(i)
            functionname = self.data.get_functionname(i)
            web_admin = self.data.get_web_admin(i)
            method = self.data.get_method(i)
            isrun = self.data.get_is_run(i)
            data = self.data.get_data_json(i)
            file = self.data.get_files(i)
            return_value = self.data.get_return_value(i)
            # 若url为拼接方式
            if "+" in url:
            #     则获取到拼接参数
                url_data = self.de_data.depend_data(i)
                # print("表格里数据",url,url_data)
                url = url.split("+")[0]+str(url_data)
                # print("拼接后",url,type(url_data),type(str(url_data)))
            if file:
                files = {"logo1": ("aa.jpg", open(file, "rb"), "image/jpeg")}
            else:
                files = None
            # cookies = self.data.get_cookies(i)
            expect = self.data.get_expect(i)
            webexpect = self.data.get_web_expectvalu(i)
            depen_case = self.data.get_case_depen(i)
            depend_data = self.de_data.depend_data(i)
            # print("*****第",i,"个",data,depen_data,depen_filed)
            # 查看运行状态是否运行
            # 判断是否是后台案例
            if isrun and web_admin ==0:
                # 首先获取cookie,请求代入cookies
                cookies = self.admin_cookies()
            # 执行案例
                self.caserun.case_run(caseid,rows_count, depen_case,depend_data,url, method, data, cookies, expect, i, webexpect, functionname, files,return_value)
            # 判断是否是学生端案例
            elif isrun and web_admin ==1:
                cookies = self.student_cookies()
                self.caserun.case_run(caseid,rows_count,depen_case,depend_data,url, method, data,cookies, expect, i,webexpect,functionname,files,return_value)
            # 判断是否是教师端案例
            elif isrun and web_admin ==2:
                cookies = self.teacher_cookies()
                self.caserun.case_run(caseid,rows_count,depen_case,depend_data,url, method, data,cookies, expect, i,webexpect,functionname,files,return_value)
if __name__ =='__main__':
    # 案例表格、数据文件路径
    # case_excelpath = "..//Test_Case//Paper_Process.xls"
    # data_jsonpath="../data/Paper_Process.json"
    # 定义报告文件
    excel_copy = "..//Test_Case//Paper_Process_bk.xls"
    html_path = "../Test_Case/Report.html"
    a = Run_case()
    c = a.go_run()
    # 生成报告
    run_html = report(new_filename= excel_copy,report_path= html_path)
    run_html.creat_report()
    # 报告中追加测试数据总计
    add_report = Case()
    add_report.add_html()