# -*- coding: utf-8 -*-
from unittesttool.DB_CONNECT import DB_CONNECT

class Case_Table:
    #判断执行哪个表格中的案例
    def __init__(self):
    # 连接数据库
        cursor = DB_CONNECT(2)
        self.cursor,self.connect = cursor.connect_db()
    def get_tablename(self):
    # 获取需要运行的案例的表明
        select_table = "select table_name from Case_Mangement where Run ='Y' order by id asc limit 1"
        try:
            self.cursor.execute(select_table)
            table = self.cursor.fetchall()
        except Exception as  e:
            print("查询业务案例表名sql执行有误",e)
        else:
            print("需要执行的案例表名为",table[0].get("table_name"))
            self.connect.close()
            return table[0].get("table_name")
# a = Case_Table()
# c = a.get_tablename()
# print(c)
