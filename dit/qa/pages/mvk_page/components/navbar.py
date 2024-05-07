from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Navbar']


class NavbarWrapper(ComponentWrapper):
    gerb = Component(css='[class="opn-navbar__gerb"]')
    menu_registry = Component(id="menu-registry-appeals")
    mvk = Button(xpath='//span[text()="Инструменты"]')
    report = Button(xpath='//span[text()="Отчеты"]')
    info = Component(id="menu-info")
    user_data = Component(css='[class*="user-data"]')
    registry_meeting = Button(id="menu-tools-registry-meeting")
    menu_reports = Button(id="menu-reports-stats")


class Navbar(Component):
    def __get__(self, instance, owner) -> NavbarWrapper:
        return NavbarWrapper(instance.app, self.find(instance), self._locator)
