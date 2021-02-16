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
    # def topicModule01(self):
    #     '''验证发布功能是否正常'''
    #     self.driver.implicitly_wait(60)
    #     time.sleep(3)
    #     self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/iconTabItem").click()

    def test_topicModule02(self):
        '''验证发布功能是否正常'''
        self.driver.implicitly_wait(60)
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='视频']").click()
        self.driver.find_element_by_xpath(
            "//android.widget.FrameLayout[@resource-id='cn.xiaochuankeji.tieba:id/publish_item']/android.widget.ImageView[@resource-id='cn.xiaochuankeji.tieba:id/iconTabItem']").click()
        time.sleep(4)
        rs = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etContent").send_keys("红红火火恍恍惚惚")
        rsText = rs.text
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/try_publish").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='搞笑']").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/topic_desc").click()
        time.sleep(2)
        self.driver.find_elements_by_id('cn.xiaochuankeji.tieba:id/title')[1].click()
        # con = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
        # for i in range(0,len(con)):
        #     print(i,con[i].text)
        # self.assertEqual(rsText,con)
        time.sleep(6)
if __name__ == "__main__":
    unittest.main()

