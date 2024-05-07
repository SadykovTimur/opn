from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['User']


class UserWrapper(ComponentWrapper):
    photo = Component(class_name="photo")
    download = Component(xpath="//label[text()='Загрузить фото']")


class User(Component):
    def __get__(self, instance, owner) -> UserWrapper:
        return UserWrapper(instance.app, self.find(instance), self._locator)
