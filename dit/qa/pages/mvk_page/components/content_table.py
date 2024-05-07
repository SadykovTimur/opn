from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button


__all__ = ['ContentTable']


class ContentTableWrapper(ComponentWrapper):
    register = Component(xpath="//div[text()='Реестр обращений и объектов']")
    expand = Component(xpath="//button[text()='Развернуть все']")
    select = Component(xpath="//button[text()='Выбрать все объекты']")
    appeal = Button(xpath="//button[text()='Зарегистрировать обращение']")
    registry = Component(xpath="//div[text()='Реестр заседаний']")
    table = Components(css='[class*="GB4RCFIBDH"]')
    table_data = Button(xpath='//a[text()="24-04-2024"]')


class ContentTable(Component):
    def __get__(self, instance, owner) -> ContentTableWrapper:
        return ContentTableWrapper(instance.app, self.find(instance), self._locator)
