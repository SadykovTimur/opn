from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    title = Component(xpath="//h1[text()='ПОДСИСТЕМА ВЕДЕНИЯ РЕЕСТРА ИНДИВИДУАЛЬНЫХ ПРЕДПРИНИМАТЕЛЕЙ']")
    logo = Component(class_name="header__logo")
    header_login = Component(xpath="//span[text()='Авторизация пользователей']")
    logout = Component(id="logoutForm")
    patents = Component(xpath="//span[text()='Реестр объектов']")
    statistics = Component(xpath="//span[text()='Отчеты']")
    protocol = Component(xpath="//span[text()='Инструменты']")
    help = Component(xpath="//span[text()='Инфо']")


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
