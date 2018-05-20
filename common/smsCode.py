# coding = utf-8
import re
import unittest

import pymysql


class codeConfig(unittest.TestCase):

    def Pymysql1(self, phoneNum):
        conn = pymysql.connect(host='192.168.20.60', port=3306, user='xiaopeng', passwd='xiaopeng99', db='xiaopeng2',
                               charset='utf8')
        cur = conn.cursor()

        # 查询
        cur.execute('select * from bmsglog where mobile='+phoneNum+' ORDER BY addtime DESC LIMIT 1')
        data = cur.fetchall()
        for d in data:
            print("验证码： " + str(d[1]))
            string = str(d[1])
        b = re.findall(r"\d+\b", string)
        list = b
        print(list[0])
        cur.close()
        conn.close()
        yzm = list[0]
        return yzm

