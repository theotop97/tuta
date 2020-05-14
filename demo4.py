import os
import unittest

import ddt
import HTMLTestRunner
from until.logger import Logger
from until.uihelper import UiHelper
from until.parseexcelutil import ParseExcel

pe = ParseExcel("settingsearch.xlsx", "search1")

@ddt.ddt
class Demo4(unittest.TestCase):

    uh = None
    log = None

    @classmethod
    def setUpClass(cls):
        cls.uh = UiHelper("config.yml")
        cls.log = Logger(__name__, "demo2.txt")
        print("setUpClass")
        cls.log.getLog().info("setUpClass")
        # cls.pe = ParseExcel("settingsearch.xlsx", "search1")

    def setUp(self):
        self.uh.findElement("com.android.settings:id/search").click()

    def tearDown(self):
        # self.uh.getWebDriver().reset()
        self.uh.findElement("android:id/search_src_text").send_keys("")
        print("tearDown")
        self.log.getLog().info("tearDown")

    @ddt.data(*pe.getDataFromSheet())
    def testByExcel(self, data):
        testData, exceptData = tuple(data)
        self.uh.findElement("android:id/search_src_text").send_keys(testData)
        self.uh.impWait(2)

    @classmethod
    def tearDownClass(cls):
        cls.uh.quitDriver()
        log = cls.log.getLog()
        log.info("tearDownClass")
        print("tearDownClass")


if __name__ == '__main__':
    unittest.main()
    print("main")
    suit = unittest.TestSuite()
    suit.addTest(Demo4("testByExcel"))

    fileName = r"F:\CODE\demo4.html"
    fp = open(fileName, 'wb')

    reportRunner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例测试情况')
    reportRunner.run(suit)
    fp.close()
