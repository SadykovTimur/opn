from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    current_data = Component(id="widgetCurrentDate")
    title_ts = Component(xpath="//h1[contains(text(), 'Сведения, содержащиеся в списке объектов, актуальны на')]")
    title_nio = Component(xpath="//h1[text()='Включен ли ваш объект в утвержденный перечень объектов недвижимости']")
    title_gin = Component(xpath="//h1[text()='Результаты инспекционных мероприятий']")
    title_search_ts = Component(xpath="//h1[text()='Найти объект']")
    title_search_gin = Component(xpath="//h1[contains(text(),'Вы можете найти интересующий вас объект при помощи')]")


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
