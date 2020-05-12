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
        return self.__findElement(controlInfo)

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

    '''
    在控件中查找其他控件的方法
        parentElement:父级控件
        childElementInfo:子空间的id/name/classname/xpath定位方法，要求传入String
    '''
    def findElementInParentElement(self, parentElement: webdriver.webelement, childElementInfo: str):
        if childElementInfo.startswith("//"):
            element = parentElement.find_element_by_xpath(childElementInfo)
        elif "/id" in childElementInfo or ":string/":
            element = parentElement.find_element_by_id(childElementInfo)
        else:
            try:
                element = parentElement.find_element_by_name(childElementInfo)
            except:
                element = parentElement.find_element_by_class_name(childElementInfo)
        return element

    '''
    寻找元素
    '''
    def __findElement(self, elementInfo: str):
        if elementInfo.startswith("//"):
            element = self._driver.find_element_by_xpath(elementInfo)
        elif ":id/" in elementInfo or ":string/" in elementInfo:
            element = self._driver.find_element_by_id(elementInfo)
        else:
            try:
                element = self._driver.find_element_by_name(elementInfo)
            except:
                element = self._driver.find_element_by_class_name(elementInfo)
        return element

    '''
    检查元素Enable属性
        elementInfo:要检查元素的定位信息
    '''
    def checkElementIsEnable(self, elementInfo):
        return self.__checkElementAttribute(elementInfo, "enable")

    '''
    检查元素clickable属性
        elementInfo:要检查元素的定位信息
    '''
    def checkElementClickable(self, elementInfo):
        return self.__checkElementAttribute(elementInfo, "clickable")

    '''
    检查元素checked属性
        elementInfo:要检查元素的定位信息
    '''
    def checkElementIsChecked(self, elementInfo):
        return self.__checkElementAttribute(elementInfo, "checked")

    '''
    检查元素属性
        elementInfo:要检查元素的定位信息
        attributeName:要检查元素的属性信息
    '''
    def __checkElementAttribute(self, elementInfo: str, attributeName: str):
        return self.findElement(elementInfo).get_attribute(attributeName)

    def getWebDriver(self):
        return self._driver
