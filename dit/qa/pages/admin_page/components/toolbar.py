from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Toolbar']


class ToolbarWrapper(ComponentWrapper):
    account = Component(css='[class*="circle-plus"]')
    filter = Component(css='[class*="filter-toogle"]')
    download = Component(css='[class*="download-file"]')


class Toolbar(Component):
    def __get__(self, instance, owner) -> ToolbarWrapper:
        return ToolbarWrapper(instance.app, self.find(instance), self._locator)
