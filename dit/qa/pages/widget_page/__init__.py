from __future__ import annotations
from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException
from dit.qa.pages.widget_page.components.header import Header
from dit.qa.pages.widget_page.components.question import Question

__all__ = ['WidgetPage']


class WidgetPage(Page):
    footer = Component(css='[class*="footer"]')
    header = Header(tag='h1')
    questions = Question(css='[class*="questions"]')
    search = Button(css='[class*="btn-service"]')
    grid = Component(class_name="b-grid")
    tabs = Component(class_name="tabs")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.title_ts.visible
                assert self.header.current_data.visible

                assert self.questions.question.visible
                assert self.questions.item_ts[0].visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_widget_nio(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.title_nio.visible

                assert self.questions.question.visible
                assert self.questions.item_nio[0].visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_widget_gin(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_transition_search_widget_ts(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.title_search_ts.visible

                assert self.grid.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_transition_search_widget_nio(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.title_nio.visible
                assert self.tabs.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_transition_search_widget_gin(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.visible
                assert self.grid.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
