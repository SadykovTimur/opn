from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['SettingsPanel']


class SettingsPanelWrapper(ComponentWrapper):
    apply_btn = Button(id="btn_apply")
    title = Component(xpath="//span[text()='Параметры и фильтры']")
    coff_filter = Button(id="coff_filter")


class SettingsPanel(Component):
    def __get__(self, instance, owner) -> SettingsPanelWrapper:
        return SettingsPanelWrapper(instance.app, self.find(instance), self._locator)
