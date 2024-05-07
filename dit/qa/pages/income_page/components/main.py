from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Main']


class MainWrapper(ComponentWrapper):
    news_block = Components(css='[class="newsBlock"]')
    search_name = Component(id="searchName")
    search = Component(id="search")
    reset = Component(id="btn_del_reset")


    

class Main(Component):
    def __get__(self, instance, owner) -> MainWrapper:
        return MainWrapper(instance.app, self.find(instance), self._locator)
