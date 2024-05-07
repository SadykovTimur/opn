from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Content']


class ContentWrapper(ComponentWrapper):
    entity = Components(css='[class="add-entity-btn"]')
    blocks = Component(xpath="//label[text()='Все блоки']")
    untouched = Components(css='[class*="ng-untouched"]')
    cad_number = Component(css='[class*="cad-number"]')
    table_title = Component(css='[class*="table-title"]')
    ok = Component(xpath="//button[text()='OK']")
    clear = Component(xpath="//button[text()='Отмена']")
    form_group = Components(css='[class*="form-group"]')


class Content(Component):
    def __get__(self, instance, owner) -> ContentWrapper:
        return ContentWrapper(instance.app, self.find(instance), self._locator)
