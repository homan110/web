# _*_ coding:utf-8 _*_
import importlib
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'heshiwen'

importlib.reload(sys)



# pages基类
class Page(object):
    """
        Page基类，所有page都应该继承该类
    """
    #  __init__ 类的实例化
    def __init__(self, selenium_driver):
        self.driver = selenium_driver
        self.timeout = 30


    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
            #WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
            return self.driver.find_element(*loc)
        except:

            print("%s 页面中未能找到 %s 元素" % (self, loc))


    def input_text(self, loc, text):
        self.find_element(*loc).send_keys(text)

    def click(self, loc):
        self.find_element(*loc).click()

    def clear(self,loc):
        self.find_element(*loc).clear()

    def submit(self, loc):
        self.find_element(loc).submit()

    def get_title(self):
        return self.driver.title

    # 重写switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    # 定义script方法，用于执行js脚本，范围执行结果
    def script(self, src):
        self.driver.execute_script(src)




