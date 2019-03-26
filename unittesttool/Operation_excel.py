# coding=utf-8
# 导入excel操作包
import xlrd
from xlutils.copy import copy
import gc
# # 打开excel
# data =  xlrd.open_workbook("C:/Iqidao_all/unittesttool/config.xls")
# # 获取所有sheet的名称
# print(data.sheet_names())
# # 获取sheet,通过下标值获取
# tables = data.sheet_by_index(0)
# # 取sheet,通过名字获取
# tables1 = data.sheet_by_name('Sheet1')
# # 取出sheet的行数,列数
# print(tables.nrows)
# print(tables.ncols)
# # 获取整行数据
# rows = tables.row_values(3) # 获取第四行内容
# cols = tables.col_values(2) # 获取第三列内容
# print(rows,cols)
# # 根据单元格获取数据
# print("第三行第四列，因为下标是从0开始", tables.cell_value(2, 3))
class oper_excel:
    def __init__(self, filename=None, sheet_id=None):
        if filename:
            self.filename = filename
            self.sheet_id = 0
        else:
            self.filename = "../Test_Case/TestCase.xls"
            self.sheet_id = 0
        self.book = xlrd.open_workbook(self.filename, formatting_info=True)
        tables = self.book.sheet_by_index(self.sheet_id)
        # self.data = self.get_excel()
        self.data = tables
    # # 找到文件
    # def get_excel(self):
    #     self.book = xlrd.open_workbook(self.filename,formatting_info=True)
    #     tables = self.book.sheet_by_index(self.sheet_id)
    #     # 返回查找的sheet表名
    #     return tables

    # 获取shetts内容
    # def get_sheets(self):
    # 获取单元格行数
    def get_line(self):
        tables = self.data
        return tables.nrows
        # 获取某一单元格内容

    # 获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols

    def get_cell_value(self, row, col):
        # 获取单元格内容
        data = self.data.cell_value(row, col)
        return data
        # 根据对应的caseid找到对应的行号

    def get_row_num(self, case_id):
        num = 0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num
            num = num + 1

    # 根据caseid获取整行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    # 根据行号，找到该行的内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data
    # def write_value(self, row, col, value):
    #     #     写入excel数据
    #     # 打开excel文件
    #     read_data = xlrd.open_workbook(self.filename)
    #     # 复制文件
    #     write_data = copy(read_data)
    #     # 获取sheet页
    #     sheet_data = write_data.get_sheet(0)
    #     # 单元格写入数据
    #     sheet_data.write(row, col, value)
    #     # 保存文件
    #     write_data.save(self.filename)
    def setOutCell(self, outSheet, col, row, value):
        """ Change cell value without changing formatting. """

        def _getOutCell(outSheet, colIndex, rowIndex):
            """ HACK: Extract the internal xlwt cell representation. """
            row = outSheet._Worksheet__rows.get(rowIndex)
            if not row:
                return None

            cell = row._Row__cells.get(colIndex)
            return cell

        # HACK to retain cell style.
        previousCell = _getOutCell(outSheet, col, row)
        # print("****",previousCell)
        # END HACK, PART I

        outSheet.write(row, col, value)

        # HACK, PART II
        if previousCell:
            newCell = _getOutCell(outSheet, col, row)
            if newCell:
                newCell.xf_idx = previousCell.xf_idx
    def write_value(self, row, col, value):
        # 打开excel文件
        read_data = xlrd.open_workbook(self.filename, formatting_info=True)
        # 复制文件
        write_data = copy(read_data)
        # 获取sheet页
        sheet_data = write_data.get_sheet(0)
        self.setOutCell(sheet_data,col, row, value)
        # 保存文件
        write_data.save(self.filename)
# orer = oper_excel('..//Test_Case//Paper_Process - 副本 (2).xls', 0)
# print(orer.get_line())
# print("获取最开始",orer.get_cell_value(1,1),orer.get_cell_value(2,1))
# del orer
# gc.collect()
# orer = oper_excel('..//Test_Case//test1.xls', 0)
# orer.write_value(1,1,"aaa")
# orer.write_value(0,1,"{'String': '测试代金券', 'Valid': True}")
# print("houlai",orer.get_cell_value(1,1),orer.get_cell_value(2,1))



