from __future__ import annotations
from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException
from dit.qa.pages.ts_page.components.capblock import Capblock
from dit.qa.pages.ts_page.components.filter import Filter
from dit.qa.pages.ts_page.components.navbar import Navbar
__all__ = ['TsPage']


class TsPage(Page):
    footer = Component(class_name="t-footer")
    navbar = Navbar(class_name="opn-navbar")
    cap_block = Capblock(class_name="cap-block")
    filer = Filter(class_name="filter")


    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.navbar.title.visible
                assert self.navbar.logo.visible
                assert self.navbar.logout.visible
                assert self.navbar.registry.visible
                assert self.navbar.statistics.visible
                assert self.navbar.protocol.visible
                assert self.navbar.help.visible

                assert self.cap_block.trading.visible
                assert self.cap_block.export.visible
                assert self.cap_block.objects.visible
                assert self.cap_block.settings.visible
                assert self.cap_block.table.visible

                assert self.filer.filter_title.visible
                assert self.filer.reset.visible
                assert self.filer.show_red.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_card_ts(self) -> None:
        def condition() -> bool:
            try:
                assert self.navbar.title.visible
                assert self.navbar.logo.visible
                assert self.navbar.logout.visible
                assert self.navbar.registry.visible
                assert self.navbar.statistics.visible
                assert self.navbar.protocol.visible
                assert self.navbar.help.visible

                assert self.cap_block.title.visible
                assert self.cap_block.object_table.visible
                assert self.cap_block.block_section[0].visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_transition_registry_electronic_document_ts(self) -> None:
        def condition() -> bool:
            try:
                assert self.cap_block.registry_electronic.visible
                assert self.cap_block.export.visible
                assert self.cap_block.settings.visible

                assert self.filer.filter_title.visible
                assert self.filer.save.visible
                assert self.filer.show.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_transition_registry_act_ts(self) -> None:
        def condition() -> bool:
            try:
                assert self.cap_block.registry_act.visible
                assert self.cap_block.objects.visible

                assert self.filer.filter_title.visible
                assert self.filer.save.visible
                assert self.filer.show.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_transition_detailed_registry_act_ts(self) -> None:
        def condition() -> bool:
            try:
                assert self.navbar.title.visible
                assert self.navbar.logo.visible
                assert self.navbar.logout.visible
                assert self.navbar.registry.visible
                assert self.navbar.statistics.visible
                assert self.navbar.protocol.visible
                assert self.navbar.help.visible

                assert self.cap_block.registry_act.visible
                assert self.cap_block.export.visible
                assert self.cap_block.settings.visible
                assert self.cap_block.card_object[0].visible
                assert self.cap_block.card_table[0].visible

                assert self.filer.filter_title.visible
                assert self.filer.save.visible
                assert self.filer.show.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
