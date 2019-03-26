# -*- coding: utf-8 -*-
# 案例运行完毕后，执行此文件，将本次新增数据全部删除
from unittesttool.DB_CONNECT import DB_CONNECT
def delactivitydata():
    cursor,connect = DB_CONNECT(1).connect_db()
    activityname = "活动-0313"
    seasonname="接口测试创建赛季0313"
    delete_activity ="SELECT id FROM Activity WHERE NAME = %s ORDER BY ct ASC LIMIT 1"
    delete_season = "SELECT id  FROM ActivitySeason WHERE activityid = %S  AND NAME = %s ORDER BY ct DESC LIMIT 1"
    try:
        cursor.execute(delete_activity,activityname)
        activityid= cursor.fetchall()[0].get("id")
        # cursor.execute(delete_season,activityid,seasonname)
        # seasonid= cursor.fetchall()[0].get("id")
        print("所删除的数据来源于活动：",activityid)
    except Exception as e:
        print("查询活动id,sql执行有误.", e)
    # 执行删除
    del_QuizUser="delete from QuizUser where paperid in (SELECT id from Paper where activityid =%s)"
    del_QuizMistake="delete from QuizMistake  where paperid in (SELECT id from Paper where activityid =%s)"
    del_PaperUser="delete FROM PaperUser where paperId in (SELECT id from Paper where activityid =%s)"
    del_PaperQuiz="delete from PaperQuiz where paperId in (SELECT id from Paper where activityid =%s)"
    del_Paper="delete from Paper where activityid =%s"
    del_ActivityGroupUser="delete FROM ActivityGroupUser where activityid =%s"
    del_ActivityGroup="delete FROM ActivityGroup where activityid =%s"
    del_ActivityComboRel="delete from ActivityComboRel where activityid =%s"
    del_ActivitySeasonUser="delete from ActivitySeasonUser where activityid =%s"
    del_ActivityItem="delete from ActivityItem  where activityid = %s "
    del_ActivityItemUser="delete from ActivityItemUser where activityid= %s "
    del_ActivitySeason="delete from ActivitySeason  where activityid =%s"
    del_Activity="delete from Activity  where id =%s"
    # 执行
    try:
        print("开始执行删除")
        cursor.execute(del_QuizUser,activityid)
        cursor.execute(del_QuizMistake,activityid)
        cursor.execute(del_PaperUser, activityid)
        cursor.execute(del_PaperQuiz, activityid)
        cursor.execute(del_ActivityItemUser,activityid)
        cursor.execute(del_ActivityItem, activityid)
        cursor.execute(del_Paper, activityid)
        cursor.execute(del_ActivityGroupUser, activityid)
        cursor.execute(del_ActivityGroup, activityid)
        cursor.execute(del_ActivityComboRel, activityid)
        cursor.execute(del_ActivitySeasonUser, activityid)
        cursor.execute(del_ActivitySeason, activityid)
        cursor.execute(del_Activity, activityid)
    except Exception as e:
        print("sql执行有误",e)
    else:
        connect.commit()
        connect.close()
        print("执行结束，执行成功")
def delhomework():
    # 查找作业题试卷id
    papername="0313作业试卷"
    selectpaper="SELECT * from Paper WHERE name=%s"
    cursor, connect = DB_CONNECT(1).connect_db()
    try:
        cursor.execute(selectpaper,papername)
        paperid = cursor.fetchall()[0].get("id")
        print("所删除的数据来源于活动：",paperid)
    except Exception as e:
        print("查询活动id,sql执行有误.", e)
    del_QuizUser = "delete from QuizUser where paperid=%s"
    del_QuizMistake = "delete from QuizMistake  where paperid  =%s"
    del_PaperUser = "delete FROM PaperUser where paperId  =%s"
    del_PaperQuiz = "delete from PaperQuiz where paperId =%s"
    del_Paper = "delete from Paper where id =%s"
    del_PaperAssignment="delete from PaperAssignment where paperId =%s"
    del_PaperAssignmentConfig="delete from PaperAssignmentConfig where paperId =%s"
    del_QuizUserMoral="delete from QuizUserMoral where paperid=%s"
    del_PaperUserMoralScoreItem="delete from PaperUserMoralScoreItem where paperid=%s"
    # 执行
    try:
        print("开始执行删除")
        cursor.execute(del_QuizUser, paperid)
        cursor.execute(del_QuizMistake, paperid)
        cursor.execute(del_PaperUser, paperid)
        cursor.execute(del_PaperQuiz, paperid)
        cursor.execute(del_Paper, paperid)
        cursor.execute(del_PaperAssignment, paperid)
        cursor.execute(del_PaperAssignmentConfig, paperid)
        cursor.execute(del_QuizUserMoral, paperid)
        cursor.execute(del_PaperUserMoralScoreItem, paperid)
    except Exception as e:
        print("sql执行有误", e)
    else:
        connect.commit()
        connect.close()
        print("执行结束，执行成功")
if __name__=='__main__':
    delactivitydata()
    delhomework()