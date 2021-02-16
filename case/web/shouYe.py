# coding=utf-8
from selenium import webdriver
from public.login import Mylogin
import unittest
import os
import time

class TestShouye(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://101.133.169.100/yuns/index.php")
        self.driver.maximize_window()
        time.sleep(5)
        #获取当前时间，并把当前时间格式化输出
        print("starttime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        filedir = "D:/test/screenshot/"
        #如果不存在这个路径，会取创建一个路径
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'screenshot'))
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()


    # def testShouye01_01(self):
    #     '''测试首页导航文案显示是否正常'''
    #     Mylogin(self.driver).login()
    #     firstPageNavi = self.driver.find_element_by_xpath("//div[@class='top']/span")
    #     loginText = self.driver.find_element_by_css_selector("div.login>a:nth-child(1)")
    #     regisText = self.driver.find_element_by_css_selector("div.login>a:nth-child(3)")
    #
    #     self.assertEqual("亲，欢迎您来到云商系统商城！",firstPageNavi.text)
    #     self.assertEqual("177****979", loginText.text)
    #     self.assertEqual("退出", regisText.text)
    #     self.assertNotEqual("dd", regisText.text)
    #
    #     self.assertIn("云商系统商城",firstPageNavi.text)
    #
    #     self.assertTrue(self.driver.find_element_by_xpath("//div[@class='top']/span").is_displayed())
    #     self.assertFalse(firstPageNavi.is_displayed())
    #
    #     if loginText.text == "177****0979":
    #         print("等于")
    #     else:
    #         print("不等于")
    #         self.driver.find_element_by_xpath("王麻子")



    # def testShouye01_02(self):
    #     '''验证搜索内容无时，提示语是否正常'''
    #     Mylogin(self.driver).login()
    #     self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[1]").send_keys("王麻子")
    #     self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[2]").click()
    #     time.sleep(2)
    #     searchText = self.driver.find_element_by_xpath("//div[@class='nomsg']")
    #     self.assertEqual(searchText.text, "抱歉，没有找到相关的商品")

    def testShouye01_03(self):
        '''
        验证搜索内容是否正常
        执行步骤：1.输入“Uniqlo”
        预期结果：1.页面有相应商品显示
        :param self:
        :return:
        '''
        self.driver.find_element_by_xpath("//input[@class='but1']").send_keys("Uniqlo")
        self.driver.find_element_by_xpath("//input[@class='but2']").click()
        searchResult = self.driver.find_element_by_xpath("//div[@class='img']/a[contains(@href,'72.html')]")
        self.assertEqual(searchResult.get_attribute("title"), "女装003优质长绒棉A字型条纹连衣裙(七分袖) 412932 优衣库UNIQLO")

    def testShouye01_04(self):
       '''
       验证菜单栏数据匹配
       1.点击“秒杀”
       2.查看页面展示效果
       预期结果：页面跳转到秒杀界面
       :return:
       '''
       self.driver.find_element_by_xpath("//div[@class='nav_pub']/a[2]").click()
       self.driver.switch_to.window(self.driver.window_handles[1])
       searchText = self.driver.find_element_by_xpath("//div[@class='bnma']/a[1]")
       self.assertEqual(searchText.text,"限时抢购")
    def testShouye01_05(self):
        '''
        验证验证查看订单
        1.点击首页--查看“我的订单
        2.查看页面
        前置条件：会员已登录
        预期结果：1.页面显示我的订单
        :return:
        '''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//div[@class='help']/a[2]").click()
        ele =  self.driver.find_element_by_xpath("//div[@class='tab']/span")
        self.assertEqual(ele.text,"我的订单")

if __name__ == "__main__":
    unittest.main()


