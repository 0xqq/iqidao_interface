# coding=utf-8

import requests
from unittesttool.Requestdemo import inter
from unittesttool.Get_data import Getdata
from unittesttool.Expect_IsEqual import isequal
from unittesttool.Operation_excel import oper_excel
from unittesttool.Send_email import sendmail
from unittesttool.WebPageCheck import PageCheck
from unittesttool.Oper_depend_data import dependata
import os
class Case():
    # class执行前执行，且一个class只执行一次
    # @classmethod
    # def setupClass(cls):
    #     print('class执行前执行')
    # # 每个方法执行前执行一次
    # def setUp(self):
    #     print('test前执行')
    def __init__(self,txt_path = None,report_path= None,excelpath = None,jsonpath = None):
        if report_path:
            self.report_path = report_path
        else:
            self.report_path = "../Test_Case/Report.html"
        if txt_path:
            self.txt_path = txt_path
        else:
            self.txt_path = "../Test_Case/Result.txt"
        if jsonpath:
            self.jsonpath = jsonpath
        else:
            self.jsonpath = "../Test_Case/TestCase.xls"
        self.run_method = inter()
        self.data = Getdata(excelpath=excelpath,jsonfilepath=jsonpath)
        self.result = isequal()
        self.opexcel = oper_excel(filename=excelpath)
        self.sendmail = sendmail()
        self.page_check = PageCheck()
        self.de_data = dependata(excelpath=excelpath,jsonpath=jsonpath)
        self.pass_total = []
        self.fail_total = []
    def case_run(self,caseid,rows_count,depen_case,depend_data,url, method, data,cookies, expect, i,webexpect,functionname,files,return_value):
        # 若不存在数据依赖
        if depen_case ==None:
        # 获取接口请求的返回结果和重定向url
            res,direct_url = self.run_method.run_main(url=url, method=method, data=data,files=files, cookies = cookies,return_value= return_value)
        # 若存在数据依赖
        else:
        #     #获取到依赖数据的值:sql查询或直接数值或从表格中获取，与请求参数合并
        #     print("拼接款******",depend_data,url,method,return_value)
            res, direct_url = self.run_method.run_main(url, method, data=depend_data, files=files, cookies=cookies,return_value=return_value)
        # 检查预期结果:接口响应数据或数据库比对结果
        if self.result.isequalstring(expect, res, i):
            # 若比对结果通过，继续进行界面期望值比较，有则比较，无责直接记录通过
            if webexpect:
                if self.page_check.case_param(i, url=direct_url):
                    self.opexcel.write_value(i, 16, 'Pass')
                    self.opexcel.write_value(i, 13, 'Pass')
                    print("案例id", caseid, functionname, "测试通过")
                    self.pass_total.append(i)
                else:
                    self.opexcel.write_value(i, 16, 'Fail')
                    self.opexcel.write_value(i, 13, 'Pass')
                    print("案例id", caseid, functionname, "测试失败--界面预期值比较失败")
            else:
                #没有界面比较，只需比较响应结果或数据库，则比较成功
                self.opexcel.write_value(i, 13, 'Pass')
                print("案例id", caseid, functionname, "测试通过-预期值校验通过，无界面预期值进行比较")
                self.pass_total.append(caseid)
        else:
            print("案例id", caseid,functionname, "测试失败")
            # 将返回格式转换为字符串写入excel
            self.opexcel.write_value(i, 13, str(res))
            self.fail_total.append(caseid)
        # self.sendmail.send_main(self.pass_total, self.fail_total)
        # # 将测试结果写入txt文件
        f = open(self.txt_path, "w+")
        pass_num = len(self.pass_total)
        fail = len(self.fail_total)
        # f.write("执行案例总数量-Total"+ str(total)+'\n')
        f.write("执行成功案例数量-Pass共有：" + str(pass_num) + "条，案例id分别是" + str(self.pass_total) + '\n', )
        f.write("执行失败案例数量-Fail共有：" + str(fail) + "条，案例id分别是" + str(self.fail_total) + '\n')
    def add_html(self):
        #读取txt文件
        txt_file = open(self.txt_path, "r")
        result = []
        if os.path.getsize(self.txt_path) != 0:
            for i in txt_file:
                result.append(i)
            txt_file.close()
            # # 将测试结果写入txt文件
            # 向html报告中添加测试总结数据
            report = open(self.report_path)
            line = []
            for i in report.readlines():
                line.append(i)
            report.close()
            line.insert(7,
                        '<p>\n <a href="report %s .html" rel="external nofollow" target="_blank">test %s</a>\n</p>\n ' % (
                            result[0], result[0]))
            line.insert(8,
                        '<p>\n <a href="report %s .html" rel="external nofollow" target="_blank">test %s</a>\n</p>\n ' % (
                            result[1], result[1]))
            s = ''.join(line)
            reportnew = open("../Test_Case/Report.html", 'w')
            reportnew.write(s)
            reportnew.close()
            #删除多余文件
            os.remove(self.txt_path)
