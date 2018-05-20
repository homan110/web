#  coding=utf-8
import time
from selenium.webdriver.common.by import By

from common.smsCode import codeConfig
from pages.basePage import Page

__author__='heshiwen'

class RegisterPage(Page):
    #元属集
    #common bar_title
    pyw_tv_common_title_bar_title = (By.ID, 'com.pengyouwan.game.sdk.demo:id/pyw_tv_common_title_bar_title')

    #快速注册
    pyw_tv_quick_regist=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_tv_quick_regist')
    pyw_tv_fastregister_account_tips=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_tv_fastregister_account_tips')
    pyw_et_fastregister_password=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_et_fastregister_password')
    pyw_btn_login_fastregister=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_btn_login_fastregister')
      #未绑定手机
    pyw_title=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_title')
    pyw_iv_tips_word=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_iv_tips_word')
    pyw_btn_bind=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_btn_bind')
      #绑定手机
    pyw_et_register_code=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_et_register_code')
    # common 账号输入框
    pyw_et_register_account = (By.ID, 'com.pengyouwan.game.sdk.demo:id/pyw_et_register_account')

    pyw_btn_getcode= (By.ID, 'com.pengyouwan.game.sdk.demo:id/pyw_btn_getcode')
    # common 账号输入框
    pyw_et_register_password = (By.ID, 'com.pengyouwan.game.sdk.demo:id/pyw_et_register_account')

    pyw_btn_next=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_btn_next')

    pass_TextView=(By.CLASS_NAME,'android.widget.TextView')
    pyw_btn_back_usercenter=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_btn_back_usercenter')

    #手机注册
    pyw_tv_fast_regist=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_tv_fast_regist')
    pyw_tv_getcode_again = (By.ID, 'com.pengyouwan.game.sdk.demo:id/pyw_tv_getcode')
    pyw_et_register_pwd = (By.ID, 'com.pengyouwan.game.sdk.demo:id/pyw_et_register_pwd')

    pyw_pwd_visible_img = (By.ID, 'com.pengyouwan.game.sdk.demo:id/pyw_pwd_visible_img')
    pyw_btn_login = (By.ID, 'com.pengyouwan.game.sdk.demo:id/pyw_btn_login')


    #已注册
    TextView=(By.CLASS_NAME,'android.widget.TextView')
    pyw_btn_register_ohter=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_btn_register_ohter')


    def __init__(self, appium_driver):
        Page.__init__(self, appium_driver)
#快速注册
    def quickregister_enter(self):
        self.click(self.pyw_tv_quick_regist)

   # def quickregister_input_text(self,password):
#    self.input_text(*self.pyw_et_fastregister_password,password)

    def login_quickregister_btn(self):
        self.click(self.pyw_btn_login_fastregister)

    def Not_Bindphone_title(self):
        return self.find_element(*self.pyw_title).text

    def Bindphone_btn(self):
        self.click(self.pyw_btn_bind)

    def phone_input_codetext(self,phoneNum):
        code = codeConfig()
        yzm = code.Pymysql1(phoneNum)
        self.input_text(self.pyw_et_register_code, yzm)

    def register_common_next_btn(self):
        self.click(self.pyw_btn_next)

    def register_pwd_visible(self):
        self.click(self.pyw_pwd_visible_img)

    def Bindphone_showSuccess_text(self):
        return self.find_element(*self.pass_TextView).text

    def back_usercenter_btn(self):
        self.click(self.pyw_btn_back_usercenter)

#手机注册
    def register_enter(self):
        self.click(self.pyw_tv_fast_regist)

    def register_input_account_text(self,phoneNum):
        self.input_text(self.pyw_et_register_account,phoneNum)

    def register_btn(self):
        self.click(self.pyw_tv_fast_regist)

    def register_btn_getcode(self):
        self.click(self.pyw_btn_getcode)

    def register_getcode_again(self):
        self.click(self.pyw_tv_getcode_again)

    def register_input_password_text(self,password):
        self.input_text(self.pyw_et_register_pwd,password)

    def register_common_bar_title(self):
        return self.find_element(*self.pyw_tv_common_title_bar_title).text

    def input_code_text_error(self,code):
        self.input_text(self.pyw_et_register_code,code)

# 已注册
    def show_Already_registered_tips(self):
        return self.find_element(*self.TextView).text

    def register_ohter_btn(self):
        self.click(self.pyw_btn_register_ohter)

    def login_btn(self):
        self.click(self.pyw_btn_login)





