# coding=utf-8
import requests


def setcookies():
    data2 = {
        'phone': '186186',
        'password': '111111',
        'captcha': '666666'
    }
    r1 = requests.post("https://testing.iqidao.com/admin001/signin", verify=False, data=data2)
    cookies1 = r1.cookies
    return cookies1


def setcookies_web():
    data2 = {
        'key': 90000000019,
        # 'key': 13811469892,
        'password': '111111',
        'captcha': '666666',
        "rememberMe": 1
    }
    r1 = requests.post("https://testing.iqidao.com/json/user/signin", verify=False, data=data2)
    print(r1.text)
    cookies1 = r1.cookies
    return cookies1
coo = setcookies()
# coo = setcookies_web()
print("coo:", coo)
# url = "https://testing.iqidao.com/admin001/combo/create"
# requests.post(url=url,data = data1,verify = False,cookies = coo)
urlget = "https://testing.iqidao.com/json/kidgame/new"
urlget_1 = "https://testing.iqidao.com/kidgame/:id"
url_start = "https://testing.iqidao.com/json/kidgame/start"
url_end = "https://testing.iqidao.com/json/kidgame/finish"
para = {
    "activityId": 338,
    "seasonId": 950
}
para1 = {
    "id": 2
}
para2 = {
    "id": 3,
    "result": "1",
    "resultDescription": "1",
    "aiWin": "0",
    "sgf": "(;CA[gb2312]SZ[13]AP[MultiGo:4.4.4]MULTIGOGM[1];B[gf];W[hf];B[hg];W[gg];B[aa])",
    "timeSpend": "15"
}
activitystatus_edit = {
    "ComboEndTime": 0,
    "ComboStartTime": 0,
    "id": 855,
    "name": "启蒙活动-测试数据",
    "teacherId": 18133,
    "category": 1,
    "status": 1,
    "polyvVideoId": "",
    "quarter": "",
    "signupStartTime": "2018-12-19 11:04",
    "signupEndTime": "2019-01-06 11:03",
    "startTime": "2018-12-19 11:04",
    "endTime": "2019-12-06 11:03",
    "userLimit": 100,
    "remainder": 99,
    "type": 2,
    "price": 200.00,
    "signupCount": 1,
    "lowerDuan": -2,
    "upperDuan": -2,
    "activityVersion": 2,
    "logo1": "",
    "wxGroupQr": "",
    "enableGame": "true",
    "description": "<p>启蒙活动-测试数据</p>"
}
mod_game = {
    "score":"-25",
    "result":"2",
    "uid":18652,
    "gameid":5
}
a = {
}
mod_game_url = "https://testing.iqidao.com/json/kidgame/modify"
edit_url = "https://testing.iqidao.com/admin001/activity/edit"
list_url = "https://testing.iqidao.com/json/kidgame_histories"
teacher_kidgame = "https://testing.iqidao.com/student_kidgames"
teacher_kid= {
    "gameId":"",
    "uid":"",
    "startTime":"",
    "endTime":"",
    "activityId":"",
    "seasonId":"",
    "result":"",
    "aiWin":""
}
id = {
    "":"18"
}
# 修改活动
ac_id = {
    "id":856
}
ac_url= "https://testing.iqidao.com/admin001/activity/edit"
# requests.get(url =ac_url,params=ac_id, verify=False, cookies=coo)
# ac_mod_ost = requests.post(url = ac_url,data= activitystatus_edit,verify=False, cookies=coo,files= None)
# 棋谱下载
# r1 = requests.get(url=sgf_url,params = sgf,verify = False,cookies = coo)
#学生信息
# # r2 = requests.get(url = student_url,verify=False, cookies=coo)
# # 棋谱详情页
# r3 = requests.get(url = detail_url,verify=False, cookies=coo)
# # 教师端棋谱页
# # r4 =requests.get(url =teacher_kidgame,params=teacher_kid, verify=False, cookies=coo)
# print("返回响应", r3.text, r3.status_code)
#
# 学生换班
url = "https://testing.iqidao.com/admin001/order/switch/add"
data = {
    "uid": 646,
    "srcActivityId": 724,
    "srcSeasonIds": 801,
    "dstActivityId": 722,
    "dstSeasonIds": 874,
}
# switch_user = requests.post(url = url,data= data,verify=False, cookies=coo)

# 修改试题
mod_quizurl="https://testing.iqidao.com/admin001/quiz/put"
mod_data={
    "id":66470,
    "name":"test",
    "category":2,
    "smFiled":"",
    "classes":"3",
    "duan":0,
    "resultType":0,
    "aim":1,
    "type":4,
    "whoPlay":1,
    "idaun":0,
    "vid": ""
}
files = {"file": ("u=2856000109,3701537385&fm=27&gp=0.jpg", open("C://爱棋道测试文件-棋//试题//死活sgf//1D1.sgf", "rb"), "image/jpeg", {})}
# mod_quiz = requests.post(url = mod_quizurl,data= mod_data,verify=False, cookies=coo,files= files)
# print(mod_quiz)
uril_paperassign = "https://testing.iqidao.com/papers_t/cast/add"
data_assign =  {
            "activityId": 814,
            "candotime": "2019-01-21 17:52",
            "paperId": 141373,
            "seasonId": 957
        }
