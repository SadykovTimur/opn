from __future__ import annotations
from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException
from dit.qa.pages.arm_lead_page.components.navbar import Navbar
from dit.qa.pages.arm_lead_page.components.filter_panel import FilterParent
from dit.qa.pages.arm_lead_page.components.content import Content
from dit.qa.pages.arm_lead_page.components.modal import Modal

__all__ = ['ArmLeadPage']


class ArmLeadPage(Page):
    footer = Component(class_name="footer")
    navbar = Navbar(class_name="navbar")
    content = Content(class_name="arm-content")
    filter = FilterParent(css='[class*="filter-parent"]')
    modal = Modal(class_name="modal-content")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.navbar.gerb.visible
                assert self.navbar.system_name.visible
                assert self.navbar.unio_nav.visible
                assert self.navbar.ts_nav.visible
                assert self.navbar.ipp_nav.visible
                assert self.navbar.user.visible
                assert self.navbar.logout.visible

                assert self.filter.navigation.visible
                assert self.filter.flag.visible
                assert self.filter.list_2014.visible
                assert self.filter.list_2015.visible
                assert self.filter.list_2016.visible
                assert self.filter.list_2017.visible
                assert self.filter.current_list.visible
                assert self.filter.project_list.visible
                assert self.filter.gin.visible

                assert self.content.favorites.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_transition_group_arm_lead(self) -> None:
        def condition() -> bool:
            try:
                assert self.content.tax_objects.visible
                assert self.content.declared_objects.visible
                assert self.content.declaration_objects.visible
                assert self.content.list_14.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_transition_trade_collection_arm_lead(self) -> None:
        def condition() -> bool:
            try:
                assert self.content.mark.visible
                assert self.content.act_objects.visible
                assert self.content.act_taxable.visible

                assert self.filter.information.visible
                assert self.filter.trade_objects.visible
                assert self.filter.appeal.visible
                assert self.filter.act.visible
                assert self.filter.results.visible
                assert self.filter.unio.visible
                assert self.filter.archive.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_open_indicator_details_arm_lead(self) -> None:
        def condition() -> bool:
            try:
                assert self.modal.header.visible
                assert self.modal.close.visible
                assert self.modal.table.visible

                return self.modal.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
