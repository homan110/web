# coding = utf-8


from selenium import webdriver


class Config():

    driver = webdriver.Firefox()

    driver.get("http://pyw.cn")

# user=driver.find_element_by_id("user_center")
