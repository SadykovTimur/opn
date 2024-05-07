from __future__ import annotations
from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException
from dit.qa.pages.admin_page.components.toolbar import Toolbar
from dit.qa.pages.admin_page.components.navbar import Navbar
from dit.qa.pages.admin_page.components.content import Content

__all__ = ['AdminPage']


class AdminPage(Page):
    footer = Component(tag="footer")
    navbar = Navbar(css='[class*="opn-navbar"]')
    toolbar = Toolbar(css='[class*="top-toolbar"]')
    content = Content(css='[class*="view-content"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.navbar.gerb.visible
                assert self.navbar.menu_registry.visible
                assert self.navbar.users.visible
                assert self.navbar.roles.visible
                assert self.navbar.journal.visible
                assert self.navbar.instrument.visible
                assert self.navbar.info.visible
                assert self.navbar.pi.visible
                assert self.navbar.user_data.visible

                assert self.toolbar.account.visible
                assert self.toolbar.filter.visible
                assert self.toolbar.download.visible

                assert self.content.user_list.visible
                assert self.content.sortable[0].visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_transition_section_role_admin(self) -> None:
        def condition() -> bool:
            try:
                assert self.content.list_role.visible
                assert self.content.group_role.visible
                assert self.content.line_group[0].visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_open_role_group_admin(self) -> None:
        def condition() -> bool:
            try:
                assert self.content.list_role.visible
                assert self.content.group_role.visible
                assert self.content.line_group[0].visible
                assert self.content.table[0].visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()