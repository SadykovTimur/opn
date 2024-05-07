from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button


__all__ = ['Modal']


class ModalWrapper(ComponentWrapper):
    header_title = Component(xpath="//h4[text()='Параметры поступившего обращения']")
    body_appeal = Component(class_name="modal-body")
    ok = Component(xpath="//button[text()='OK']")
    cancel = Component(xpath="//button[text()='Отмена']")


class Modal(Component):
    def __get__(self, instance, owner) -> ModalWrapper:
        return ModalWrapper(instance.app, self.find(instance), self._locator)
