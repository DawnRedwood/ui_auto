from lib.page_object import PageObject, PageElement
from lib.init import test_time


data = {
    "topic_name": "Topic " + test_time,
    "entry_content": "Entry " + test_time,
    "edited_entry_content": "Edit Entry " + test_time,
}

class Page(PageObject):
    # 常用元素
    url = "https://dawnredwood-learninglog.herokuapp.com/topics/"
    topics_url = "https://dawnredwood-learninglog.herokuapp.com/topics/"
    correct_topic_url = "https://dawnredwood-learninglog.herokuapp.com/topics/5/"
    wrong_topic_url = "https://dawnredwood-learninglog.herokuapp.com/topics/1/"
    correct_add_entry_url = "https://dawnredwood-learninglog.herokuapp.com/new_entry/5/"
    wrong_add_entry_url = "https://dawnredwood-learninglog.herokuapp.com/new_entry/1/"
    correct_edit_entry_url = "https://dawnredwood-learninglog.herokuapp.com/edit_entry/5/"
    wrong_edit_entry_url = "https://dawnredwood-learninglog.herokuapp.com/edit_entry/1/"
    error_404 = PageElement(xpath="//h2[text()='The item you requested is not available. (404)']", describe="错误消息404")
    error_500 = PageElement(xpath="//h2[text()='There has been an internal error. (500)']", describe="错误消息500")
    login = PageElement(xpath="//button[text()='log in']", describe="登录按钮")
    topics = PageElement(xpath="//a[text()='Topics']", describe="导航栏中的Topics")
    topic = PageElement(xpath="//a[text()='%s']" % data["topic_name"], describe="主题列表、新增与编辑条目中的主题链接")
    add_new_topic = PageElement(xpath="//a[text()='Add new topic']", describe="新增主题按钮")
    topic_name = PageElement(xpath="//input[@id='id_text']", describe="新增主题中的主题名称")
    entry = PageElement(xpath="//p[text()='%s']" % data["entry_content"], describe="条目列表中的条目内容")
    edited_entry = PageElement(xpath="//p[text()='%s']" % data["edited_entry_content"], describe="条目列表中编辑过的条目内容")
    add_new_entry = PageElement(xpath="//a[text()='add new entry']", describe="新增条目按钮")
    edit_entry = PageElement(xpath="//p[contains(text(), '%s')]/../../div[1]//a[contains(text(), 'edit entry')]" % data["entry_content"], describe="编辑条目按钮")
    entry_content = PageElement(xpath="//textarea[@id='id_text']", describe="新增与编辑条目中的条目内容")
    submit = PageElement(xpath="//button[@name='submit']", describe="提交")
