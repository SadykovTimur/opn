from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button


__all__ = ['Content']


class ContentWrapper(ComponentWrapper):
    favorites = Component(xpath="//label[text()='ИЗБРАННОЕ']")
    list_14 = Component(xpath="//label[text()='ПЕРЕЧЕНЬ 2014']")
    tax_objects = Component(css='[class*="UNIO_TAX_OBJECTS_2014"]')
    declared_objects = Component(css='[class*="UNIO_DECLARED_OBJ_2014"]')
    declaration_objects = Component(css='[class*="UNIO_TAX_OBJECTS_W_RIGHT_OR_DECLARATION_2014"]')
    mark = Component(xpath="//div[contains(text(),'Общие сведения')]")
    act_objects = Component(css='[class*="FNS_AND_ACT_OBJECTS"]')
    act_taxable = Component(css='[class*="FNS_AND_ACT_TAXABLE"]')


class Content(Component):
    def __get__(self, instance, owner) -> ContentWrapper:
        return ContentWrapper(instance.app, self.find(instance), self._locator)
