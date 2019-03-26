# coding=utf-8
import json
import datetime
class opreation_json:
    def __init__(self,filepath= None):
        self.data = self.get_json(filepath)
    def get_json(self,filepath):
        if filepath:
            try:
                # 打开文件后且自行关闭
                with open(filepath) as fp:
                    data = json.load(fp)
                    return data
            except Exception as e:
                print(filepath,"文件没有被找到或者文件有错误，无法打开",e)
                return None
        else:
            try:
            # 打开文件后且自行关闭
                with open('..//data//Tc_alldata.json') as fp:
                    data = json.load(fp)
                    return data
            except Exception as e:
                print(filepath,"文件没有被找到或者文件有错误，无法打开",e)
                return None
    def get_data(self, id):
        #根据关键字获取数据
        try:
            json_data = self.data[id]
            # 遍历请求数据字典，若存在时间格式的数据，则获取当前数据进行代替
            for k in json_data:
                if json_data[k]== "Start_Datime_addten":
                    json_data[k] = (datetime.datetime.now()+datetime.timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M")
                elif json_data[k]== "End_time":
                    json_data[k] = (datetime.datetime.now() + datetime.timedelta(days=100)).strftime("%Y-%m-%d %H:%M")
                elif json_data[k] =="Now_Datime":
                    json_data[k] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            return json_data
        except Exception as e:
            print("没有关于",id,"的参数数据")
            return None
# a = opreation_json(filepath="C:/Iqidao_all/data/Paper_Process.json")
# c = a.get_data('teacher_create_paper')
# print(c)
