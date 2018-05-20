# coding = utf-8
from selenium.webdriver.common.by import By

from common.smsCode import codeConfig
from pages.basePage import Page

__author__="heshiwen"

class ForgetpswPage(Page):
    #元属集

    #忘记密码
    forget_password_enter = (By.ID,U'com.pengyouwan.game.sdk.demo:id/pyw_tv_forgetpsw_tips')
    pyw_et_forgetPw_account = (By.ID,u'com.pengyouwan.game.sdk.demo:id/pyw_et_register_account')
    pyw_btn_getcode =(By.ID,u'com.pengyouwan.game.sdk.demo:id/pyw_btn_getcode')
    pyw_common_title_bar_title=(By.ID,u'com.pengyouwan.game.sdk.demo:id/pyw_tv_common_title_bar_title')
    pyw_et_register_code=(By.ID,u'com.pengyouwan.game.sdk.demo:id/pyw_et_register_code')
    pyw_tv_getcode=(By.ID,u'com.pengyouwan.game.sdk.demo:id/pyw_tv_getcode')
    pyw_btn_next =(By.ID,u'com.pengyouwan.game.sdk.demo:id/pyw_btn_next')
    pyw_new_password=(By.ID,u'com.pengyouwan.game.sdk.demo:id/pyw_et_register_account')
    pyw_password_visible_img=(By.ID,u'com.pengyouwan.game.sdk.demo:id/pyw_pwd_visible_img')
    pyw_btn_login=(By.ID,u'com.pengyouwan.game.sdk.demo:id/pyw_btn_login')
    pyw_btn_entergame=(By.ID,u'com.pengyouwan.game.sdk.demo:id/pyw_btn_entergame')

    def __init__(self,appium_driver):
        Page.__init__(self, appium_driver)

    def input_forgetPw_account_text(self,phoneNum):
        self.input_text(self.pyw_et_forgetPw_account,phoneNum)

    def forgetPw_btn_enter(self):
        self.click(self.forget_password_enter)

    def show_common_title_bar_title(self):
        return self.find_element(*self.pyw_common_title_bar_title).text

    def forgetPw_btn_getcode(self):
        self.click(self.pyw_btn_getcode)

    def input_code_text_error(self,code):
        self.input_text(self.pyw_et_register_code,code)

    def input_code_text(self,phoneNum):
        code = codeConfig()
        yzm = code.Pymysql1(phoneNum)
        self.input_text(self.pyw_et_register_code,yzm)

    def getcode_again(self):
        self.click(self.pyw_tv_getcode)

    def code_btn_next(self):
        self.click(self.pyw_btn_next)

    def input_newPw_text(self, password):
        self.input_text(self.pyw_new_password,password)

    def pwd_visible(self):
        self.click(self.pyw_password_visible_img)

    def btn_resetPassword(self):
        self.click(self.pyw_btn_login)

    def clear_newPw_text(self):
        self.clear(self.pyw_new_password)

    def show_pyw_btn_entergame(self):
        return  self.find_element(self.pyw_btn_entergame).text




