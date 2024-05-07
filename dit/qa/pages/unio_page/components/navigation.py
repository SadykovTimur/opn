from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Navigation']


class NavigationWrapper(ComponentWrapper):
    gerb = Component(css='[class*="navbar__gerb"]')
    dropdown = Component(id="dropdownMenuButton")
    buttons_block = Component(css='[class*="buttons-block"]')
    register = Button(id="icon-register-oks")
    user_data = Button(xpath="//a[text()='Бот ДИТ ']")
    logout = Component(css='[class*="logout-link"]')
    gin = Button(id="icon-gin-arm")
    gin_list = Button(id="gin-list")
    person = Component(css='[class*="system-name"]')


class Navigation(Component):
    def __get__(self, instance, owner) -> NavigationWrapper:
        return NavigationWrapper(instance.app, self.find(instance), self._locator)
