from lib.page_object import PageObject, PageElement
from lib.init import test_time


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
