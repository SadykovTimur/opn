from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Navbar']


class NavbarWrapper(ComponentWrapper):
    system_name = Component(css='[class*="system-name"]')
    dashboard = Button(xpath='//div[text()="Основные"]')
    manager = Component(css='[href="/ippm2/main/task-manager"]')
    task = Component(xpath='//div[text()="Реестр"]')
    sub_task = Component(css='[href="/ippm2/main/sub-task-list/map.ClaimSubTask"]')
    reports = Component(xpath='//div[text()="Отчеты"]')
    admin = Component(xpath='//div[text()="Админка"]')
    icon_user = Component(class_name="icon-user")
    logout = Component(css='[class*="logout"]')
    slide = Component(id="mat-slide-toggle-2")
    slide_toggle = Component(id="mat-slide-toggle-1-input")


class Navbar(Component):
    def __get__(self, instance, owner) -> NavbarWrapper:
        return NavbarWrapper(instance.app, self.find(instance), self._locator)
