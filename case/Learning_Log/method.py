"""模块1公共方法"""
# 注册
from case.Learning_Log.package_1_user.data_1_register import Page as RegisterPage
def register(username, password1, password2):
    page = RegisterPage()
    page.get(page.url)
    if page.exist(page.username, page.password1, page.password2, page.register):
        page.username = username
        page.password1 = password1
        page.password2 = password2
        page.register.click()

# 登录
from case.Learning_Log.package_1_user.data_2_login import Page as LoginPage, data as login_data
def login(username=login_data["correct_username"], password=login_data["correct_password"]):
    page = LoginPage()
    page.get(page.url)
    if page.exist(page.username, page.password, page.login):
        page.username = username
        page.password = password
        page.login.click()

# 退出
from case.Learning_Log.package_1_user.data_3_logout import Page as LogoutPage
def logout():
    page = LogoutPage()
    page.get()
    if page.exist(page.logout):
        page.logout.click()
