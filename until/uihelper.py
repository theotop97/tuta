from appium import webdriver
from until import configloader
from selenium.webdriver.support.wait import WebDriverWait

'''
Ui自动化测试帮助类，可以初始化webDriver、配置环境
封装了一些经常用到的方法
'''
class UiHelper:
    """
    初始化类的时候，获取webDriver
    """
    def __init__(self, configPath: str):
        self.desried_caps = configloader.loadConfig(configPath)
        self._driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desried_caps)

    '''
    关闭webDriver
    '''
    def quitDriver(self):
        if self._driver:
            self._driver.quit()

    '''
    寻找元素
        controlInfo:传入要寻找元素的id或classname或name或根据xpath定位，要求必须为String类型
    '''
    def findElement(self, controlInfo: str):
        if controlInfo.startswith("//"):
            element = self._driver.find_element_by_xpath(controlInfo)
        elif ":id/" in controlInfo or ":string/" in controlInfo:
            element = self._driver.find_element_by_id(controlInfo)
        else:
            try:
                element = self._driver.find_element_by_name(controlInfo)
            except:
                element = self._driver.find_element_by_class_name(controlInfo)

        return element

    '''
    隐式等待
        time_seconds:隐式等待的时长，单位为秒
    '''
    def impWait(self, time_seconds):
        self._driver.implicitly_wait(time_seconds)

    '''
    显式等待
        time_out:超时时长，单位为秒
        time_seconds:间隔时间，单位为秒
        element:具体某个元素显式等待
    '''
    def expWait(self, time_out, time_seconds, element: str):

        wd = WebDriverWait(self._driver, time_out, poll_frequency=time_seconds)
        wd.until(lambda x: x.find_element_by_id(element))
