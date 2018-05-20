# coding = utf-8
import HTMLTestRunner
import unittest
import time


from waptest.testcase.testLogin import Login


__author__ = 'heshiwen'

if __name__ == '__main__':
    unittest.main()

     testunit = unittest.TestSuite()

     testunit.addTest(Login('testlogin'))
    #
    # # 获取当前时间，这样便于下面的使用。
    # now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    # # 打开一个文件，将result写入此file中
    # fq = open("E:\\Androidtest\\report\\" + now + ".html", "wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fq, title='测试结果', description=u'测试报告:')
    # runner.run(testunit)
    # fq.close()
