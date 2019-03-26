# coding=utf-8
# 获取依赖数据，数据来源两种方式：
# 1.直接获取依赖案例的请求参数，将该参数字典作为数据依赖值进行再次发出请求检查
# 2.通过select查询数据库，查询关键字段的值，与该案例的请求参数结合为一个完整的请求参数，发出请求
# 3.depemd[......]在返回值保存表格中获取字段值
# 此py文件是获取到的依赖数据，与依赖数据所属字段进行相结合
from unittesttool.Get_data import Getdata
from unittesttool.Operation_excel import oper_excel
import unittesttool.Data_config
class dependata:
    def __init__(self,excelpath= None,jsonpath=None):
        if excelpath:
            self.excelpath = excelpath
        else:
            self.excelpath = '../Test_Case/TestCase.xls'
        if jsonpath:
            self.jsonpath = jsonpath
        else:
            self.jsonpath='..//data//Tc_alldata.json'
        self.get = Getdata(self.excelpath,self.jsonpath)
        self.operation_excel = oper_excel(self.excelpath)
    def depend_data(self,i):
        # 判断依赖数据值的获取方式：select?depend[]?请求数据？
        col = int(unittesttool.Data_config.get_data_depend())
        data = self.operation_excel.get_cell_value(i, col)
        # 获取依赖数据的值以及其所属字段
        depen_data = self.get.get_data_depen(i)
        depen_filed = self.get.get_filed_depen(i)
        # 获取请求参数
        request_data = self.get.get_data_json(i)
        #     若是查询数据库，则直接取出列表中的字典与请求参数合并
        if data.startswith("select") or data.startswith("SELECT") or data.startswith("Select"):
            # 若是所属字段为No,则不需要合并，反之为None或有值则需要合并
            try:
                if depen_filed == "No":
                    return list(depen_data[0].values())[0]
            # 若存在数请求数据，则将请求数据与依赖数据合并作为请求数据发送
                for i in range(len(depen_data)):
                    # 若请求参数不是空，则合并
                    if request_data is not None:
                        # return dict(data.items()+depen_data[0].items())
                        # return dict(request_data, **depen_data[0])
                        data_combin = request_data.copy()
                        data_combin.update(depen_data[i])
                        return data_combin
                    # 反之，则直接返回依赖数据作为请求参数
                    return depen_data[0]
            except Exception as e:
                print("请确认数据库查询依赖值是否存在,depen_data=",depen_data,"request_data=",request_data)
        elif data.startswith("depend["):
        #若是从depend表格中获取，则将依赖数据的值与所属字段相合并组成字典，且与请求参数合并
            #拆分依赖数据值，与所属字段相结合
            depend_split =list(depen_data.values())[0]
            depend_dict = {}
            depend_dict[depen_filed] = depend_split
            if depen_filed == "No":
                return list(depend_dict.values())[0]
        # print("组合后所属字段",depend_dict)
            # 若请求参数不是空，则合并
            if request_data is not None:
                data_combin = request_data.copy()
                data_combin.update(depend_dict)
                return data_combin
            # 反之，则直接返回依赖数据作为请求参数
            return depend_dict
        else:
            # 若是从直接给出值，则直接进行两次合并即可
            depend_dict = {}
            depend_dict[depen_filed] = depen_data
            # print("oper+depen**",request_data)
            if request_data is not None:
                data_combin = request_data.copy()
                data_combin.update(depend_dict)
                return data_combin
                # 反之，则直接返回依赖数据作为请求参数
            return depend_dict


# a = dependata(excelpath= "..//Test_Case//Paper_Process.xls", jsonpath="C:/Iqidao_all/data/Paper_Process.json")
# a = dependata(excelpath= "..//Test_Case//TestCase.xls", jsonpath="C:/Iqidao_all/data/Tc_alldata.json")
# print("最后",a.depend_data(7))

