from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField

__all__ = ['TreePanel']


class TreePanelWrapper(ComponentWrapper):
    search_tree = TextField(id="search_tree")
    search = Button(css='[class*="search-btn"]')
    inn = Component(class_name="t-inn")
    name = Component(class_name="t-name")
    checkbox = Button(css='[id*="lid_legal"]')
    show = Button(id="btn_display")
    tree = Component(xpath='//span[text()="Дерево показателей"]')


class TreePanel(Component):
    def __get__(self, instance, owner) -> TreePanelWrapper:
        return TreePanelWrapper(instance.app, self.find(instance), self._locator)
