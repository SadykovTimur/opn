from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Navbar']


class NavbarWrapper(ComponentWrapper):
    gerb = Component(class_name="gerb")
    system_name = Component(xpath="//div[text()='АРМ Руководителя']")
    unio_nav = Component(id="nav-unio")
    ts_nav = Button(id="nav-ts")
    ipp_nav = Component(id="nav-ipp")
    user = Component(id="current-user")
    logout = Component(id="logout")


class Navbar(Component):
    def __get__(self, instance, owner) -> NavbarWrapper:
        return NavbarWrapper(instance.app, self.find(instance), self._locator)
