from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Table']


class TableWrapper(ComponentWrapper):
    line = Button(xpath="(//div[text()='Нет данных'])[3]")


class Table(Component):
    def __get__(self, instance, owner) -> TableWrapper:
        return TableWrapper(instance.app, self.find(instance), self._locator)
