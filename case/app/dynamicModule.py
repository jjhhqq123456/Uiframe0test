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
    def test_dynamicModule01(self):
        '''验证动态列表显示情况'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='动态']").click()
        time.sleep(3)
        rs = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        for i in  range(0,len(rs)):
            print(rs[i].text,i)
        # self.assertEqual("关注",rs[1].text)
        # self.assertEqual("广场",rs[2].text)

    #
    # def test_dynamicModule02(self):
    #     '''验证评论动态功能是否正常'''
    #     self.driver.implicitly_wait(60)
    #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='动态']").click()
    #     self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvCommentCount").click()
    #     self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput").send_keys("sdfsa")
    #     self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/send").click()
    #     toast_rs = ("xpath", "//*[contains(@text,'评论发送成功')]")
    #     rs_text = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_rs))
    #     self.assertEqual("评论发送成功",rs_text.text)

    # def test_dynamicModule03(self):
    #     '''验证评论动态功能是否正常'''
    #     self.driver.implicitly_wait(60)
    #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='动态']").click()
    #     self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvCommentCount").click()
    #     self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput").send_keys("sdfsa")
    #     self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/send").click()
    #     toast_rs = ("xpath", "//*[contains(@text,'评论发送成功')]")
    #     rs_text = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_rs))
    #     self.assertEqual("评论发送成功", rs_text.text)
    #
    # def test_dynamicModule04(self):
    #     '''验证点击头像进入用户主页进行私信情况'''
    #     self.driver.implicitly_wait(60)
    #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='动态']").click()
    #     self.driver.find_element_by_xpath("//android.view.View[@resource-id='cn.xiaochuankeji.tieba:id/avatar_view_root']/android.widget.ImageView[1]").click()
    #     self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_send_message").click()
    #     self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/input").send_keys('你好啊')
    #     self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/text").click()
    #     success_text = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/content").text
    #     self.assertEqual("你好啊",success_text)
if __name__ == "__main__":
    unittest.main()

