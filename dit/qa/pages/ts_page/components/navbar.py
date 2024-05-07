from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Navbar']


class NavbarWrapper(ComponentWrapper):
    title = Component(xpath="//div[text()='ПОДСИСТЕМА ВЕДЕНИЯ УЧЁТА ТОРГОВОГО СБОРА']  ")
    logo = Component(css='[class*="navbar__gerb"]')
    logout = Component(css="[class*='logout-link']")
    registry = Component(xpath="//span[text()='РЕЕСТР ОБЪЕКТОВ']")
    statistics = Component(xpath="//span[text()='ОТЧЕТЫ']")
    protocol = Component(xpath="//span[text()='ИНСТРУМЕНТЫ']")
    help = Component(xpath="//span[text()='ИНФО']")
    objects_eds = Button(id="menu-registry-objects-eds")
    objects_acts = Button(id="menu-registry-objects-acts")


class Navbar(Component):
    def __get__(self, instance, owner) -> NavbarWrapper:
        return NavbarWrapper(instance.app, self.find(instance), self._locator)
