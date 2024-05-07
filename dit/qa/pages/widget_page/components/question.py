from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Question']


class QuestionWrapper(ComponentWrapper):
    question = Component(xpath="//h3[text()='Часто задаваемые вопросы'] ")
    item_ts = Components(css='[class="g_blue"]')
    item_nio = Components(css='[class="blue"]')


class Question(Component):
    def __get__(self, instance, owner) -> QuestionWrapper:
        return QuestionWrapper(instance.app, self.find(instance), self._locator)
