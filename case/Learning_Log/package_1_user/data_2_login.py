from lib.page_object import PageObject, PageElement


data = {
    "wrong_username": ["", "test", "test"],
    "wrong_password": ["", "", "test"],
    "correct_username": "test",
    "correct_password": "test123456"
}

class Page(PageObject):
    url = "https://dawnredwood-learninglog.herokuapp.com/users/login/"
    redirect_url = "https://dawnredwood-learninglog.herokuapp.com/users/login/?next=/topics/"
    topics_url = "https://dawnredwood-learninglog.herokuapp.com/topics/"
    redirect = PageElement(xpath="//div[@id='navbar']//a[text()='Topics']", describe="从Topics重定向到登录页面")
    jump = PageElement(xpath="//div[@id='navbar']//a[text()='log in']", describe="从导航栏跳转到登录页面")
    username = PageElement(id_="id_username", describe="用户名")
    password = PageElement(id_="id_password", describe="密码")
    login = PageElement(xpath="//button[@name='submit']", describe="登录按钮")
