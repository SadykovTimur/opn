from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button


__all__ = ['Modal']


class ModalParentWrapper(ComponentWrapper):
    header = Component(xpath="//h4[text()='Объекты, включенные в Перечень 2014 года']")
    close = Component(class_name="close")
    table = Component(class_name="modal-body")
    footer = Component(class_name="modal-footer")


class Modal(Component):
    def __get__(self, instance, owner) -> ModalParentWrapper:
        return ModalParentWrapper(instance.app, self.find(instance), self._locator)
