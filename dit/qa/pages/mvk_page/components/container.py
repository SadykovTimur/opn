from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button


__all__ = ['Container']


class ContainerWrapper(ComponentWrapper):
    header = Component(xpath="//h4[text()='Объекты, включенные в Перечень 2014 года']")
    close = Component(class_name="close")
    table = Component(class_name="modal-body")
    footer = Component(class_name="modal-footer")
    title = Component(xpath="//h3[text()='ПРОВЕДЕНИЕ ЗАСЕДАНИЯ МВК']")
    block_inputs = Component(class_name="inputs-block")
    report_title = Component(xpath="//h3[text()='Статистический отчет о количестве объектов в обращениях, поданных в ДЭПиР']")
    report_table = Component(class_name="stat-report")


class Container(Component):
    def __get__(self, instance, owner) -> ContainerWrapper:
        return ContainerWrapper(instance.app, self.find(instance), self._locator)
