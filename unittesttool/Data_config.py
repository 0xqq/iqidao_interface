# coding=utf-8
#取出TestCase.xls中的数据，标注各个字段所在列
# 测试文件名大写
class global_var:
    # caseid
    id = '0'
    function = '1'
    web_admin = '2'
    url = '3'
    is_run = '4'
    requestmethod = '5'
    files = '6'
    return_value = '7'
    case_depend ='8'
    data_depen = '9'
    fileld_depend ='10'
    request_data ='11'
    expect='12'
    result = '13'
    db_value = '14'
    web_expectvalu = '15'
def get_db_value():
    return global_var.db_value
# 获取caseid
def get_caseid():
    return global_var.id
# 获取接口请求属于前端或后端
def get_web_admin():
    return global_var.web_admin
# 获取url
def get_url():
    return global_var.url
def get_functionname():
    return global_var.function
def get_isrun():
    return global_var.is_run
def get_method():
    return global_var.requestmethod
def get_files():
    return global_var.files
def get_case_depend():
    return global_var.case_depend
def get_data_depend():
    return global_var.data_depen
def get_file_depend():
    return global_var.fileld_depend
def get_request_data():
    return global_var.request_data
def get_expect():
    return global_var.expect
def get_return_value():
    return global_var.return_value
def get_web_expectvalu():
    return global_var.web_expectvalu

