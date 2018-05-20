#  coding=utf-8
import time
from selenium.webdriver.common.by import By
from pages.basePage import Page

__author__='heshiwen'

class ManageAccount(Page):
    # 元素集合
    common_title_bar_title=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_tv_common_title_bar_title')
    Manage_account_normal=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_layout_account_normal')
    Manage_account_new=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_layout_account_new')

    #account_normal
    Manage_account_normal_SetPsw=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_tv_login')
    Manage_account_normal_unbind=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_tv_unbind')
    cancle=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_tv_cancle')

    Set_account_password_et=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_et_register_account')
    Managepwd_visible=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_pwd_visible_img')
    Managebtn_login=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_btn_login')

    Managepyw_tv_account=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_tv_account')
    Managepyw_tv_pwd=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_tv_pwd')

    Managepyw_btn_back=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_btn_back')

    #new
    Manageaccount_newSet=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_tv_login')
    Managebind_account=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_tv_unbind')

    #绑定已有账号
    Manageet_login_account=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_et_login_account')
    Manageet_login_psw = (By.ID, 'com.pengyouwan.game.sdk.demo:id/pyw_et_login_psw')

    #绑定失败
    Manageback_btn=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_btn_unbind')
    Manage_bind_otheraccount_btn=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_btn_bind')

    #登录新账号
    Managebtn_login_new=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_layout_account_normal')
    Managebtnlogint_new_ensure=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_btn_logout_ensure')
    Managebtnlogint_new_cancel=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_btn_logout_cancel')


    def __init__(self,appium_driver):
        Page.__init__(self,appium_driver)

    def common_show_bar_title(self):
        return self.find_element(*self.common_title_bar_title).text

    def Manage_account_normal_btn(self):
        self.click(self.Manage_account_normal)

    def Manage_account_new_btn(self):
        self.click(self.Manage_account_new)

    def Manage_account_normal_SetPsw_btn(self):
        self.click(self.Manage_account_normal_SetPsw)

    def Manage_account_normal_unbind_btn(self):
        self.click(self.Manage_account_normal_unbind)

    def cancle_btn(self):
        self.click(self.cancle)

    def Set_account_password_input(self,password):
        self.input_text(self.Set_account_password_et,password)

    def pwd_visible_btn(self):
        self.click(self.Managepwd_visible)

    def login_btn(self):
        self.click(self.Managebtn_login)

    def Setaccount_Success_tip(self):
        return self.find_element(self.Managepyw_tv_account).text

    def Setpsw_Success_tip(self):
        return self.find_element(self.Managepyw_tv_pwd).text

    def btn_back(self):
        self.click(self.Managepyw_btn_back)

    def account_newSet_btn(self):
        self.click(self.Manageaccount_newSet)

    def bind_account_enter(self):
        self.click(self.Managebind_account)

    def et_login_account_input(self,account):
        self.input_text(self.Manageet_login_account,account)
    def et_login_psw_input(self,password):
        self.input_text(self.Manageet_login_psw,password)

    def Manage_btn_login_new(self):
        self.click(self.Managebtn_login_new)

    def Manage_btnlogint_new_ensure(self):
        self.click(self.Managebtnlogint_new_ensure)

    def Manage_btnlogint_new_cancel(self):
        self.click(self.Managebtnlogint_new_cancel)




