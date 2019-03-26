import  os
def add_html():
    # 读取txt文件
    txt_file = open("../Test_Case/Result.txt", "r")
    result = []
    if os.path.getsize("../Test_Case/Result.txt") != 0:
        for i in txt_file:
            result.append(i)
        txt_file.close()
        # # 将测试结果写入txt文件
        # 向html报告中添加测试总结数据
        report = open("../Test_Case/Report.html")
        line = []
        for i in report.readlines():
            line.append(i)
        report.close()
        line.insert(7,
                    '<p>\n <a href="report %s .html" rel="external nofollow" target="_blank">test %s</a>\n</p>\n ' % (
                        result[0], result[0]))
        line.insert(8,
                    '<p>\n <a href="report %s .html" rel="external nofollow" target="_blank">test %s</a>\n</p>\n ' % (
                        result[1], result[1]))
        s = ''.join(line)
        reportnew = open("../Test_Case/Report.html", 'w')
        reportnew.write(s)
        reportnew.close()
        # 删除多余文件
        # os.remove(self.txt_path)
add_html()
