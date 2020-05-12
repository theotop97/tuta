from until.uihelper import UiHelper

uh = UiHelper("config.yml")
uh.impWait(2)
uh.getWebDriver().start_activity("com.tencent.mobileqq", ".activity.LoginActivity")

uh.expWait(10, 1, "com.tencent.mobileqq:id/btn_login")

uh.quitDriver()