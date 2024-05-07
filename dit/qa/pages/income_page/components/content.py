from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Content']


class ContentWrapper(ComponentWrapper):
    logo = Component(id="h-logo")
    news = Component(css='[href="index.php?show=news"]')
    inds = Button(css='[href="index.php?show=inds"]')
    input = Button(css='[href="index.php?show=input"]')
    show_legal = Button(css='[href="index.php?show=legal"]')
    reports = Component(css='[href="index.php?show=reports_null"]')
    present = Component(css='[href="index.php?show=present_null"]')
    map = Component(css='[href="index.php?show=map"]')
    book = Component(css='[class="book_ico"]')
    navi = Component(css='[class="navi_ico"]')
    help = Component(css='[class="help_ico"]')
    docs = Component(css='[class="docs_ico"]')
    user = Component(css='[class="user_ico"]')
    title_registry = Component(xpath="//h1[text()='Реестр ЮЛ']")
    data = Component(xpath="//h1[text()='Ввод данных']")
    title_editor = Component(xpath="//h1[text()='Редактор показателей']")


class Content(Component):
    def __get__(self, instance, owner) -> ContentWrapper:
        return ContentWrapper(instance.app, self.find(instance), self._locator)
