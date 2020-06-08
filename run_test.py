import os, time
import unittest
from lib.HTMLTestRunner_cn import HTMLTestRunner
from lib.init import config, driver


if __name__ == "__main__":
    # 初始化配置参数变量
    globals().update(config["project"])
    globals().update(config["test"])
    report_dir = f"./report/{project}/"
    if not os.path.exists(report_dir):
        os.mkdir(report_dir)
    report = report_dir + "Report " + time.strftime("%Y-%m-%d %H_%M_%S") + ".html"
    # 创建测试报告
    with open(report, "wb") as f:
        # 加载并执行测试用例
        runner = HTMLTestRunner(stream=f, title=config["title"], description=project + "自动化测试",
            verbosity=verbosity, retry=retry, save_last_try=save_last_try)
        if full_test:
            suite = unittest.defaultTestLoader.discover(f"./case/{project}/", pattern="module_*.py")
        else:
            suite = unittest.TestSuite()
            discover = unittest.defaultTestLoader.discover
            loader = unittest.TestLoader().loadTestsFromName
            for package in packages:
                suite.addTest(discover(f"./case/{project}/{package}/", pattern="module_*.py", top_level_dir=f"./"))
            for module in modules:
                suite.addTest(loader(f"case.{project}.{module}"))
            for case in cases:
                suite.addTest(loader(f"case.{project}.{case}"))
        runner.run(suite)
    driver.quit()
