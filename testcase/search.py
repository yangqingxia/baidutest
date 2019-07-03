from selenium import webdriver
import time
import unittest

import os


class BaiduSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://www.baidu.com"
        self.verficationErrors = []
        self.accept_next_alert = True

    def testSearch(self):
        # 下面用于生成报表中的注释
        u"""百度搜索"""
        driver = self.driver
        driver.get(self.base_url)
        try:
           driver.find_element_by_id("kw").send_keys("selenium我要自学网")
           driver.find_element_by_id("su").click()
           time.sleep(2)
           driver.close()
        except:
            driver.get_screenshot_as_file("F:\\学习练习\\python\\untitled\\error_png\\kw.png")

    def tearDown(self) -> None:
        self.driver.quit()
        self.assertEqual([], self.verficationErrors)
'''

if __name__ == "__main__":

    #unittest.main()
    testunit = unittest.TestSuite()  # 定义一个单元测试容器
    testunit.addTest(BaiduSearch("testSearch"))  # 将测试用例加入到测试容器中
    unittest.TestRunner().run(testunit)
'''