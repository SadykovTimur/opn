from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Content']


class ContentWrapper(ComponentWrapper):
    hide_block = Components(css='[class="block_with_hide_block"]')
    center_col = Components(css='[class="centerCol"]')
    person = Button(xpath="//a[text()='АБАШИНА ЛИЛИЯ ДМИТРИЕВНА '] ")
    

class Content(Component):
    def __get__(self, instance, owner) -> ContentWrapper:
        return ContentWrapper(instance.app, self.find(instance), self._locator)
