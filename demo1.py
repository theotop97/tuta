import os

# from until.uihelper import UiHelper
#
#
# ul = UiHelper("config.yml")
#
#
# ul.findElement("com.android.settings:id/search").click()
# #
# # ul.expWait(5, 1, "android:id/search_src_text")
# # sd = ul.findElement("android.widget.TextView")
# # print(sd.get_attribute("resourceId"))
# ul.quitDriver()


# e = 0
# if e:
#     print(11)
# else:
#     print(2)
#
# print(os.getcwd())


# from until.logger import Logger
#
# log = Logger(__name__, "231.txt")
#
# log.getLog().debug("dsds")
from until import swipe
from until.swipe import Swipe
from until.uihelper import UiHelper

uh = UiHelper("config.yml")

sw = Swipe(uh.getWebDriver())

sw.swipUp()

