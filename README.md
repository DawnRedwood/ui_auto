# UIAUTO
> **作者**：Dawn  
> **语言**：Python  
> **概述**：本项目主要用于==Web端UI自动化测试==，所用框架为`python`+`selenium`+`unittest`。编写用例提供了两种方式，一是通过PO模式编写用例，二是通过`katalon-recorder`录制用例。项目提供了参数化执行用例、生成测试报告、错误截图、用例可以选择全部执行或部分执行、常用参数可配置、简化selenium中的复杂方法等功能。  
> **引用**：  
> - **page_object**: https://github.com/SeldomQA/poium   
在虫师的poium库基础上做了一定的修改，增加了一些方法。  
> - **HTMLTestRunner_cn**: https://github.com/GoverSky/HTMLTestRunner_cn   
改了几行代码，使模块排序按照模块名而不是类名，使截图不需要每次都初始化`webdriver`。  

### 项目目录介绍  
```
uiauto
  ┝ attach                              # 用于上传下载的附件目录
  |   └ project_name
  ┝ case                                # 用于存放用例的目录
  |   └ project_name
  |         ┝ package_1_name
  |         |       ┝ data_1_name       # 存放数据的文件
  |         |       └ module_1_name     # 存放用例代码的文件
  |         ┝ package_2_name
  |         └ method.py                 # 存放该项目公共方法的文件
  ┝ lib                                 # 用于存放公共库的目录
  |   ┝ HTMLTestRunner_cn.py            # 生成测试报告的库
  |   ┝ init.py                         # 初始化各种参数的库
  |   └ page_object.py                  # 实现PO设计模式的库
  ┝ report                              # 存放测试报告
  |   └ project_name
  ┝ config.toml                         # 配置文件
  ┝ README.md                           # 说明文件
  └ run_test.py                         # 执行测试的文件
```

### 使用步骤  
1. 安装`python`或`anaconda`（版本: `3.7`或更高）。  
- python: https://www.python.org/downloads/  
- anaconda: https://www.anaconda.com/distribution/  
2. 安装用到的库。
```
# 在cmd中执行下面的命令
pip install selenium
pip install parameterized
pip install toml
```
3. 根据你的`Chrome`浏览器版本安装对应的`webdriver`。  
下载地址：http://npm.taobao.org/mirrors/chromedriver/  
下载后将`webdriver`放到`python`的根目录。

4. 安装录制工具`Chrome`插件`Katalon_Recorder`。  
下载地址：https://chrome.google.com/webstore/detail/katalon-recorder-selenium/ljdobmomdgdljniojadhoplhkpialdid  
如果下载地址无法打开，可以将`lib`目录下的`Katalon_Recorder_5.1.0_0.crx`文件拖动到浏览器中进行安装。

5. 编写`case`文件夹中的用例，修改`config.py`文件中的配置。

6. 执行测试，生成测试报告。
```
# 在cmd中项目根目录下执行下面的命令
python runtest.py
# 运行结束后，测试报告在report目录中生成
```

### 已实现功能  
1. 参数化：在方法前加`@parameterized.expand`装饰器。
```
@parameterized.expand([
    (data["username"][0], data["password"][0],
    (data["username"][1], data["password"][1]),
])
def test_2_register_failure(self, username, password):
```

2. 截图：用例执行失败会自动截图，也可以手动执行命令截图。
```
# 在用例执行过程中通过下列代码手动截图
page.screenshot(self, 1) # 该用例中第一次截图
page.screenshot(self)    # 该用例中第二次及之后的截图
```

3. 执行部分用例：修改`config.py`中的配置项。
```
full_test = false # 是否完整测试, true: 完整测试, false: 部分测试
packages = ["package_2_topics"] # 待测包
modules = ["package_1_user.module_1_register"] # 待测模块
cases = [
    "package_1_user.module_2_login.Login.test_1_jump",
    "package_1_user.module_4_logout_by_record.Module4LogoutByRecord.test_module4_logout_by_record"
] # 待测用例, 此项慎用, 因为同一 module 内的不同 case 可能耦合
```

4. PO设计模式：在`data_1_xx.py`，`module_1_yy.py`中录入对应的信息。
```
# data_1_register.py:
data = {
    "wrong_username": ["", test_time, test_time, "test", test_time, test_time, test_time, test_time, test_time],
    "wrong_password1": ["", "", "test123456", "test123456", "test123456", test_time, "t_t123", "testtest", "20200101"],
    "wrong_password2": ["", "", "", "test123456", "test234567", test_time, "t_t123", "testtest", "20200101"],
    "correct_username": test_time,
    "correct_password": "test123456"
}
class Page(PageObject):
    url = "https://dawnredwood-learninglog.herokuapp.com/users/register/"
    jump_from_nav = PageElement(xpath="//div[@id='navbar']//a[text()='register']", describe="从导航栏跳转到注册页面")
    jump_from_body = PageElement(xpath="//a[text()='Register an account']", describe="从正文跳转到注册页面")
    username = PageElement(id_="id_username", describe="用户名")
    password1 = PageElement(id_="id_password1", describe="密码")
    password2 = PageElement(id_="id_password2", describe="确认密码")
    register = PageElement(xpath="//button[@name='submit']", describe="注册按钮")

# module_1_register.py
class Register(unittest.TestCase):
    """注册"""
    def test_1_jump(self):
        """跳转到注册页面"""
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
```

5. 录制用例：打开`Katalon_Recorder`，录制下操作后导出为`Python(Webdriver+unittest)`模式，放入`case`文件夹中对应的`project`、`package`中，按下面的操作修改其中的内容。
```
# 修改文件名为"module_4_xx"的格式
# 在导入命令下加一行
from lib.init import driver
# 删除类中除了test_开头的方法以外的所有内容
class Module4LogoutByRecord(unittest.TestCase):
    def test_module4_logout_by_record(self):
        driver.get("https://dawnredwood-learninglog.herokuapp.com/")
        driver.find_element_by_link_text("log in").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("test")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("test123456")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("log out").click()
```

### 后续优化  
1. 断言失败后面的内容不会执行（trycatch等全部执行完后再报错）  
2. 同一Case类中的用例容易出现耦合  
3. 丰富page_object中的方法  
4. 丰富config中的配置项  
5. 增加网页选取元素后自动生成代码功能  
6. 增加图像识别功能  
7. 增加移动端自动化测试功能  
8. 文件上传下载功能优化