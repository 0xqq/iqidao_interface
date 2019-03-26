# coding=utf-8
import smtplib
from email.mime.text import MIMEText

class sendmail:
    # global send_user
    # global email_host
    # global password

    def send_mail(self,user_list, sub, content):
        send_user = "xsdgctjy@163.com"
        email_host = "smtp.163.com"
        password = "ff993517"
        user_post = "ZJY"+"<"+send_user+">"
        # 生成邮件格式
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        # 主题、发送人、接收人
        message['Subject'] = sub
        message['From'] = user_post
        message['To'] = ";".join(user_list)
        # 创建smtp服务
        server = smtplib.SMTP()
        server.connect(host=email_host)
        # 邮箱登陆
        server.login(send_user,password)
        # 发送邮件
        server.sendmail(user_post, user_list, message.as_string())
        server.close()
    def send_main(self, pass_count, fail_count):
        user_list = "xsdgctjy@163.com"
        sub = "测试报告"
        pass_num = int(len(pass_count))
        fail_num = int(len(fail_count))
        sum = pass_num + fail_num
        # 输出通过率
        pass_result = "%.2f%%"%(pass_num/sum * 100)
        fail_result = "%.2f%%"%(fail_num/sum * 100)
        content = "运行案例总数%s个，通过个数%s个，分别是%s，失败个数%s个，分别是%s, 失败率%s,通过率%s" % (sum, pass_num, pass_count, fail_num, fail_count, fail_result, pass_result)
        self.send_mail(user_list, sub, content)
if __name__ == '__main__':
    send = sendmail()
    user_list = "xsdgctjy@163.com"
    sub = "测试报告"
    # content = "第一封邮件"
    # send.send_mail(user_list, sub, content)
    send.send_main([1, 2, 3], [4])