#  coding=utf-8
import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium import  webdriver
from waptest.androidConfig.appConfig import Config
from waptest.pages.basePage import Page



class LoginPage(Page):

    user = (By.ID,"user_center")

    login_phoneNum=(By.XPATH,"html/body/div[2]/form[1]/ul/li[1]/input")
    login_password=(By.XPATH,"html/body/div[2]/form[1]/ul/li[2]/input")
    l=(By.XPATH,"html/body/div[2]/form[1]/ul/p/button")
    user_tel=(By.XPATH,"html/body/div[1]/div[1]/div/a[5]/span[2]")

    waitingSuccess = time.sleep

    def __init__(self,selenium_driver):
        Page.__init__(self,selenium_driver)

    def input_login_text(self, phoneNum, password):
        time.sleep(2)
        self.input_text(self.login_phoneNum, phoneNum)
        self.input_text(self.login_password, password)

    def click_login_btn(self):
        self.click(self.user)
        print(u"点击登录")

    def click_login(self):
        self.click(self.l)
        print(u"登录")

    def show_usercentertitle_bar(self):
        return self.find_element(*self.user_tel).text
        #print(%s"登陆成功",self.user_tel)

    def enter_demo(self):
        self.click(self.center_demo)

    def enter_usercenter(self):
        self.find_element(self.usercenter)
        self.click(self.usercenter)

    def logout_account(self):
        self.click(self.pyw_btn_change_account)
        self.click(self.logout_cancel)
        self.click(self.pyw_btn_change_account)
        self.click(self.logout_ensure)

    def modify_loginpassword_btn(self):
        self.click(self.pyw_layout_modify_loginpassword)

    def modify_Paypsw_btn(self):
        self.click(self.pyw_layout_paypassword)

    # Tip框提示内容展示
    def show_loginTip_element(self):
        return self.find_element(*self.login_element).text

