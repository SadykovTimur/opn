from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Capblock']


class CapBlockWrapper(ComponentWrapper):
    trading = Component(xpath="//label[text()='Реестр торговых объектов']")
    export = Component(css='[class*="export"]')
    objects = Button(css='[class*="showObjects"]')
    settings = Component(css='[class*="colSettings"]')
    table = Component(css='[class*="tableMode"]')
    pictogram = Button(css='[class*="glyphicon-info-sign"]')
    title = Component(xpath="//summary[text()='ОБЩАЯ ИНФОРМАЦИЯ О ТОРГОВОМ ОБЪЕКТЕ']")
    object_table = Component(css='[class*="objectLinkTable"]')
    block_section = Components(css='[class*="blockSection"] ')
    registry_electronic = Component(xpath="//label[text()='Реестр электронных документов']")
    registry_act = Component(xpath="//label[text()='Реестр Актов']")
    card_object = Components(css='[class*="GB4RCFIBMH"]')
    card_table = Components(css='[class*="GB4RCFIBNG"]')


class Capblock(Component):
    def __get__(self, instance, owner) -> CapBlockWrapper:
        return CapBlockWrapper(instance.app, self.find(instance), self._locator)
