import unittest
from time import sleep
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from parameterized import parameterized
from lib.init import root_url, driver, sleep_time, init
from case.Learning_Log.method import register, login, logout
data, Page = init(__file__)
page = Page()


class Login(unittest.TestCase):
    """登录"""

    def tearDown(self):
        sleep(sleep_time)

    @classmethod
    def tearDownClass(cls):
        logout()

    def test_1_jump(self):
        """跳转到登录页面"""
        # 验证从导航栏跳转到登录页面
        page.get()
        page.jump.click()
        self.assertEqual(page.url, driver.current_url)
        # 验证从Topics重定向到登录页面,并在登录后返回Topics页面
        page.get()
        page.redirect.click()
        self.assertEqual(page.redirect_url, driver.current_url)
        page.username = data["correct_username"]
        page.password = data["correct_password"]
        page.login.click()
        self.assertTrue(page.topics_url == driver.current_url)
        logout()

    @parameterized.expand([
        (data["wrong_username"][0], data["wrong_password"][0]), # 用户名为空
        (data["wrong_username"][1], data["wrong_password"][1]), # 密码为空
        (data["wrong_username"][2], data["wrong_password"][2]), # 用户名、密码错误
    ])
    def test_2_login_failure(self, wrong_name, wrong_password):
        """登录失败"""
        login(wrong_name, wrong_password)
        self.assertEqual(page.url, driver.current_url)
    
    def test_3_login_success(self):
        """登录成功"""
        login(data["correct_username"], data["correct_password"])
        self.assertTrue(root_url == driver.current_url and not page.exist(page.jump))


if __name__ == "__main__":
    unittest.main()
