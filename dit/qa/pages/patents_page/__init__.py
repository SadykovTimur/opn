from __future__ import annotations
from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException
from dit.qa.pages.start_patents_page.components.header import Header
from dit.qa.pages.patents_page.components.sidebar import Sidebar
from dit.qa.pages.patents_page.components.content import Content
from dit.qa.pages.patents_page.components.modal import Modal

__all__ = ['PatentsPage']


class PatentsPage(Page):
    header = Header(tag='header')
    sidebar = Sidebar(class_name="left_sidebar")
    content = Content(css='[class*="g-block_white_with_table"]')
    menu = Modal(class_name="modal_block")
    title = Component(xpath="//h1[text()='Реестр карточек ИП']")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.title.visible
                assert self.header.logo.visible
                assert self.header.logout.visible
                assert self.header.patents.visible
                assert self.header.statistics.visible
                assert self.header.protocol.visible
                assert self.header.help.visible

                assert self.sidebar.title.visible
                assert self.sidebar.search.visible
                assert self.sidebar.clear_filter.visible

                return self.content.hide_block[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_filter_value(self) -> None:
        def condition() -> bool:
            try:

                return self.sidebar.value_select.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_data_filter(self, begin: str, end: str) -> None:
        def condition() -> bool:
            try:
                assert self.sidebar.data_begin.value == begin

                return self.sidebar.data_end.value == end

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_filters(self) -> None:
        def condition() -> bool:
            try:
                assert self.title.visible

                return self.content.center_col[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_transition_card(self) -> None:
        def condition() -> bool:
            try:
                assert self.menu.title.visible
                assert self.menu.user.visible
                assert self.menu.print.visible

                return self.menu.table.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

