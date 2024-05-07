from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Report']


class ReportWrapper(ComponentWrapper):
    title = Component(xpath='//b[text()="Отчет о формировании Перечня объектов недвижимого имущества для налогообложения от кадастровой стоимости на 2025 год (количество, площадь и кадастровая стоимость) по состоянию на "]')
    canvas = Components(class_name="report-canvas")
    container = Components(class_name="pairs-charts-caption")
    filter = Component(xpath="//div[text()='ФИЛЬТР']")
    data = Component(xpath="//label[text()='Дата: ']")


class Report(Component):
    def __get__(self, instance, owner) -> ReportWrapper:
        return ReportWrapper(instance.app, self.find(instance), self._locator)
