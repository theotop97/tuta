import unittest

from until.logger import Logger
from until.uihelper import UiHelper

class Demo2(unittest.TestCase):

    uh = None
    log = None

    @classmethod
    def setUpClass(cls):
        cls.uh = UiHelper("config.yml")
        cls.log = Logger(__name__, "demo2.txt")
        print("setUpClass")
        cls.log.getLog().info("setUpClass")

    def setUp(self):
        # self.uh.getWebDriver().start_activity("com.android.settings", ".SubSettings")
        self.uh.getWebDriver().reset()
        print("setUp")
        self.log.getLog().info("setUp")

    def tearDown(self):
        # self.uh.getWebDriver().reset()
        print("tearDown")
        self.log.getLog().info("tearDown")

    def test_1(self):
        self.uh.findElement("//*[@text='WLAN']").click()

    def test_2(self):
        self.uh.findElement("//*[@text='更多']").click()

    def test_3(self):
        self.uh.findElement("//*[@text='蓝牙']").click()

    @classmethod
    def tearDownClass(cls):
        cls.uh.quitDriver()
        log = cls.log.getLog()
        log.info("tearDownClass")
        print("tearDownClass")


if __name__ == '__main__':
    unittest.main()