# paper_assign = requests.post(url = uril_paperassign,data= data_assign,verify=False, cookies=coo)
# 添加活动
creat_activity_url ="https://testing.iqidao.com/admin001/activity/create"
creat_activity={
    "name": "启蒙活动-测试数据",
    "teacherId": 18133,
    "category": 1,
    "quarter": "",
    "signupStartTime": "2019-01-29 10:30",
    "signupEndTime": "2019-01-31 10:30",
    "startTime": "2019-01-29 10:30",
    "endTime": "2019-01-31 10:30",
    "userLimit": 100,
    "type": 7,
    "price": 200.00,
    "signupCount": 1,
    "lowerDuan": -2,
    "upperDuan": -2,
    "activityVersion": 2,
    "enableGame": "true",
    "description": "<p>启蒙活动-测试数据</p>"
	# "name":"活动999",
	# "type":2,
	# "category":"",
	# "signupCount":0,
	# "lowerduan":-2,
	# "upperduan":-2,
	# "price":0,
	# "userLimit":100,
	# "teacherId":18133,
	# "signupStartTime":"2019-01-09 16:54",
	# "signupEndTime":"2019-02-10 16:54",
	# "startTime":"2019-01-30 16:55",
	# "endTime":"2019-02-10 16:54",
	# "quarter":"",
	# "activityVersion":"2",
	# "description":"活动"
}
create = {
"name":"123",
"type":2,
"category":"",
"signupCount":0,
"lowerduan":-2,
"upperduan":-2,
"price":1000.00,
"userLimit":"1000",
"teacherId":206,
"signupStartTime":"2019-01-31 10:30",
"signupEndTime":"2019-02-10 10:29",
"startTime":"2019-01-31 10:30",
"endTime":"2019-02-09 10:29",
"quarter":"",
"activityVersion":2,
"description":"12333"
}
filepath = "C:/Users/zhangjy/Pictures/aa.jpg"
files1 = {"logo1": ("aa.jpg",open(filepath ,"rb"), "image/jpeg")}
print(type(files))
# creat_activity_post = requests.post(url = creat_activity_url,data= creat_activity,verify=False, cookies=coo,files = files1)
# 添加条目
add_ietam_url ="https://testing.iqidao.com/admin001/activity/item"
add_ietam ={
	"activityId":830,
	"seasonId":979,
	"name":"课堂条目-0130",
	"startTime":"2019-01-30 14:11",
	"type":0,
	"duration":45,
	"GameCount":"",
	"GameDuan":"",
	"GameRuleId":""
}
data22 = {
    "key" : "活动-0225",

}
r =  requests.get(url = "https://testing.iqidao.com/admin001/json/select2/activity",params=data22,verify=False, cookies=coo)
#添加预习题
add_pre_paperurl="https://testing.iqidao.com/admin001/paper/quiz"
add_pre_paper={
	"paperId":141469,
	"quizId":65792
}
# add_pre_paperrepost=requests.post(url = add_pre_paperurl,data= add_pre_paper,verify=False, cookies=coo)
# # 进入条目
# iteam_id = "10500"
# item_open_url= "https://testing.iqidao.com/trainingitem/"+iteam_id
# item_open_get = requests.get(url = item_open_url,verify=False, cookies=coo)
# #打开试卷
# open_paper_url= "https://testing.iqidao.com/json/paper/open"
# open_paper= {
#     "paperId":141463
# }
# paper_open_post = requests.post(url = open_paper_url,data= open_paper,verify=False, cookies=coo)
# #答题
# answer_paper_url ="https://testing.iqidao.com/json/paper/quiz"
# answer_paper_1= {
#     "paperId": 141463,
#     "quizId": 64775,
#     "answer": "A"
# }
# answer_paper_2= {
#     "paperId": 141463,
#     "quizId": 64777,
#     "answer": "A"
# }
# answer_paper_3= {
#     "paperId": 141463,
#     "quizId": 64778,
#     "answer": "A"
# }
# answer_paper_4= {
#     "paperId": 141463,
#     "quizId": 64779,
#     "answer": "A"
# }
# answer_paper_5= {
#     "paperId": 141463,
#     "quizId": 65550,
#     "answer": "B"
# }
# answer_paper_post_1 = requests.post(url = answer_paper_url,data= answer_paper_1,verify=False, cookies=coo)
# answer_paper_post_2 = requests.post(url = answer_paper_url,data= answer_paper_2,verify=False, cookies=coo)
# answer_paper_post_3 = requests.post(url = answer_paper_url,data= answer_paper_3,verify=False, cookies=coo)
# answer_paper_post_4 = requests.post(url = answer_paper_url,data= answer_paper_4,verify=False, cookies=coo)
# answer_paper_post_5 = requests.post(url = answer_paper_url,data= answer_paper_5,verify=False, cookies=coo)
#
#交卷
commit_paperurl = "https://testing.iqidao.com/json/paper/commit"
commit_paper={
    "paperId": 141463
}
# commit_paper_post = requests.post(url = commit_paperurl,data= commit_paper,verify=False, cookies=coo)
paperurl = "https://testing.iqidao.com/json/paper/score"
paper={
    "paperId": 141441
}
# paperurl_post = requests.get(url = paperurl,params= paper,verify=False, cookies=coo)
# 教师查看阅卷
teacher_view_url = "https://testing.iqidao.com/student_papers"


