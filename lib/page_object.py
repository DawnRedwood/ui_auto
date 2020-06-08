from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from lib.init import root_url, driver, sleep_time


LOCATOR_LIST = {
    'css': By.CSS_SELECTOR,
    'id_': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'class_name': By.CLASS_NAME,
}


class PageObject:

    def __init__(self):
        self._driver = driver
        self._number = 0
        self._father_number = {0: 0}

    def get(self, url=root_url):
        sleep(sleep_time)
        self._driver.get(url)
        sleep(sleep_time)
    
    def refresh(self):
        sleep(sleep_time)
        self._driver.refresh()
        sleep(sleep_time)

    def frame(self, frame):
        sleep(sleep_time)
        self._driver.switch_to.frame(frame)
        sleep(sleep_time)

    def default_content(self):
        sleep(sleep_time)
        self._driver.switch_to.default_content()
        sleep(sleep_time)
    
    def next_window(self):
        sleep(sleep_time)
        _father = self._number
        self._number = len(self._driver.window_handles) - 1
        self._father_number[self._number] = _father
        self._driver.switch_to.window(self._driver.window_handles[self._number])
        sleep(sleep_time)
        
    def previous_window(self):
        sleep(sleep_time)
        self._number = self._father_number[self._number]
        self._driver.switch_to.window(self._driver.window_handles[self._number])
        sleep(sleep_time)

    def wait(self, *elems, timeout=10): # TODO: 优化为等待时间超时，引发ERROR
        for elem in elems:
            for i in range(timeout):
                if elem is not None:
                    if elem.is_displayed():
                        break
                    else:
                        sleep(1)
                else:
                    sleep(1)

    def clear(self, *elems):
        for elem in elems:
            if self.exist(elem):
                elem.send_keys(Keys.CONTROL, 'a')
                elem.send_keys(Keys.DELETE)

    def exist(self, *elems):
        try:
            for elem in elems:
                if not elem.is_displayed():
                    return False
            else:
                return True
        except Exception as e:
            return False

    def screenshot(self, test, num=2): # test: test_case的self, num: 第一次截图时传1
        if num == 1:
            test.imgs = []
        if hasattr(test, "imgs"):
            test.imgs.append(driver.get_screenshot_as_base64())

    def select(self, elem, text): # elem: 下拉框, text: 想要选中的值
        if self.exist(elem) and text:
            select = Select(elem)
            select.select_by_visible_text(text)


class PageElement(object):

    def __init__(self, timeout=4, describe="", context=False, **kwargs):
        self.time_out = timeout
        self.describe = describe
        self.has_context = bool(context)
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        self.k, self.v = next(iter(kwargs.items()))
        self.locator = (LOCATOR_LIST[self.k], self.v)

    def get_element(self, context):
        try:
            elem = context.find_element(*self.locator)
        except NoSuchElementException:
            return None
        else:
            try:
                style_red = 'arguments[0].style.border="2px solid red"'
                context.execute_script(style_red, elem)
            except BaseException as e:
                return elem
            return elem

    def find(self, context):
        for i in range(1, self.time_out):
            if self.get_element(context) is not None:
                return self.get_element(context)
        else:
            return self.get_element(context)

    def __get__(self, instance, owner, context=None): # 此处instance指父类PageObject实例对象,owner指实例类型
        if not instance:
            return None
        if not context and self.has_context:
            return lambda ctx: self.__get__(instance, owner, context=ctx)
        if not context:
            context = instance._driver
        sleep(sleep_time)
        return self.find(context)

    def __set__(self, instance, value):
        elem = self.__get__(instance, instance.__class__)
        elem.send_keys(value)
