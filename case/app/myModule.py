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
    def test_myModule01(self):
        '''验证“我的”页面展示情况'''
        # Mylogin(self.driver).login()
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='我的']").click()
        ele = self.driver.find_elements_by_class_name("android.widget.TextView")
        for i in range(0,len(ele)):
            print(ele[i].text,i)
        self.assertEqual(ele[8].text,"空间动态")
        self.assertEqual(ele[9].text, "我的帖子")
        self.assertEqual(ele[10].text, "我的评论")
        self.assertEqual(ele[11].text, "我的收藏")
        self.assertEqual(ele[12].text, "我赞过的")
if __name__ == "__main__":
    unittest.main()

