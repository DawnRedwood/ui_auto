import unittest
from time import sleep
import sys, os, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from parameterized import parameterized
from lib.init import root_url, driver, sleep_time, init
from case.Learning_Log.method import register, login, logout
data, Page = init(__file__)
page = Page()


class Topics(unittest.TestCase):
    """主题"""

    def tearDown(self):
        sleep(sleep_time)
    
    @classmethod
    def tearDownClass(cls):
        logout()

    def test_1_guest_auth(self):
        """游客权限"""
        # 验证访问主题列表的权限
        page.get(page.topics_url)
        self.assertTrue(page.exist(page.login))
        # 验证访问主题的权限
        page.get(page.correct_topic_url)
        self.assertTrue(page.exist(page.login))
        # 验证新增条目的权限
        page.get(page.correct_add_entry_url)
        self.assertTrue(page.exist(page.login))
        # 验证编辑条目的权限
        page.get(page.correct_edit_entry_url)
        self.assertTrue(page.exist(page.login))

    def test_2_user_auth(self):
        """用户权限"""
        login()
        # 验证访问主题的权限
        page.get(page.correct_topic_url)
        self.assertTrue(page.exist(page.add_new_entry))
        page.get(page.wrong_topic_url)
        self.assertTrue(page.exist(page.error_404))
        # 验证新增条目的权限
        page.get(page.correct_add_entry_url)
        self.assertTrue(page.exist(page.entry_content))
        page.get(page.wrong_add_entry_url)
        self.assertTrue(page.exist(page.error_404))
        # 验证编辑条目的权限
        page.get(page.correct_edit_entry_url)
        self.assertTrue(page.exist(page.entry_content))
        page.get(page.wrong_edit_entry_url)
        self.assertTrue(page.exist(page.error_404))

    def test_3_add_topic(self):
        """新增主题"""
        # 主题名称为空
        page.topics.click()
        page.add_new_topic.click()
        page.submit.click()
        self.assertTrue(page.exist(page.submit))
        # 正常新增主题
        page.topics.click()
        page.add_new_topic.click()
        page.topic_name = data["topic_name"]
        page.submit.click()
        self.assertTrue(page.exist(page.topic))

    def test_4_add_entry(self):
        """新增条目"""
        # 条目内容为空
        page.topics.click()
        page.topic.click()
        page.add_new_entry.click()
        page.submit.click()
        self.assertTrue(page.exist(page.submit))
        # 正常新增条目
        page.topic.click()
        page.add_new_entry.click()
        page.entry_content = data["entry_content"]
        page.submit.click()
        self.assertTrue(page.exist(page.entry))

    def test_5_edit_entry(self):
        """编辑条目"""
        # 条目内容为空
        page.topics.click()
        page.topic.click()
        page.edit_entry.click()
        page.clear(page.entry_content)
        page.submit.click()
        self.assertTrue(page.exist(page.submit))
        # 正常编辑条目
        page.topic.click()
        page.edit_entry.click()
        page.clear(page.entry_content)
        page.entry_content = data["edited_entry_content"]
        page.submit.click()
        self.assertTrue(page.exist(page.edited_entry))


if __name__ == "__main__":
    unittest.main()
