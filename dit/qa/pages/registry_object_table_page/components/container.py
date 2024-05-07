from coms.qa.frontend.pages.component import Component,Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Container']


class ContainerWrapper(ComponentWrapper):
    table_value = Components(css='[class ="GB4RCFIBNG"]')
    table_body = Components(css='[class ="GB4RCFIBMH"]')
    map = Button(css='[class*="mapButton"]')
    table_view = Component(css='[class*="tableViewButton"]')
    upload = Component(css='[class*="uploadButton"]')
    reference = Component(css='[class*="referenceButton"]')
    list = Component(xpath="//div[contains(text(),'Найдено объектов:')]")
    wrapper = Components(css='[class*="gwt-TabBarItem-wrapper"]')
    field_group = Component(css='[class*="field-group"]')


class Container(Component):
    def __get__(self, instance, owner) -> ContainerWrapper:
        return ContainerWrapper(instance.app, self.find(instance), self._locator)
