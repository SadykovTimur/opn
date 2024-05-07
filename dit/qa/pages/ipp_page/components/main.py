from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Main']


class MainWrapper(ComponentWrapper):
    refresh = Component(xpath="//span[contains(text(),'Обновить')]")
    mark = Component(xpath="//span[contains(text(),'Отметить')]")
    away = Component(xpath="//span[contains(text(),'Убрать')] ")
    start = Component(xpath="//span[contains(text(),' Старт ')] ")
    stop = Component(xpath="//span[contains(text(),' Стоп ')]")
    download = Component(xpath="//span[contains(text(),' Скачать выгрузку ')]")
    open = Button(xpath='(//button[@class="btn default"])[6]')
    card_statement = Component(xpath="//div[text()='Карточка заявления']")
    print = Component(xpath="//span[text()='Печатная форма']")
    application = Component(class_name="application-stats")
    factors = Component(xpath="//h2[text()='Основные показатели']")
    all_apllication = Component(xpath="//h4[text()='Всего заявлений']")
    check = Component(xpath="//h4[text()='Проверка комплектности']")
    accept = Component(xpath="//h4[text()='Принято к рассмотрению']")
    analytic_block = Components(css='[class="analytics-block-item"]')
    characteristics = Component(id="main-characteristics")


class Main(Component):
    def __get__(self, instance, owner) -> MainWrapper:
        return MainWrapper(instance.app, self.find(instance), self._locator)
