import os
import unittest
import time
from public.loginApp import Mylogin
from appium import webdriver
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['noReset'] = 'True'
        desired_caps['app'] = PATH('D:/newCourse/zuiyou518.apk')
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'
        desired_caps['automationName'] = 'Uiautomator2'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()
    def test_newsModule01(self):
        '''验证消息页面显示是否正常'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='消息']").click()
        ele = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        for i in range(0,len(ele)):
            print(ele[i].text)
        self.assertEqual("提醒",ele[0].text)
        self.assertEqual("私信",ele[1].text)

    def test_newsModule02(self):
        '''验证回复私信功能是否正常'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='消息']").click()
        ele = self.driver.find_elements_by_class_name("android.widget.RelativeLayout")
        ele[1].click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/input").send_keys('你好啊')
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/text").click()
if __name__ == "__main__":
    unittest.main()

