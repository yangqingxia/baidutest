from selenium import webdriver
import os,time
import  unittest


class BaiduSet(unittest.TestCase):


    def setUp(self) :
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"
        self.verficationErrors = []
        self.accept_next_alert = True

    def testBaiduSet(self):
        #下面用于生成报表中的注释
        u"""百度搜索设置"""
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(5)
        myset = driver.find_element_by_link_text("设置")
        webdriver.ActionChains(driver).move_to_element(myset).perform()
        time.sleep(10)
        driver.find_element_by_link_text("搜索设置").click()
        time.sleep(10)  # 很重要，保证可见
        bdsel = driver.find_element_by_id("nr")

        bdsel.find_element_by_xpath("//option[@value='50']").click()
        time.sleep(10)
        driver.find_element_by_link_text("保存设置").click()

        driver.switch_to.alert.accept()
        driver.close()

    def tearDown(self) -> None:
        self.driver.quit()
        self.assertEqual([], self.verficationErrors)
'''
if __name__ == "__main__":
    #unittest.main()
    testunit = unittest.TestSuite()  # 定义一个单元测试容器
    testunit.addTest(BaiduSet("testBaiduSet"))  # 将测试用例加入到测试容器中
    unittest.TestRunner().run(testunit)
'''