teacher_view= {
    "paperName": "课堂条目-接口测试预习题",
    "status": -1,
    "reviewed": -1,
    "src": -1,
    "student":"",
    "sortName":"",
    "sortType":"",
    "si":0,
    "partial": 1,
    "returnType": 1,

}
# teacher_view_get = requests.get(url = teacher_view_url,params= teacher_view,verify=False, cookies=coo)
# print(teacher_view_get.text)
papers_url = "https://testing.iqidao.com/admin001/papers"
paper_data = {
    "returnType":1,
    "name":"期末",
    # "type":"",
    # "startTime":"",
    # "partial":1
}

# papers_url_get = requests.get(url = papers_url,params= paper_data,verify=False, cookies=coo)
paper_score_student= "https://testing.iqidao.com/json/paper/score"
paper_score= {
    "paperId":141488
}
# paper_score_post = requests.get(url = paper_score_student,params= paper_score,verify=False, cookies=coo)
get_url = "https://testing.iqidao.com/trainingitem/10520"
# iteam_get = requests.get(url = get_url,verify=False, cookies=coo)
#添加分组
groupurl = "https://testing.iqidao.com/admin001/grade/group/add"
groupdata= {
    "activityId":883,
    "type":2,
    "seasonId":1033,
    "name":"分组1",
    "teacherId":18133
}
# group_add = requests.post(url = groupurl,data= groupdata,verify=False, cookies=coo)
# 学生分组
assign_group_url = "https://testing.iqidao.com/admin001/grade/group/user/update"
assign_group = {
    "uid":39351,
    "uid":39352,
    "uid":18213,
    "groupId":1062
}
# assig_group_post = requests.post(url = assign_group_url,data= assign_group,verify=False, cookies=coo)
# 添加续报组合关联
add_url = "https://testing.iqidao.com/admin001/activity/combo_manage/addcombo"
add_data = {
    "ActivityId2":883,
    "activityComboId":2
}
# add_post = requests.post(url = add_url,data= add_data,verify=False, cookies=coo)
# 设置续报组合显示时间
display_url ="https://testing.iqidao.com/admin001/add/displaytime"
display_data = {
    "ActivityId":883,
    "startTime":"2019-03-13 11:22",
    "endTime":"2019-04-05 11:22"
}
# display_post = requests.post(url = display_url,data= display_data,verify=False, cookies=coo)
# 发放代金券
ti_url = "https://testing.iqidao.com/admin001/coupon/user/add"
us_data = {
    "uid":39351,
    "price":"99.99",
    "status":0,
    "startTime":"2019-03-13 11:22",
    "endTime":"2019-03-30 11:37"
}
# us_post = requests.post(url = ti_url,data= us_data,verify=False, cookies=coo)
# 添加专属代金券
onl_url ="https://testing.iqidao.com/admin001/coupon/basic/add/config"
onl_data = {
    "name":"0303接口发放",
    "limit":100,
    "price":99.99,
    "startTime":"2019-03-13 11:41",
    "endTime":"2019-03-28 11:41",
    "intro":"测试代金券"
}
# onl_post = requests.post(url = onl_url,data= onl_data,verify=False, cookies=coo)
# 代金券添加到专属活动
add_ur = "https://testing.iqidao.com/admin001/coupon/basic/activity/add"
ad_data = {
    "couponId":328,
    "activityId":568
}
# ad_post = requests.post(url = add_ur,data= ad_data,verify=False, cookies=coo)

# 发给指定用户
us_ti_url = "https://testing.iqidao.com/admin001/coupon/basic/user/add"
us_ti_data ={
    "couponId":328,
    "uid":0,
    "limit":1000
}
# us_ti_post = requests.post(url = us_ti_url,data= us_ti_data,verify=False, cookies=coo)

url_moduser="https://testing.iqidao.com/admin001/user/put"
mod_data = {
    "id":39373,
    "realName":"zhagjiya",
    "group":0,
    "phone":13811469896
}
us_mod_post = requests.post(url = url_moduser,data= mod_data,verify=False, cookies=coo)
