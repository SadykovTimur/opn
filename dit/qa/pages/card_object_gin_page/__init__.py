from __future__ import annotations
from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from selenium.common.exceptions import NoSuchElementException
from dit.qa.pages.unio_page.components.navigation import Navigation


__all__ = ['CardObjectGinPage']


class CardObjectGinPage(Page):
    navigation = Navigation(class_name='opn-navbar')
    footer = Component(class_name="footer")
    list_object = Component(xpath="//h3[text()='Список объектов недвижимого имущества']")
    table = Components(css='[class*="gwt-Hyperlink"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.navigation.gerb.visible
                assert self.navigation.dropdown.visible
                assert self.navigation.buttons_block.visible
                assert self.navigation.user_data.visible

                assert self.list_object.visible
                assert self.table[0].visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
