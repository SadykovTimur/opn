from __future__ import annotations
from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException
from dit.qa.pages.unio_page.components.navigation import Navigation
from dit.qa.pages.registry_object_table_page.components.container import Container
from dit.qa.pages.registry_object_table_page.components.table import Table
from coms.qa.frontend.pages.component.button import Button


__all__ = ['RegistryObjectPage']


class RegistryObjectPage(Page):
    navigation = Navigation(class_name='opn-navbar')
    footer = Component(class_name="footer")
    object_register = Container(class_name="object-register")
    register_table = Table(css='[class*="OksRegisterTable"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.navigation.gerb.visible
                assert self.navigation.dropdown.visible
                assert self.navigation.buttons_block.visible
                assert self.navigation.user_data.visible

                assert self.object_register.map.visible
                assert self.object_register.table_view.visible
                assert self.object_register.upload.visible
                assert self.object_register.reference.visible
                assert self.object_register.list.visible
                assert self.object_register.table_value[0].visible
                assert self.object_register.table_body[0].visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_information_object(self) -> None:
        def condition() -> bool:
            try:
                assert self.object_register.field_group.visible

                return self.object_register.wrapper[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
