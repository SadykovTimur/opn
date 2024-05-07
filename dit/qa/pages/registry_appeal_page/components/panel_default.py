from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Panel']


class PanelWrapper(ComponentWrapper):
    title = Component(css='[class*="title"]')
    head_table = Component(css='[class*="head-table"]')
    period = Components(css='[class*="period-col"]')
    mission = Components(css='[class*="mission-col"]')
    answer = Components(css='[class*="answer-col"]')

class Panel(Component):
    def __get__(self, instance, owner) -> PanelWrapper:
        return PanelWrapper(instance.app, self.find(instance), self._locator)
