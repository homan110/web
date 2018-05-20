#  coding=utf-8
import time
from selenium.webdriver.common.by import By
from pages.basePage import Page

__author__='heshiwen'

class ModifypswPage(Page):
    # 元素集合
    #修改密码
    common_title_bar_title=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_tv_common_title_bar_title')
    et_reset_old=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_et_reset_old')
    et_reset_new=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_et_reset_new')
    pwd_visible=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_pwd_visible_img')
    btn_reset_modify=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_btn_reset_modify')

    usercenter_btn = (By.ID, u'com.pengyouwan.game.sdk.demo:id/btn_usercenter')

    common_title_bar_back=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_layout_common_title_bar_back')


    def __init__(self,appium_driver):
        Page.__init__(self,appium_driver)

    def show_common_title_bar_title(self):
        return self.find_element(*self.common_title_bar_title).text

    def Modify_et_reset_input(self,oldpassword,newpassword):
        time.sleep(2)
        self.input_text(self.et_reset_old,oldpassword)
        self.input_text(self.et_reset_new,newpassword)

    def Modify_clear_et_reset_input(self,oldpassword,newpassword):
        self.click(self.et_reset_old)
        self.clear(self.et_reset_old)
        self.input_text(self.et_reset_old,oldpassword)
        self.click(self.et_reset_new)
        self.clear(self.et_reset_new)
        self.input_text(self.et_reset_new,newpassword)

    def Modify_pwd_visible(self):
        self.click(self.pwd_visible)

    def modify_btn_reset(self):
        time.sleep(2)
        self.click(self.btn_reset_modify)
        time.sleep(2)

    def displayed_usercenterbtn(self):
        self.find_element(self.usercenter_btn).is_displayed()

    def Modify_bar_back(self):
        self.click(self.common_title_bar_back)