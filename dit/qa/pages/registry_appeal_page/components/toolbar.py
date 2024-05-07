from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Toolbar']


class ToolbarWrapper(ComponentWrapper):
    title = Component(xpath="//span[text()='Все обращения']")
    switch = Button(css='[class="material-switch"]')
    reg_appeal = Button(css='[class*="grey-button"]')
    title_subject = Component(xpath="//div[text()='Выбор тематики блоков: ']")
    title_block = Component(xpath="//div[text()='Наименование блока: ']")
    card_app = Component(xpath="//b[text()='Карточка обращения']")


class Toolbar(Component):
    def __get__(self, instance, owner) -> ToolbarWrapper:
        return ToolbarWrapper(instance.app, self.find(instance), self._locator)
