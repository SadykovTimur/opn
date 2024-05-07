from __future__ import annotations
from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException
from dit.qa.pages.mvk_page.components.navbar import Navbar
from dit.qa.pages.mvk_page.components.parent import Parent
from dit.qa.pages.mvk_page.components.content_table import ContentTable
from dit.qa.pages.mvk_page.components.container import Container
from dit.qa.pages.mvk_page.components.modal import Modal

__all__ = ['MvkPage']


class MvkPage(Page):
    footer = Component(class_name="footer")
    navbar = Navbar(class_name='opn-navbar')
    parent = Parent(class_name="filter-parent-panel")
    content_table = ContentTable(class_name="contentTable")
    container = Container(class_name="content-container")
    modal = Modal(class_name="modal-content")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.navbar.gerb.visible
                assert self.navbar.menu_registry.visible
                assert self.navbar.mvk.visible
                assert self.navbar.report.visible
                assert self.navbar.info.visible
                assert self.navbar.user_data.visible

                assert self.parent.title.visible
                assert self.parent.block_title.visible
                assert self.parent.clear.visible
                assert self.parent.apply.visible

                assert self.content_table.register.visible
                assert self.content_table.expand.visible
                assert self.content_table.select.visible
                assert self.content_table.appeal.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_transition_registry_meetings_mvk(self) -> None:
        def condition() -> bool:
            try:
                assert self.content_table.registry.visible
                assert self.content_table.table[0].visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_transition_card_meetings_mvk(self) -> None:
        def condition() -> bool:
            try:
                assert self.container.title.visible
                assert self.container.block_inputs.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_transition_report_mvk(self) -> None:
        def condition() -> bool:
            try:
                assert self.container.report_title.visible
                assert self.container.report_table.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_registration_new_appeal_mvk(self) -> None:
        def condition() -> bool:
            try:
                assert self.modal.header_title.visible
                assert self.modal.body_appeal.visible
                assert self.modal.ok.visible

                return self.modal.cancel.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
