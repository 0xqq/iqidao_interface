
# -*- coding:utf-8 -*-
# @Date    : 2016-07-13 14:47:56
# @Function: 把Excel表单转化为json文件
# @Author  : JennyZhang

import xlrd
import json
import codecs

# 获取excel数据源
def get_data(file_path,file):
    """获取excel数据源"""
    try:
        data = xlrd.open_workbook(file_path+'\\'+file)
        return data
    except Exception as e:
        print(u'excel表格读取失败：%s' % e)
        return None


# 把excel表格中指定sheet转为json
def Excel2Json(file_path,file,params_name,json_name):
    # 打开excel文件
    if get_data(file_path,file) is not None:
        book = get_data(file_path,file)
        # 抓取所有sheet页的名称
        worksheets = book.sheet_names()
        print("该Excel包含的表单列表为：\n")
        for sheet in worksheets:
            print ('%s,%s' %(worksheets.index(sheet), sheet))
        inp = input(u'请输入表单名对应的编号，对应表单将自动转为json:\n')
        print("----inp",inp)
        sheet = book.sheet_by_index(int(inp))
        print("-------",sheet)
        row_0 = sheet.row(0)
        # 第一行是表单标题
        print("rooooo",row_0)
        nrows = sheet.nrows  # 行号
        print("ooo",nrows)
        ncols = sheet.ncols  # 列号

        result = {}  # 定义json对象
        print("-----",result)
        result["title"] = file_path  # 表单标题
        result["rows"] = nrows  # 行号
        result[params_name] = []  # 每一行作为数组的一项
        # 遍历所有行，将excel转化为json对象
        for i in range(nrows):
            if i == 0:
                continue
            tmp = {}
            # 遍历当前行所有列

            for j in range(ncols):
                # 获取当前列中文标题
                # title_de = str(row_0[j]).decode('unicode_escape')
                title_de = str(row_0[j])
                title_cn = title_de.split("'")[1]
                # 获取单元格的值
                # print("--------",type(sheet.row_values(i)[j]),sheet.row_values(i)[j])
                if type(sheet.row_values(i)[j])==float:
                    tmp[title_cn] = int(sheet.row_values(i)[j])
                else:
                    tmp[title_cn] = sheet.row_values(i)[j]
            result[params_name].append(tmp)
            # print("res",result)
        json_data = json.dumps(result, indent=4, sort_keys=True,ensure_ascii=False)
        # json_data = json.dumps(result, indent=4, sort_keys=True).decode('unicode_escape')
        # print(json_data)
        file = open(file_path+"//"+json_name+".json", 'w')
        with open(file_path+"//"+json_name+".json", "w") as f:
            file.write(json_data)
        return json_data



def saveFile(file_path, file_name, data):
    output = codecs.open(file_path + "/" + file_name + ".json", 'w', "utf-8")
    print("shengcengwenjian",file_name)
    output.write(data)
    output.close()



if __name__ == '__main__':
    file_path = "..//data"
    file = input(u'请输入excel文件名称(包含后缀)：\n')
    params_name= file.split(".")[0]
    json_name = file.split(".")[0]
    json_data = Excel2Json(file_path,file,params_name,json_name)
        # json.dump(json_data, f)
    # print("json+data-----",json_data)
    # file = open("..//data//json22.json", 'w')
    # with open("..//data//json22.json", "w") as f:
    #     file.write(json_data)
    print("加载入文件完成...")
