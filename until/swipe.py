from appium import webdriver

class Swipe:

    def __init__(self, wd: webdriver):
        self.driver = wd
        self.x = self.driver.get_window_size()["width"]
        self.y = self.driver.get_window_size()["height"]

    def swipeUp(self, dur=500, t=1):
        x1 = self.x * 0.5   # x坐标
        y1 = self.y * 0.75  # 起始y坐标
        y2 = self.y * 0.25  # 终点y坐标
        self.__mySwipe(x1, y1, x1, y2, dur, t)

    def swipeDown(self, dur=500, t=1):
        x1 = self.x * 0.5   # x坐标
        y1 = self.y * 0.25  # 起始y坐标
        y2 = self.y * 0.75  # 终点y坐标
        self.__mySwipe(x1, y1, x1, y2, dur, t)

    def swipeLeft(self, dur=500, t=1):
        x1 = self.x * 0.75
        y1 = self.y * 0.5
        x2 = self.x * 0.05
        self.__mySwipe(x1, y1, x2, y1, dur, t)

    def swipeRight(self, dur=500, t=1):
        x1 = self.x * 0.75
        y1 = self.y * 0.5
        x2 = self.x * 0.05
        self.__mySwipe(x1, y1, x2, y1, dur, t)

    def __mySwipe(self, x1, y1, x2, y2, dur=500, t=1):
        for i in range(t):
            self.driver.swipe(x1, y1, x2, y2, dur)
