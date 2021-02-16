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
    # def testshouye01_01(self):
    #     '''验证首页导航栏文案显示是否正常'''
    #     time.sleep(8)
    #     self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click() #app打开后弹出的广告框
    #     time.sleep(6)
    #     navText = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
    #     self.assertEqual(navText[0].text,"关注")
    #     self.assertEqual(navText[1].text, "推荐")
    #     self.assertEqual(navText[2].text, "视频")
    #     self.assertEqual(navText[3].text, "图文")

    #
    # def testshouye01_02(self):
    #     '''验证帖子列表内容跳转'''
        Mylogin(self.driver).login()
    #     time.sleep(8)
    #     aa = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
    #     bb = aa.text
    #     aa.click()
    #     time.sleep(3)
    #     forumDetailText = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvTitle")
    #     cc = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ss")
    #     self.assertEqual(forumDetailText.text,"帖子详情")
    #     self.assertEqual(bb,cc.text)


    # def testshouye01_03(self):
    #     '''验证评论帖子功能'''
    #     Mylogin(self.driver).login()
    #     time.sleep(3)
    #     self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/iconTabItem").click()
    #     time.sleep(6)
    #     self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/expand_content_view").click()
    #     time.sleep(3)
    #     self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput").send_keys("textCESHI")
    #     self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/send").click()
    #     sendContent = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/expandTextView")
    #     sendContentRawList = []
    #     for i in range(0, len(sendContent)):
    #         sendContentRawList.append(sendContent[i].text)
    #     sendContentList = "".join(sendContentRawList)
    #     self.assertIn("textCESHI", sendContentList)

    def testshouye01(self):
        '''验证关注功能'''
        try:
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        except:
            pass
        # Mylogin(self.driver).login()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='关注']").click()
        time.sleep(3)
        rs= self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/layout_subscribe_unselected")
        rs.click()
        time.sleep(3)
        rs_text = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_subscribe_name_selected")
        self.assertEqual("已关注",rs_text.text)


    def testshouye02(self):
        '''验证关注板块是否支持滑动'''
        try:
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        except:
            pass
        # Mylogin(self.driver).login()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='关注']").click()
        time.sleep(3)
        self.driver.swipe(200,400,800,400,3000)
        time.sleep(3)
        rs = self.driver.find_elements_by_class_name("android.widget.LinearLayout")[1]
        self.assertEqual(True,rs.is_enabled())
    def testshouye03(self):
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='关注']").click()
        time.sleep(3)
        rs = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
        rs_text = rs.text
        print(rs_text)
        rs.click()
        time.sleep(3)
        rs_title = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvTitle")
        rs_content = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvPostContent")
        self.assertEqual(rs_text,rs_content.text)
        self.assertEqual("帖子详情",rs_title.text)

    def testshouye04(self):
        '''验证用户头像跳转情况'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/avatar_view_avatar").click()
        time.sleep(3)
        btn_home = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/btn_profile")
        btn_zone = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/btn_zone")
        # print(rs.text)
        self.assertEqual( btn_home.text,"主页")
        self.assertEqual(btn_zone.text,"空间")

    def testshouye05(self):
        '''验证详情页返回首页'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/avatar_view_avatar").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/iv_back_white").click()
        rs_nav = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        self.assertEqual(rs_nav[0].text,"关注")
        self.assertEqual(rs_nav[1].text, "推荐")
        self.assertEqual(rs_nav[2].text, "视频")
        self.assertEqual(rs_nav[3].text, "图文")

    def testshouye06(self):
        '''验证是否可以评论帖子'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/middle_view").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput").send_keys("哈哈哈")
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/send").click()
        toast_rs = ("xpath", "//*[contains(@text,'评论发送成功')]")
        rs_text = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_rs))
        self.assertEqual("评论发送成功",rs_text.text)
    def testshouye07(self):
        '''验证评论帖子页面返回'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/middle_view").click()
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput").send_keys("哈哈哈")
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/send").click()
        time.sleep(2)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ivBack").click()
        rs_nav = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        self.assertEqual(rs_nav[0].text,"关注")
        self.assertEqual(rs_nav[1].text, "推荐")
        self.assertEqual(rs_nav[2].text, "视频")
        self.assertEqual(rs_nav[3].text, "图文")
    def testshouye08(self):
        '''验证搜索功能是否正常'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input").send_keys("新闻")
        rs = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title").text
        self.assertIn("新闻",rs)
    def testshouye09(self):
        ''' 验证取消搜索情况'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input").send_keys("新闻")
        time.sleep(2)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/cancel").click()
        rs_nav = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        self.assertEqual(rs_nav[0].text,"关注")
        self.assertEqual(rs_nav[1].text, "推荐")
        self.assertEqual(rs_nav[2].text, "视频")
        self.assertEqual(rs_nav[3].text, "图文")

    def testshouye10(self):
        '''验证清空“搜索输入”情况'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input").send_keys("新闻")
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input_clear").click()
        rs_text= self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input")
        self.assertEqual("搜索话题 / 帖子 / 用户",rs_text.text)

    def testshouye11(self):
        '''验证转发取消功能是否正常'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='图文']").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/operate_share").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/iconTabItem").click()

    def testshouye12(self):
        '''验证不喜欢功能是否正常'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='视频']").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/simple_decorator_delete").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='内容重复']").click()
        toast_text = ('xpath',".//*[contains(@text,'将减少类似内容推荐')]")
        rs = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_text))
        self.assertEqual("将减少类似内容推荐",rs.text)

if __name__ == "__main__":
    unittest.main()

