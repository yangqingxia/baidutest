import unittest, doctest, test
import sys
sys.path.append("/testcase")
import allcase_list
import HTMLTestRunner

suit = doctest.DocTestSuite()
#罗列要执行的文件
'''
suit.addTest(unittest.makeSuite(testcase.search.BaiduSearch))
suit.addTest(unittest.makeSuite(testcase.set.BaiduSet))
'''
print("start")
# alltestnames = ['testcase.search.BaiduSearch','testcase.baiduset.bdset.BaiduSet']
# alltestnames = ['search.BaiduSearch','bdset.BaiduSet']
alltestnames = allcase_list.caselist()
for test in alltestnames:
    suit.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
#suit.addTest(unittest.makeSuite(search.BaiduSearch))
filename = "F:\\learn\\result\\selenium\\result.html"
fp = open(filename, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="测试套件测试结果",description="百度测试结果")
runner.run(suit)
fp.close()
#unittest.TextTestRunner(verbosity=2).run(suit) 不生产报表