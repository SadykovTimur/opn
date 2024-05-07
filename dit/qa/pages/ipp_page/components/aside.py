from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Aside']


class AsideWrapper(ComponentWrapper):
    header_aside = Component(xpath="//span[text()='Реестр заявлений']")
    apply = Component(xpath="//span[text()='Применить']")
    clear = Component(xpath="//span[text()='Очистить']")


class Aside(Component):
    def __get__(self, instance, owner) -> AsideWrapper:
        return AsideWrapper(instance.app, self.find(instance), self._locator)
