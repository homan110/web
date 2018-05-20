# coding = utf-8
import time
import unittest
from selenium import webdriver
from androidConfig import appConfig
from pages.loginPage import LoginPage
from pages.usercenter.ModifypswPage import ModifypswPage

__author__ = 'heshiwen'


class Modifypsw(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", appConfig.Config.desired_caps)  # 启动app

    def testModifypsw(self):
        #数据
        driver = self.driver
        # 输入数据
        phoneNum = "17112340000"
        password1 = "123123"
        password2='123456'
        # 期望
        title_bar1 = "欢迎登录，%s" % (phoneNum)
        title_bar2 = "修改密码"

        # 声明Page类对象
        login_Page = LoginPage(driver)
        Modifypsw_Page = ModifypswPage(driver)
        login_Page.enter_demo()
        try:
            #登录账号
            time.sleep(1)
            login_Page.input_login_text(phoneNum, password1)
            print("无缓冲账号")
            login_Page.click_login_btn()
            time.sleep(1)
            # 验证
            if title_bar1 in login_Page.show_loginTip_element():
               self.assertEqual(login_Page.show_loginTip_element(), title_bar1)
               print("登录后提示信息：" + login_Page.show_loginTip_element())
            else:
                time.sleep(1)
                login_Page.input_login_text(phoneNum, password2)
                login_Page.click_login_btn()
                time.sleep(1)
                # 验证
                self.assertEqual(login_Page.show_loginTip_element(), title_bar1)
                print("登录后提示信息：" + login_Page.show_loginTip_element())

        except:
            print("有缓存账号")


        time.sleep(2)
        login_Page.enter_usercenter()
        login_Page.modify_loginpassword_btn()
        self.assertEqual(Modifypsw_Page.show_common_title_bar_title(),title_bar2)
        print("当前页面："+Modifypsw_Page.show_common_title_bar_title())

        Modifypsw_Page.Modify_et_reset_input(password1,password2)
        Modifypsw_Page.Modify_pwd_visible()
        Modifypsw_Page.modify_btn_reset()
        try:
            Modifypsw_Page.Modify_bar_back()
            login_Page.modify_loginpassword_btn()

            Modifypsw_Page.Modify_et_reset_input(password2, password1)
            Modifypsw_Page.Modify_pwd_visible()
            Modifypsw_Page.modify_btn_reset()

            login_Page.enter_demo()
            login_Page.input_login_text(phoneNum, password1)
            login_Page.click_login_btn()
            # 验证
            self.assertEqual(login_Page.show_loginTip_element(), title_bar1)
            print("登录后提示信息：" + login_Page.show_loginTip_element())
            print("账号：%s ，修改密码成功"%phoneNum)
            print("修改后的密码为：%s"%password1)
        except:
            time.sleep(1)
            login_Page.enter_demo()
            login_Page.input_login_text(phoneNum, password2)
            login_Page.click_login_btn()
            # 验证
            self.assertEqual(login_Page.show_loginTip_element(), title_bar1)
            print("登录后提示信息：" + login_Page.show_loginTip_element())
            print("账号：%s ，修改密码成功" % phoneNum)
            print("修改后的密码为：%s" % password2)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()


