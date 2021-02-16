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
    def testLogin01(self):
        '''
        验证手机号不输入登录
        1.打开云商系统
        2.点击左上角“登录”
        3.手机号不输入，密码输入正确，点击“登录按键”
        预期结果：不能登录，提示用户名不能为空
        :return:
        '''
        self.driver.find_element_by_xpath("//div[@class='login']/a[1]").click()
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys("")
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys("123456")
        self.driver.find_element_by_xpath("//input[@class='submit_login']").click()
        time.sleep(3)
        ele = self.driver.find_element_by_css_selector("div#error_msg")
        self.assertEqual(ele.text, "用户名不能为空")

    def testLogin02(self):
        '''
        验证密码不输入登录
       1.打开云商系统
       2.点击左上角“登录”
       3.手机号输入正确，密码不输入，点击“登录按键”
        预期结果：不能登录，提示密码不能为空
        :return:
        '''
        self.driver.find_element_by_xpath("//div[@class='login']/a[1]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys("17358453683")
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys("")
        self.driver.find_element_by_xpath("//input[@class='submit_login']").click()
        time.sleep(3)
        ele = self.driver.find_element_by_css_selector("div#error_msg")
        self.assertEqual(ele.text, "密码不能为空")

    def testLogin03(self):
        '''
       验证未注册的手机号进行登录
       前置条件：手机号未注册
       1.打开云商系统
       2.点击左上角“登录”
       3.输入未注册的手机号，输入符合要求的密码格式，点击“登录按键”
        预期结果：不能登录并提示该用户未注册
        实际结果：不能登录，提示用户名或者密码错误
        :return:
        '''
        self.driver.find_element_by_xpath("//div[@class='login']/a[1]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys("17358453234")
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys("123456")
        self.driver.find_element_by_xpath("//input[@class='submit_login']").click()
        time.sleep(3)
        ele = self.driver.find_element_by_css_selector("div#error_msg")
        self.assertEqual(ele.text, "该用户未注册")

    def testLogin04(self):
        '''
         验证登录页面跳转忘记密码页面
         前置条件：已在会员登录界面
         1.打开云商系统
         2.点击左上角“登录”
         3.点击“忘记密码”
         预期结果：1.进入云商系统
                   2.进入登录界面
                   3.进入“忘记密码”界面
        :return:
        '''
        self.driver.find_element_by_xpath("//div[@class='login']/a[1]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='login_reg_box']/a[1]").click()
        time.sleep(3)
        ele = self.driver.find_element_by_xpath("//div[@class='bname']/span")
        self.assertEqual("重置密码",ele.text)

    def testLogin05(self):
        '''
         验证登录页面跳转注册页面
         前置条件：已在会员登录界面
         1.打开云商系统
         2.点击左上角“登录”
         3.点击“立即注册”
         预期结果：1.进入云商系统
                   2.进入登录界面
                   3.进入“注册”界面
        :return:
        '''
        self.driver.find_element_by_xpath("//div[@class='login']/a[1]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='login_reg_box']/a[2]").click()
        time.sleep(3)
        ele = self.driver.find_element_by_xpath("//div[@class='reg_bname']/span")
        self.assertEqual("用户注册", ele.text)

if __name__ == "__main__":
    unittest.main()
