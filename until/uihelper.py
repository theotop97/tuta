from appium import webdriver
from until import configloader
from selenium.webdriver.support.wait import WebDriverWait

class UiHelper:

    def __init__(self, configPath: str):
        self.desried_caps = configloader.loadConfig(configPath)
        self._driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desried_caps)

    def quitDriver(self):
        if self._driver:
            self._driver.quit()

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

    def impWait(self, time_seconds):
        self._driver.implicitly_wait(time_seconds)

    def expWait(self, time_out, time_seconds, element: str):

        wd = WebDriverWait(self._driver, time_out, poll_frequency=time_seconds)
        wd.until(lambda x: x.find_element_by_id(element))
