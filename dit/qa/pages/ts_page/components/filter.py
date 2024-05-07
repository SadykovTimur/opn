from coms.qa.frontend.pages.component import Component, ComponentWrapper


__all__ = ['Filter']


class FilterWrapper(ComponentWrapper):
    filter_title = Component(xpath="//label[text()='ПАРАМЕТРЫ И ФИЛЬТРЫ']")
    reset = Component(css='[class*="grey-button"]')
    show_red = Component(css='[class*="red-button"]')
    save = Component(xpath="//button[text()='Сохранить как новый']")
    show = Component(xpath="//button[text()='Показать']")


class Filter(Component):
    def __get__(self, instance, owner) -> FilterWrapper:
        return FilterWrapper(instance.app, self.find(instance), self._locator)
