from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField

__all__ = ['Sidebar']


class SidebarWrapper(ComponentWrapper):
    title = Component(xpath="//div[text()='Фильтр по реестру']")
    search = Button(css='[class*="icon-search"]')
    clear_filter = Component(xpath="//div[text()='Очистить фильтр']")
    select = Button(xpath="//span[text()='Все округа']")
    multiselect = Button(xpath="//span[text()='Северо-Восточный административный округ']")
    value_select = Component(xpath="//span[text()='Северо-Восточный административный округ']")
    data_begin = TextField(css='[data-bind*="selectedActivityBeginDate"]')
    data_end = TextField(css='[data-bind*="selectedActivityEndDate"]')


class Sidebar(Component):
    def __get__(self, instance, owner) -> SidebarWrapper:
        return SidebarWrapper(instance.app, self.find(instance), self._locator)
