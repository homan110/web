#  coding=utf-8
import time
from selenium.webdriver.common.by import By

from common.smsCode import codeConfig
from pages.basePage import Page

__author__='heshiwen'

class PaypswPage(Page):
    # 元素集合
    #交易密码
    #问题
    common_title_bar_title=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_tv_common_title_bar_title')
    Paypsw_TextView=(By.CLASS_NAME,'android.widget.TextView')
    Paypsw_modify_pay_TextView=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_tv_modify_pay')
    Paypsw_setquestion_Text=(By.NAME,'交易密码找回问题设置：')
    Paypsw_set_1_question = (By.NAME,'我的家乡')
    Paypsw_set_1_answer=(By.ID,'home')
    Paypsw_set_2_question = (By.NAME, '小学校名')
    Paypsw_set_2_answer = (By.ID, 'school')
    Paypsw_set_3_question = (By.NAME, '我父亲名字')
    Paypsw_set_3_answer = (By.ID, 'father')
    Paypsw_set_4_question = (By.NAME, '我的生日')
    Paypsw_set_4_answer = (By.ID, 'day')

    Paypsw_sure_btn=(By.NAME,'确定提交')

    #设置
    Paypsw_phone=(By.ID,'phoneNum')
    Paypsw_phone_getcode = (By.ID,'button')
    Paypsw_phone_code=(By.ID,'smsCode')
    Paypsw = (By.ID,'payPwd')
    Paypsw_changeSure_btn = (By.ID,'changePayWord')

   #已设置
    Paypsw_change_btn=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_layout_change_paypsd')
    Paypsw_change_TextView =(By.NAME,'请输入6位旧的交易密码：')
    Paypsw_old = (By.ID,'oldPwd')
    Paypsw_changeNew_TextView = (By.NAME,'请输入6位新的交易密码')
    Paypsw_New=(By.ID,'newPwd')


    Paypsw_find_btn=(By.ID,'com.pengyouwan.game.sdk.demo:id/pyw_layout_find_paypsd')
    Paypsw_find_answer = (By.ID,'answer')
    Paypsw_find_next=(By.NAME,'下一步')



    def __init__(self,appium_driver):
        Page.__init__(self,appium_driver)

    def show_common_title_bar_title(self):
        return self.find_element(self.common_title_bar_title).text
    def Paypsw_TextView_show(self):
        return self.find_element(self.Paypsw_TextView).text
    def Paypsw_modify_pay_TextView_show(self):
        return self.find_element(self.Paypsw_modify_pay_TextView).text

    def Paypsw_set_answer1_input(self,answer1):
        self.input_text(self.Paypsw_set_1_answer,answer1)
    def Paypsw_set_answer2_input(self, answer2):
        self.input_text(self.Paypsw_set_2_answer, answer2)
    def Paypsw_set_answer3_input(self,answer3):
        self.input_text(self.Paypsw_set_3_answer, answer3)
    def Paypsw_set_answer4_input(self,answer4):
        self.input_text(self.Paypsw_set_4_answer, answer4)

    def Paypsw_Sure_btn(self):
        self.click(self.Paypsw_sure_btn)

    def Paypsw_phone_show(self):
        return self.find_element(self.Paypsw_phone).text
    def Paypsw_phone_getcode_btn(self):
        self.click(self.Paypsw_phone_getcode)
    def Paypsw_phone_code_input(self,phoneNum):
        code = codeConfig()
        yzm = code.Pymysql1(phoneNum)
        self.input_text(self.Paypsw_phone_code,yzm)
    def Paypsw_input(self,Paypassword):
        self.input_text(self.Paypsw,Paypassword)

    def Paypsw_Change_btn(self):
        self.click(self.Paypsw_change_btn)
    def Paypsw_change_TextView_show(self):
        return self.find_element(self.Paypsw_change_TextView).text
    def Paypsw_old_input(self,Paypsw_old):
        self.input_text(self.Paypsw_old,Paypsw_old)
    def Paypsw_changeNew_TextView_show(self):
        return self.find_element(self.Paypsw_changeNew_TextView).text
    def Paypsw_New_input(self,Paypsw_New):
        self.input_text(self.Paypsw_New,Paypsw_New)

    def Paypsw_setSure_btn(self):
        self.click(self.Paypsw_sure_btn)

    def Paypsw_Find_btn(self):
        self.click(self.Paypsw_find_btn)
    def Paypsw_Find_answer_input(self,answer):
        self.input_text(self.Paypsw_find_answer,answer)
    def Paypsw_Find_next_btn(self):
        self.click(self.Paypsw_find_next)

    def Paypsw_Find_answer_page(self):
        self.find_element(self.Paypsw_find_next).is_displayed()
