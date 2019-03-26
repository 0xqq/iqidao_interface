# coding=utf-8
from unittesttool.DB_Select_return import DataBase
from unittesttool.Get_data import Getdata
import operator
# 接口响应数据或数据库查询结果比较
class isequal:
    # 判断一个字符串是否在另一个字符串中
    # 预期结果与实际结果比较
    def isequalstring(self, expect, result,i):
        # expect是预期结果一栏中数据，若是None则不做比较
        if expect == None:
            print("无预期结果,接口不做比较")
            return True
        # expect是预期结果一栏中数据，若是Select,则执行sql语句
        elif expect.startswith("select"):
            print("select",expect)
            db = DataBase()
            # 执行sql获取返回结果sql_value
            sql_value = db.selectvalue(expect)
            # expect_compare:获取case表格中sql比对结果的值
            ex = Getdata()
            expect_compare = ex.get_db_value(i)
            if sql_value == [None]:
                # print("数据*****", sql_value, type(sql_value),expect_compare)
                if expect_compare == None:
                    print("数据删除成功，数据库无数据")
                    return True
                else:
                    print("数据库数据不存在，请检查")
                    return False
            else:
                try:
                    expect_compare_len = len(expect_compare)
                    sql_value_len = len(sql_value)
                except Exception as e:
                    # print("whywhy",expect_compare,sql_value)
                    print("请检查是否数据库链接错误，没有查到数据",expect_compare,sql_value)
             # sql执行结果与预期比较数据中查找共同字段，且比较值是否相等
            # 借助辅助数组
                compare_dict = {}
                for i in range(len(sql_value)):
                    # print("数据*****",sql_value[i],type(sql_value[i]))
                    for k in sql_value[i]:
                        try:
                            if k in expect_compare:
                        #相同值添加至辅助数组
                                compare_dict[k] = expect_compare.get(k)
                        except Exception as e:
                            print("没有找到expect",expect_compare,"sql_value",sql_value,"coppare_dict",compare_dict)
                # print("数据*****",compare_dict,type(compare_dict),compare_dict,sql_value,sql_value==compare_dict)
            # 辅助数组与sql查询数组比较
                if operator.eq(compare_dict,sql_value[i]):
                #sql查询结果与预期比较结果一致
                    return True
                else:
                    # print("sql查询数据与预期结果不相等",sql_value,"!=",expect_compare)
                    return False
        else:
            # expect是预期结果一栏中数据，若是指定字符，则与请求响应结果比较
            if isinstance(result,dict):
                result = str(result)
                if expect in result:
                    return True
                else:
                    return False
            elif str(result)== expect:
                return True
            return False
# a = isequal()
# # expect = "select activityId,seasonId,uid from ActivitySeasonUser where seasonId =835 ORDER BY id DESC LIMIT 1"
# # result = {
# #             "activityId": 740,
# #             "seasonId": 835,
# #             "uid": 18213
# #         }
# expect = "<Response [302]>"
# result ="<Response [302]>"
# print(a.isequalstring(expect,expect,3))