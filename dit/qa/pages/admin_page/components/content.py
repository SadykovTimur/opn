from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Content']


class ContentWrapper(ComponentWrapper):
    user_list = Component(xpath="//h2[text()='Список пользователей']")
    filter = Component(xpath="//b[text()='ФИЛЬТРЫ']")
    clear = Component(xpath="//button[text()='Очистить']")
    apply = Component(xpath="//button[text()='Применить']")
    sortable = Components(css='[class="sortable "]')
    list_role = Component(xpath="//h2[text()='Список ролей']")
    group_role = Component(xpath="//b[text()='Группы ролей']")
    line_group = Components(css='[class="line-group"]')
    admin = Button(xpath="//div[text()='ADMIN']")
    title_admin = Component(xpath="//b[contains(text(),'Роли группы')]")
    table = Components(xpath="//tr/td")


class Content(Component):
    def __get__(self, instance, owner) -> ContentWrapper:
        return ContentWrapper(instance.app, self.find(instance), self._locator)
