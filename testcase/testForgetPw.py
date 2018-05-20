# coding = utf-8
import unittest
import time
from appium import webdriver
from androidConfig import appConfig
from pages.forgetPwPage import ForgetpswPage
from pages.loginPage import LoginPage

__author__ = 'heshiwen'

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", appConfig.Config.desired_caps) # 启动app

    def testlogin(self):
        driver = self.driver
        # 输入数据
        phoneNum_null = u""
        phoneNum_null2 = " "
        phoneNum_Chinese="测试"
        phoneNum_Spcharacter="@#@!!$$"
        phoneNum_0 = "0"
        phoneNum_3 = "123"
        phoneNum_10 = ""
        phoneNum_12 ="123456789abc"
        phoneNum = u"13922763910"

        code_null = ""
        code_null2=" "
        code_Chinese = "验证码"
        code_Spcharacter="#@!#@$$"
        code_1="1"
        code_3="123"
        code_4="1234"
        code_5="12345"
        code_10="1234567890"

        newPassword1 = u"123123"
        newPassword2 = u"123456"
        # 期望title
        title_bar1 = "验证密保手机"
        title_bar2 = "填写验证码"
        title_bar3 = "重置密码"

        # 声明类对象
        login_Page = LoginPage(driver)
        forgetPw_Page = ForgetpswPage(driver)

        login_Page.enter_demo()
        try:
            forgetPw_Page.forgetPw_btn_enter()
            print("无缓冲账号")
        except:
            print("有缓存账号，先注销")
            login_Page.enter_usercenter()
            login_Page.logout_account()
            forgetPw_Page.forgetPw_btn_enter()


        print("默认不输入提交")
        forgetPw_Page.input_forgetPw_account_text(phoneNum_null)
        forgetPw_Page.forgetPw_btn_getcode()
        time.sleep(5)

        if title_bar2 not in forgetPw_Page.show_common_title_bar_title():
            print("输入账号有误，重新输入空格")
            forgetPw_Page.input_forgetPw_account_text(phoneNum_null2)
            forgetPw_Page.forgetPw_btn_getcode()
            time.sleep(5)
        if title_bar2 not in forgetPw_Page.show_common_title_bar_title():
            print("输入账号有误，重新输入中文账号：%s" % phoneNum_Chinese)
            forgetPw_Page.input_forgetPw_account_text(phoneNum_Chinese)
            forgetPw_Page.forgetPw_btn_getcode()
            time.sleep(5)
        if title_bar2 not in forgetPw_Page.show_common_title_bar_title():
            print("输入账号有误，重新输入特殊字符：%s" % phoneNum_Spcharacter)
            forgetPw_Page.input_forgetPw_account_text(phoneNum_Spcharacter)
            forgetPw_Page.forgetPw_btn_getcode()
            time.sleep(5)
        if title_bar2 not in forgetPw_Page.show_common_title_bar_title():
            print("输入账号有误，重新输入1位数字：%s" % phoneNum_0)
            forgetPw_Page.input_forgetPw_account_text(phoneNum_0)
            forgetPw_Page.forgetPw_btn_getcode()
            time.sleep(5)
        if title_bar2 not in forgetPw_Page.show_common_title_bar_title():
            print("输入账号有误，重新输入3位数字：%s" % phoneNum_3)
            forgetPw_Page.input_forgetPw_account_text(phoneNum_3)
            forgetPw_Page.forgetPw_btn_getcode()
            time.sleep(5)
        if title_bar2 not in forgetPw_Page.show_common_title_bar_title():
            print("输入账号有误，重新输入10位数字(未注册)：%s" % phoneNum_10)
            forgetPw_Page.input_forgetPw_account_text(phoneNum_10)
            forgetPw_Page.forgetPw_btn_getcode()
            time.sleep(5)
        if title_bar2 not in forgetPw_Page.show_common_title_bar_title():
            print("输入账号有误，重新输入12位（数字+字母）—未注册：%s" % phoneNum_12)
            forgetPw_Page.input_forgetPw_account_text(phoneNum_12)
            forgetPw_Page.forgetPw_btn_getcode()
            time.sleep(5)

        print("输入账号有误，重新输入11位已注册账号：%s" % phoneNum)
        forgetPw_Page.input_forgetPw_account_text(phoneNum)
        forgetPw_Page.forgetPw_btn_getcode()
        time.sleep(2)
        self.assertEqual(forgetPw_Page.show_common_title_bar_title(),title_bar2)
        print("进入页面" + forgetPw_Page.show_common_title_bar_title())

        print("验证码默认为空提交")
        forgetPw_Page.input_code_text_error(code_null)
        forgetPw_Page.code_btn_next()

        if title_bar3 not in forgetPw_Page.show_common_title_bar_title():
            print("验证码输入有误，重新输入空格：%s"%code_null2)
            forgetPw_Page.input_code_text_error(code_null2)
            forgetPw_Page.code_btn_next()
            time.sleep(2)
        if title_bar3 not in forgetPw_Page.show_common_title_bar_title():
            print("验证码输入有误，重新输入中文：%s" % code_Chinese)
            forgetPw_Page.input_code_text_error(code_Chinese)
            forgetPw_Page.code_btn_next()
            time.sleep(2)
        if title_bar3 not in forgetPw_Page.show_common_title_bar_title():
            print("验证码输入有误，重新输入特殊字符：%s" % code_Spcharacter)
            forgetPw_Page.input_code_text_error(code_Spcharacter)
            forgetPw_Page.code_btn_next()
            time.sleep(2)
        if title_bar3 not in forgetPw_Page.show_common_title_bar_title():
            print("验证码输入有误，重新输入1位数字：%s" % code_1)
            forgetPw_Page.input_code_text_error(code_1)
            forgetPw_Page.code_btn_next()
            time.sleep(2)
        if title_bar3 not in forgetPw_Page.show_common_title_bar_title():
            print("验证码输入有误，重新输入3位数字：%s" % code_3)
            forgetPw_Page.input_code_text_error(code_3)
            forgetPw_Page.code_btn_next()
            time.sleep(2)
        if title_bar3 not in forgetPw_Page.show_common_title_bar_title():
            print("验证码输入有误，重新输入错误的4位：%s" % code_4)
            forgetPw_Page.input_code_text_error(code_4)
            forgetPw_Page.code_btn_next()
            time.sleep(2)
        if title_bar3 not in forgetPw_Page.show_common_title_bar_title():
            print("验证码输入有误，重新输入5位数字：%s" % code_5)
            forgetPw_Page.input_code_text_error(code_5)
            forgetPw_Page.code_btn_next()
            time.sleep(2)
        if title_bar3 not in forgetPw_Page.show_common_title_bar_title():
            print("验证码输入有误，重新输入10位数字：%s" % code_10)
            forgetPw_Page.input_code_text_error(code_10)
            forgetPw_Page.code_btn_next()


        print("验证码输入有误，重新输入正确验证码")
        forgetPw_Page.getcode_again()
        time.sleep(5)
        forgetPw_Page.input_code_text(phoneNum)
        forgetPw_Page.code_btn_next()
        time.sleep(2)
        if title_bar3 in forgetPw_Page.show_common_title_bar_title():
            try:
                forgetPw_Page.input_newPw_text(newPassword1)
                forgetPw_Page.pwd_visible()
                forgetPw_Page.btn_resetPassword()
                print("密码：%s"%newPassword1)
            except:
                time.sleep(2)
                forgetPw_Page.clear_newPw_text()
                forgetPw_Page.input_newPw_text(newPassword2)
                forgetPw_Page.pwd_visible()
                forgetPw_Page.btn_resetPassword()
                print("密码：%s" % newPassword2)
        print("账号：%s,修改密码成功"%phoneNum)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
