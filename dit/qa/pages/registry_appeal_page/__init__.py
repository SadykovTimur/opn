from __future__ import annotations

from _pytest.fixtures import FixtureRequest
from coms.qa.core.helpers import wait_for
from coms.qa.fixtures.application import Application
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException
from dit.qa.pages.registry_appeal_page.components.navbar import Navbar
from dit.qa.pages.registry_appeal_page.components.panel_default import Panel
from dit.qa.pages.registry_appeal_page.components.toolbar import Toolbar
from dit.qa.pages.registry_appeal_page.components.content import Content

__all__ = ['RegistryAppealPage']


class RegistryAppealPage(Page):
    navbar = Navbar(tag="nav")
    toolbar = Toolbar(css='[class*="top-toolbar"]')
    footer = Component(tag="footer")
    panel_default = Panel(css='[class*="panel-default"]')
    content = Content(css='[class*="view-content"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.navbar.gerb.visible
                assert self.navbar.menu_registry.visible
                assert self.navbar.nav_reports.visible
                assert self.navbar.nav_register.visible
                assert self.navbar.nav_constructor.visible
                assert self.navbar.user_data.visible

                assert self.toolbar.title.visible
                assert self.toolbar.switch.visible
                assert self.toolbar.reg_appeal.visible

                assert self.panel_default.title.visible
                assert self.panel_default.head_table.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_filer_message_registry_appeal(self) -> None:
        def condition() -> bool:
            try:
                assert self.panel_default.mission[0].visible
                assert self.panel_default.answer[0].visible

                return self.panel_default.period[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_transition_constructor_response_registry_appeal(self) -> None:
        def condition() -> bool:
            try:
                assert self.toolbar.title_subject.visible
                assert self.content.entity[0].visible
                assert self.content.blocks.visible
                assert self.content.untouched[0].visible

                return self.toolbar.title_block.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_registration_new_registry_appeal(self) -> None:
        self.driver.switch_to.window(self.driver.window_handles[-1])

        def condition() -> bool:
            try:
                assert self.toolbar.card_app.visible

                assert self.content.cad_number.visible
                assert self.content.table_title.visible
                assert self.content.ok.visible
                assert self.content.clear.visible

                return self.content.form_group[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
