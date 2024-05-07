from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Modal']


class ModalWrapper(ComponentWrapper):
    title = Component(xpath="//span[text()='Карточка ИП']")
    user = Component(xpath="//span[text()='АБАШИНА ЛИЛИЯ ДМИТРИЕВНА']")
    print = Component(css='[print="person"]')
    table = Component(css='[class*="g-block-edit"]')


class Modal(Component):
    def __get__(self, instance, owner) -> ModalWrapper:
        return ModalWrapper(instance.app, self.find(instance), self._locator)
