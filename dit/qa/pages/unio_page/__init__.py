from __future__ import annotations
from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException
from dit.qa.pages.unio_page.components.navigation import Navigation
from dit.qa.pages.unio_page.components.report import Report
from dit.qa.pages.unio_page.components.user import User

__all__ = ['UnioPage']


class UnioPage(Page):
    navigation = Navigation(class_name='opn-navbar')
    report = Report(css='[class*="report-view"]')
    footer = Component(class_name="footer")
    user_view = User(class_name='user-view')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.navigation.gerb.visible
                assert self.navigation.dropdown.visible
                assert self.navigation.buttons_block.visible
                assert self.navigation.user_data.visible
                assert self.navigation.logout.visible

                assert self.report.title.visible
                assert self.report.filter.visible
                assert self.report.data.visible
                assert self.report.canvas[0].visible
                assert self.report.container[0].visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_open_transition_person_unio(self) -> None:
        def condition() -> bool:
            try:
                assert self.navigation.gerb.visible
                assert self.navigation.person.visible

                assert self.user_view.download.visible
                assert self.user_view.photo.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
