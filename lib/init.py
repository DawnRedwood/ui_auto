import time
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import toml
import unittest
from selenium import webdriver


# 读取配置信息
config = toml.load("./config.toml")

# 初始化项目配置
root_url = config["project"]["root_url"]

# 初始化浏览器配置
if config["driver"]["headless"]:
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    driver = webdriver.Chrome(chrome_options=option)
else:
    driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(config["driver"]["headless"])

# 初始化测试配置
test_time = time.strftime(config["test"]["time_format"])
sleep_time = config["test"]["sleep_time"]

# 初始化data与Page
def init(name):
    project_name = name.split("\\")[-3]
    package_name = name.split("\\")[-2]
    file_name = name.split("\\")[-1].split("_", 1)[1].split(".")[0]
    import_file = __import__("case.%s.%s.data_%s" % (project_name, package_name, file_name), fromlist=["data", "Page"])
    return import_file.data, import_file.Page
