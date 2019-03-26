# coding=utf-8
import pymysql
from unittesttool.DB_CONNECT import DB_CONNECT
import json
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
# 导入excel操作包
import xlrd
import xlwt
from xlutils.copy import copy

#取出TestCase.xls中的数据
# 测试文件名大写

class DataBase():
    def __init__(self):
        # 连接数据库
        # connect = pymysql.connect(
        #     host='rm-uf6dus34x3o5s3y02co.mysql.rds.aliyuncs.com',
        #     port=3306,
        #     user='iqidao',
        #     passwd='cGUNif88!Zm1vTW*',
        #     charset='utf8',
        #     db='iqidao2',
        #     # 查询结果转换为数据字典类型
        #     cursorclass=pymysql.cursors.DictCursor
        # )
        # 连接数据库
        cursor = DB_CONNECT(1)
        self.cursor= cursor.connect_db()
    def selectvalue(self,sql):
        # print("密码是什么me",self.data.return_password(1),type(self.data.return_password(1)),type('123456'))
        # 确认存在几条查询语句，分离sql
        sql_separated = sql.split(";")
        len_sql  = len(sql_separated)
        selectresult = {}
        selectresult["result"] = []
        for i in range(len_sql):
            try:
                # 执行sql
                self.cursor.execute(sql_separated[i])
                selectresult["result"].append(self.cursor.fetchone())
            except Exception as e:
                print(e)
        return selectresult["result"]
    def del_value(self,sql):
        sql_separated = sql.split(";")
        len_sql = len(sql_separated)
        for i in range(len_sql):
            try:
                # 执行sql
                self.cursor.execute(sql_separated[i])
                return True
            except Exception as e:
                print(e)
                return False
# a = DataBase()
# # print(sqldata,"sql_______----------")
# c = a.del_value("DELETE from Quiz where id =  25315")
# print(c,type(c))
# c = a.selectvalue("select id,name from Activity where name like '%AI%' limit 1")
# print(len(c),c,type(c))
# c = a.selectvalue(sqldata)
