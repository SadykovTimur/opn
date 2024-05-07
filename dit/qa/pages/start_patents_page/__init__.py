from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException
from dit.qa.pages.start_patents_page.components.header import Header

__all__ = ['StartPatentsPage']


class StartPatentsPage(Page):
    header = Header(tag='header')
    login = TextField(id="UserName")
    password = TextField(id="Password")
    remember_me = Component(css='[class="checkbox"]')
    submit = Button(xpath="//span[text()='Войти']")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.title.visible
                assert self.header.logo.visible
                assert self.header.header_login.visible

                assert self.login.visible
                assert self.password.visible
                assert self.submit.visible

                return self.remember_me.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
