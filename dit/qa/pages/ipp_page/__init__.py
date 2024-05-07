from __future__ import annotations
from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException
from dit.qa.pages.ipp_page.components.aside import Aside
from dit.qa.pages.ipp_page.components.navbar import Navbar
from dit.qa.pages.ipp_page.components.main import Main

__all__ = ['IppPage']


class IppPage(Page):
    footer = Component(class_name="footer")
    navbar = Navbar(class_name="navbar")
    main_aside = Aside(class_name="main__aside")
    main_wrapper = Main(class_name="main__wrapper")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.navbar.system_name.visible
                assert self.navbar.dashboard.visible
                assert self.navbar.manager.visible
                assert self.navbar.task.visible
                assert self.navbar.sub_task.visible
                assert self.navbar.reports.visible
                assert self.navbar.admin.visible
                assert self.navbar.icon_user.visible
                assert self.navbar.logout.visible
                assert self.navbar.slide.visible
                assert self.navbar.slide_toggle.visible

                assert self.main_aside.header_aside.visible
                assert self.main_aside.apply.visible
                assert self.main_aside.clear.visible

                assert self.main_wrapper.refresh.visible
                assert self.main_wrapper.mark.visible
                assert self.main_wrapper.away.visible
                assert self.main_wrapper.start.visible
                assert self.main_wrapper.stop.visible
                assert self.main_wrapper.download.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_card_statement(self) -> None:
        def condition() -> bool:
            try:
                assert self.main_wrapper.card_statement.visible
                assert self.main_wrapper.print.visible
                assert self.main_wrapper.application.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_chapter_main_factors(self) -> None:
        def condition() -> bool:
            try:
                assert self.main_wrapper.factors.visible
                assert self.main_wrapper.all_apllication.visible
                assert self.main_wrapper.check.visible
                assert self.main_wrapper.accept.visible
                assert self.main_wrapper.analytic_block[0].visible
                assert self.main_wrapper.characteristics.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
