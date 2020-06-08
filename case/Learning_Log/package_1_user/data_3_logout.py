from lib.page_object import PageObject, PageElement


data = {}

class Page(PageObject):
    logout = PageElement(xpath="//div[@id='navbar']//a[text()='log out']", describe="退出按钮")
