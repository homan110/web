# coding = utf-8
import os
import time
import unittest

from HTMLTestRunner import HTMLTestRunner

from waptest.androidConfig.appConfig import Config
from waptest.pages.loginPage import LoginPage
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Login(unittest.TestCase):
    ''' 登录测试 '''
    def test(self):
        ''' 登录通行证'''
        print("kaishi")

        driver = Config.driver
        login = LoginPage(driver)

        login.click_login_btn()
        phoneNum = 17112340000
        password = 123123

        login.input_login_text(phoneNum, password)
        login.click_login()

        time.sleep(5)
        login.click_login_btn()
        print("登陆成功：" + login.show_usercentertitle_bar())
        time.sleep(5)

        driver.quit()


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    smtp = smtplib.SMTP_SSL()
    smtp.connect("smtp.qq.com", 465)
    smtp.login("39225102@qq.com", "fmtnopnboeohbhbd")
    smtp.sendmail("39225102@qq.com", "115258938@qq.com", msg.as_string())
    smtp.quit()
    print("email has send out !")


def new_report(testcase):
    lists = os.listdir(testcase)
    lists.sort(key=lambda fn: os.path.getmtime(testcase + "\\" + fn))
    file_new = os.path.join(testcase, lists[-1])
    print(file_new)
    return file_new


if __name__ == "__main__":

    test_report = "E:\\homan\\wap测试脚本\\waptest\\testcase\\report"
    testunit = unittest.TestSuite()
    testunit.addTest(Login('test'))
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = test_report + "\\" + now + "result.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(testunit)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)