from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button


__all__ = ['FilterParent']


class FilterParentWrapper(ComponentWrapper):
    navigation = Component(xpath="//label[text()='НАВИГАЦИЯ']")
    list = Components(css='[class="glyphicon glyphicon-list-alt"]')
    flag = Component(class_name="flag")
    list_2014 = Button(xpath='//label[text()=" Перечень 2014"]')
    list_2015 = Component(xpath='//label[text()=" Перечень 2015"]')
    list_2016 = Component(xpath='//label[text()=" Перечень 2016"]')
    list_2017 = Component(xpath='//label[text()=" Перечень 2017"]')
    current_list = Component(xpath='//label[text()=" Перечень текущего года"]')
    project_list = Component(xpath='//label[text()=" Проект Перечня на следующий год"]')
    gin = Component(xpath='//label[text()=" ГИН"]')
    information = Component(xpath="//label[text()=' Общие сведения']")
    trade_objects = Component(xpath="//label[text()=' Сбор информации о торговых объектах']")
    appeal = Component(xpath="//label[text()=' Работа по рассмотрению обращений']")
    act = Component(xpath="//label[text()=' Работа по актам']")
    results = Component(xpath="//label[text()=' Итоги работы']")
    unio = Component(xpath="//label[text()=' Связь с УНИО']")
    archive = Component(xpath="//label[text()=' Архив']")
    indicator = Button(xpath="//label[text()='1 792']")


class FilterParent(Component):
    def __get__(self, instance, owner) -> FilterParentWrapper:
        return FilterParentWrapper(instance.app, self.find(instance), self._locator)
