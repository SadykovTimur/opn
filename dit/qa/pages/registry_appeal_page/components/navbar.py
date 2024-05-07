from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Navbar']


class NavbarWrapper(ComponentWrapper):
    gerb = Component(css='[class="opn-navbar__gerb"]')
    menu_registry = Component(id="dropdownMenuButton")
    nav_register = Component(id="nav-register")
    nav_constructor = Button(id="nav-constructor")
    nav_reports = Component(id="nav-reports")
    user_data = Component(css='[class*="user-data"]')


class Navbar(Component):
    def __get__(self, instance, owner) -> NavbarWrapper:
        return NavbarWrapper(instance.app, self.find(instance), self._locator)
