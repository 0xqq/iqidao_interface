# -*- coding: utf-8 -*-

# coding=utf-8
import pymysql
from xlwt import Workbook
from unittesttool.DB_CONNECT import DB_CONNECT
from Get_Case.Case_Table import Case_Table
# pymysql.Connect()参数说明
# host(str):      MySQL服务器地址
# port(int):      MySQL服务器端口号
# user(str):      用户名
# passwd(str):    密码
# db(str):        数据库名称
# charset(str):   连接编码
#
# connection对象支持的方法
# cursor()        使用该连接创建并返回游标
# commit()        提交当前事务
# rollback()      回滚当前事务
# close()         关闭连接
#
# cursor对象支持的方法
# execute(op)     执行一个数据库的查询命令
# fetchone()      取得结果集的下一行
# fetchmany(size) 获取结果集的下几行
# fetchall()      获取结果集中的所有行
# rowcount()      返回数据条数或影响行数
# close()         关闭游标对象
class Get_case():
    def __init__(self):
        # 连接数据库
        # 获取游标
        cursor = DB_CONNECT(2)
        self.cursor,self.connect = cursor.connect_db()
        self.tablename = Case_Table().get_tablename()
        self.caseexcel ="..//Test_Case//"+self.tablename+".xls"
    # 获取需要执行的案例编号
    def is_run(self):
        select_isrun = "select id from\r"+ self.tablename+" Paper_Process where isRun='Y'"
        try:
            self.cursor.execute(select_isrun)
            case_id = self.cursor.fetchall()
            return case_id
        except Exception as e:
            print("sql查询有误",e)
    # 获取执行案例的相关数据
    def get_case_content(self):
        # 读取需要执行的case_id
        case_id = self.is_run()
        caseid_collection= []
        content = []
        for i in range(len(case_id)):
            caseid_collection.append(case_id[i].get("id"))
        select_content = "select * from\r "+self.tablename+" where id = %s"
        for i in range(len(caseid_collection)):
            try:
                self.cursor.execute(select_content,caseid_collection[i])
                # content.append(self.cursor.fetchall())
                content =content+self.cursor.fetchall()
            except Exception as e:
                print("sql查询有误", e)
        return content
    def create_excel(self):
        # 获取表字段名称，且写入在excel表格中的首行
        try:
            sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = %s"
            self.cursor.execute(sql,self.tablename)
        except Exception as  e:
            print("查询",self.tablename,"表的案例详情sql执行有误", e)
        else:
            key_name = self.cursor.fetchall()
            field_names = []
            for i in range(len(key_name)):
                field_names.append(key_name[i].get("COLUMN_NAME"))
            #新建一个案例存储excel表格
            book = Workbook(encoding='utf-8')
            booksheet = book.add_sheet('Sheet 1')
            # 表格填写表头
            for i in range(len(field_names)):
                booksheet.write(0,i,field_names[i])
            # 执行案例的相关数据获取
            content = self.get_case_content()
            # 逐个案例获取
            for i in range(len(content)):
                case_order = content[i]
                for j in range(len(list(case_order.values()))):
                    # 第i行第j列输入
                    booksheet.write(i+1, j,list(case_order.values())[j])
            book.save(self.caseexcel)
# a = Get_case()
# a.create_excel()
