import unittest
from time import sleep
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from parameterized import parameterized
from lib.init import root_url, driver, sleep_time, init
from case.Learning_Log.method import register, login, logout
data, Page = init(__file__) # OtherPage, other_data = init("\\module_1_login\\case_2_logout.py") # 如果需要初始化其它页面时
page = Page()


class Register(unittest.TestCase):
    """注册"""

    def tearDown(self):
        sleep(sleep_time)
    
    @classmethod
    def tearDownClass(cls):
        logout()

    def test_1_jump(self):
        """跳转到注册页面"""
        # print("通过") # 可以通过print()在测试报告中添加描述
        # 验证从导航栏跳转到注册页面
        page.get()
        page.jump_from_nav.click()
        self.assertEqual(page.url, driver.current_url)
        # 验证从正文跳转到注册页面
        page.get()
        page.jump_from_body.click()
        self.assertEqual(page.url, driver.current_url)

    @parameterized.expand([
        (data["wrong_username"][0], data["wrong_password1"][0], data["wrong_password2"][0]), # 无用户名
        (data["wrong_username"][1], data["wrong_password1"][1], data["wrong_password2"][1]), # 无密码
        (data["wrong_username"][2], data["wrong_password1"][2], data["wrong_password2"][2]), # 无确认密码
        (data["wrong_username"][3], data["wrong_password1"][3], data["wrong_password2"][3]), # 用户名重名
        (data["wrong_username"][4], data["wrong_password1"][4], data["wrong_password2"][4]), # 密码不一致
        (data["wrong_username"][5], data["wrong_password1"][5], data["wrong_password2"][5]), # 密码与用户名相似
        (data["wrong_username"][6], data["wrong_password1"][6], data["wrong_password2"][6]), # 密码小于8位
        (data["wrong_username"][7], data["wrong_password1"][7], data["wrong_password2"][7]), # 密码为常用密码
        (data["wrong_username"][8], data["wrong_password1"][8], data["wrong_password2"][8]), # 密码为纯数字
    ])
    def test_2_register_failure(self, wrong_username, wrong_password1, wrong_password2):
        """注册失败"""
        register(wrong_username, wrong_password1, wrong_password2)
        self.assertEqual(page.url, driver.current_url)
    
    def test_3_register_success(self):
        """注册成功"""
        register(data["correct_username"], data["correct_password"], data["correct_password"])
        self.assertTrue(root_url == driver.current_url and not page.exist(page.jump_from_nav))


if __name__ == "__main__":
    unittest.main()
