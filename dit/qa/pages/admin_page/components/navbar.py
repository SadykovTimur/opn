from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Navbar']


class NavbarWrapper(ComponentWrapper):
    gerb = Component(css='[class="opn-navbar__gerb"]')
    menu_registry = Component(id="dropdownMenuButton")
    users = Component(xpath="//span[text()='ПОЛЬЗОВАТЕЛИ']")
    roles = Button(xpath="//span[text()='РОЛИ']")
    journal = Component(xpath="//span[text()='ЖУРНАЛ']")
    instrument = Component(xpath="//span[text()='ИНСТРУМЕНТЫ']")
    info = Component(xpath="//span[text()='ИНФО']")
    pi = Component(xpath="//span[text()='ПИ']")
    user_data = Component(css='[class*="user-data"]')


class Navbar(Component):
    def __get__(self, instance, owner) -> NavbarWrapper:
        return NavbarWrapper(instance.app, self.find(instance), self._locator)
