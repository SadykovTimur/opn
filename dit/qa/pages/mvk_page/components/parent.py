from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button


__all__ = ['Parent']


class ParentWrapper(ComponentWrapper):
    title = Component(xpath="//div[text()='РЕЕСТР ОБРАЩЕНИЙ И ОБЪЕКТОВ']")
    block_title = Component(xpath="//div[text()='ПОЛНЫЙ СПИСОК ФИЛЬТРОВ']")
    clear = Component(xpath="//button[text()='Очистить']")
    apply = Component(xpath="//button[text()='Применить']")


class Parent(Component):
    def __get__(self, instance, owner) -> ParentWrapper:
        return ParentWrapper(instance.app, self.find(instance), self._locator)
