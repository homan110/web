# coding = utf-8
import random
import unittest
import time
from telnetlib import EC

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from androidConfig import appConfig
from pages.loginPage import LoginPage
from pages.registerPage import RegisterPage



__author__="heshiwen"

class Register(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", appConfig.Config.desired_caps)  # 启动app

    def testQuickRegister(self):
        driver = self.driver
        # 输入数据
        phoneNum_null = u""
        phoneNum_null2 = " "
        phoneNum_Chinese = "测试"
        phoneNum_Spcharacter = "@#@!!$$"
        phoneNum_0 = "0"
        phoneNum_3 = "123"
        phoneNum_10 = ""
        phoneNum_12 = "123456789abc"
        phoneNum_int = 13922760000 + random.randint(1000, 10000)
        phoneNum = str(phoneNum_int)
        password = u"123456"

        code_null = ""
        code_null2 = " "
        code_Chinese = "验证码"
        code_Spcharacter = "#@!#@$$"
        code_1 = "1"
        code_3 = "123"
        code_4 = "1234"
        code_5 = "12345"
        code_10 = "1234567890"

        # 期望
        title_bar1 = "绑定手机"
        title_bar2 = "验证手机"
        title_bar3 = "绑定成功"

        bindSuccess_title="友友的游戏账号已绑定成功了哟！"

        #未绑定手机tip期望
        Not_bindphone_tip = "未绑定手机"

        # 声明类对象
        login_Page = LoginPage(driver)
        register_Page = RegisterPage(driver)

        login_Page.enter_demo()
        #快速注册
        try:
            register_Page.quickregister_enter()
        except:
            print("有缓存账号，先注销")
            time.sleep(5)
            login_Page.enter_usercenter()
            login_Page.logout_account()
            login_Page.enter_demo()
            register_Page.quickregister_enter()
        #register_Page.quickregister_input_text(password)
        register_Page.login_quickregister_btn()
        time.sleep(5)

        self.assertEqual(register_Page.Not_Bindphone_title(),Not_bindphone_tip)
        register_Page.Bindphone_btn()

        # print("默认不输入提交")
        # register_Page.register_input_account_text(phoneNum_null)
        # register_Page.register_btn_getcode()
        # if title_bar2 not in register_Page.register_common_bar_title():
        #     print("输入账号有误，重新输入空格")
        #     register_Page.register_input_account_text(phoneNum_null2)
        #     register_Page.register_btn_getcode()
        #     time.sleep(5)
        # if title_bar2 not in register_Page.register_common_bar_title():
        #     print("输入账号有误，重新输入中文账号：%s" % phoneNum_Chinese)
        #     register_Page.register_input_account_text(phoneNum_Chinese)
        #     register_Page.register_btn_getcode()
        #     time.sleep(5)
        # if title_bar2 not in register_Page.register_common_bar_title():
        #     print("输入账号有误，重新输入特殊字符：%s" % phoneNum_Spcharacter)
        #     register_Page.register_input_account_text(phoneNum_Spcharacter)
        #     register_Page.register_btn_getcode()
        #     time.sleep(5)
        # if title_bar2 not in register_Page.register_common_bar_title():
        #     print("输入账号有误，重新输入1位数字：%s" % phoneNum_0)
        #     register_Page.register_input_account_text(phoneNum_0)
        #     register_Page.register_btn_getcode()
        #     time.sleep(5)
        # if title_bar2 not in register_Page.register_common_bar_title():
        #     print("输入账号有误，重新输入3位数字：%s" % phoneNum_3)
        #     register_Page.register_input_account_text(phoneNum_3)
        #     register_Page.register_btn_getcode()
        #     time.sleep(5)
        # if title_bar2 not in register_Page.register_common_bar_title():
        #     print("输入账号有误，重新输入10位数字(未注册)：%s" % phoneNum_10)
        #     register_Page.register_input_account_text(phoneNum_10)
        #     register_Page.register_btn_getcode()
        #     time.sleep(5)
        # if title_bar2 not in register_Page.register_common_bar_title():
        #     print("输入账号有误，重新输入12位（数字+字母）—未注册：%s" % phoneNum_12)
        #     register_Page.register_input_account_text(phoneNum_12)
        #     register_Page.register_btn_getcode()
        #     time.sleep(5)

        print("重新输入11位未注册手机账号：%s" % phoneNum)
        register_Page.register_input_account_text(phoneNum)
        register_Page.register_btn_getcode()
        time.sleep(2)
        self.assertEqual(register_Page.register_common_bar_title(),title_bar2)
        print("进入页面" + register_Page.register_common_bar_title())

        # print("验证码默认为空提交")
        # register_Page.input_code_text_error(code_null)
        # register_Page.register_common_next_btn()
        #
        # if title_bar3 not in register_Page.register_common_bar_title():
        #     print("验证码输入有误，重新输入空格：%s" % code_null2)
        #     register_Page.input_code_text_error(code_null2)
        #     register_Page.register_common_next_btn()
        #     time.sleep(2)
        # if title_bar3 not in register_Page.register_common_bar_title():
        #     print("验证码输入有误，重新输入中文：%s" % code_Chinese)
        #     register_Page.input_code_text_error(code_Chinese)
        #     register_Page.register_common_next_btn()
        #     time.sleep(2)
        # if title_bar3 not in register_Page.register_common_bar_title():
        #     print("验证码输入有误，重新输入特殊字符：%s" % code_Spcharacter)
        #     register_Page.input_code_text_error(code_Spcharacter)
        #     register_Page.register_common_next_btn()
        #     time.sleep(2)
        # if title_bar3 not in register_Page.register_common_bar_title():
        #     print("验证码输入有误，重新输入1位数字：%s" % code_1)
        #     register_Page.input_code_text_error(code_1)
        #     register_Page.register_common_next_btn()
        #     time.sleep(2)
        # if title_bar3 not in register_Page.register_common_bar_title():
        #     print("验证码输入有误，重新输入3位数字：%s" % code_3)
        #     register_Page.input_code_text_error(code_3)
        #     register_Page.register_common_next_btn()
        #     time.sleep(2)
        # if title_bar3 not in register_Page.register_common_bar_title():
        #     print("验证码输入有误，重新输入错误的4位：%s" % code_4)
        #     register_Page.input_code_text_error(code_4)
        #     register_Page.register_common_next_btn()
        #     time.sleep(2)
        # if title_bar3 not in register_Page.register_common_bar_title():
        #     print("验证码输入有误，重新输入5位数字：%s" % code_5)
        #     register_Page.input_code_text_error(code_5)
        #     register_Page.register_common_next_btn()
        #     time.sleep(2)
        # if title_bar3 not in register_Page.register_common_bar_title():
        #     print("验证码输入有误，重新输入10位数字：%s" % code_10)
        #     register_Page.input_code_text_error(code_10)
        #     register_Page.register_common_next_btn()

        print("输入正确验证码")
        #register_Page.register_getcode_again()
        time.sleep(2)
        register_Page.phone_input_codetext(phoneNum)
        register_Page.register_common_next_btn()

        #self.assertEqual(register_Page.register_common_bar_title(),title_bar3)

        try:
            register_Page.register_input_account_text(password)
            register_Page.register_pwd_visible()
            register_Page.register_btn_getcode()
        except:
            print("不需要设置手机登录密码")

        self.assertEqual(register_Page.Bindphone_showSuccess_text(),title_bar3)
        register_Page.back_usercenter_btn()

        login_Page.enter_usercenter()
        # 注销
        login_Page.logout_account()
        print("注销绑定手机：" + phoneNum+"的账号")

    def testRegister(self):
        driver = self.driver
        # 手机注册
        # 输入数据
        phoneNum_int = 13922760000 +random.randint(1000, 10000)
        phoneNum=str(phoneNum_int)
        password = "123456"
        # 期望
        title_bar1 = ""
        title_bar2 = ""
        title_bar3 = ""

        bindSuccess_title = "友友的游戏账号已绑定成功了哟"
        Already_registered_title=""

        # 未绑定手机tip期望
        Not_bindphone_tip = "123"

        # 声明类对象
        login_Page = LoginPage(driver)
        register_Page = RegisterPage(driver)

        login_Page.enter_demo()
        try:
            register_Page.register_enter()
        except:
            print("有缓存账号，先注销")
            login_Page.enter_usercenter()
            login_Page.logout_account()
            login_Page.enter_demo()
            register_Page.register_enter()

        #已注册的手机
        register_Page.register_input_account_text(phoneNum)
        try:
            self.assertEqual(register_Page.show_Already_registered_tips(),Already_registered_title)
            print(register_Page.show_Already_registered_tips())
            register_Page.register_ohter_btn()
        except:
            register_Page.register_btn_getcode()

        register_Page.phone_input_codetext(phoneNum)
        register_Page.register_common_next_btn()
        register_Page.register_input_password_text(password)
        register_Page.register_pwd_visible()
        register_Page.login_btn()

        login_Page.enter_usercenter()
        # 注销
        login_Page.logout_account()
        print("注销账号：" + phoneNum)


    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

