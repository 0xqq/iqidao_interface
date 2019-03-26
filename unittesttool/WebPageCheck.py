# coding=utf-8
from unittesttool import Get_cookies
import requests
from bs4 import BeautifulSoup
from unittesttool.Get_data import Getdata
# 界面返回数据校验
class PageCheck:
    def __init__(self,division= None,classname = None):
        # 若传参:属性标签以及数据排序方式
        if division and classname:
            self.division = division
            self.classname = classname
        #不传参，默认表格数据，div,x-scroll
        else:
            self.division = "div"
            self.classname = "x-scroll"
        self.data = Getdata()
        self.cookies = Get_cookies.Get_cookies(2)
        self.cookies= self.cookies.get_cookies_admin()
    # 在界面中获取到所有指定属性的数据
    def get_allparam(self,html,actualvalue):
        soup = BeautifulSoup(html, "html.parser")
        a = []
        # 结合业务，界面数据均是在列表中
        # 若是按照创建时间倒序排序，则获取当前第二列数据
        try:
            for tag in soup.find_all('div', class_='x-scroll'):
                # print("*****", tag)
                data = tag.find_all('tr')
                # data = data.next_sibling
                # print("======",data,type(data))
                # 初始化返回至
                flag = True
                flag_b = True
                for i in actualvalue:
                    if i in str(data):
                        flag_b = True
                    else:
                        flag_b = False
                    flag = flag_b and flag
                return flag
        except Exception as e:
            print("找不到界面预期结果",e)
    # 获取页面html信息
    def getHtml(self,url,actualvalue):
        # 获取登录cookies
        page = requests.get(url, cookies=self.cookies,verify = False)
        # 页面转换为html格式输出
        html = page.text
        # 返回比较结果
        return self.get_allparam(html,actualvalue)
    def case_param(self,i,url):
        #testcase表格界面期望数据整理
        #获取表格数据
        actualvalue =self.data.get_web_expectvalu(i)
        #分号分隔字符串放置在辅助数组
        arr = []
        for k in range(len(actualvalue.split(";"))):
            arr.append(actualvalue.split(";")[k])
        return self.getHtml(url,arr)
# a = PageCheck()
# print(a.case_param(3,"http://testing.iqidao.com/admin001/activity/users?activityId=740"))