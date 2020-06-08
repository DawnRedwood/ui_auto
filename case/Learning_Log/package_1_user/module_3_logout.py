import unittest
from time import sleep
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from parameterized import parameterized
from lib.init import root_url, driver, sleep_time, init
from case.Learning_Log.method import register, login, logout
data, Page = init(__file__)
page = Page()


class Logout(unittest.TestCase):
    """退出"""

    @classmethod
    def setUpClass(cls):
        login()

    def tearDown(self):
        sleep(sleep_time)

    def test_1_logout(self):
        """退出"""
        self.assertTrue(page.exist(page.logout))
        logout()
        self.assertFalse(page.exist(page.logout))


if __name__ == "__main__":
    unittest.main()
