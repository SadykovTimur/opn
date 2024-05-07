from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException

__all__ = ['StartPage']


class StartPage(Page):
    header = Component(class_name="header")
    footer = Component(class_name="footer")
    title_auth = Component(xpath="//span[text()='Пожалуйста, авторизуйтесь!']")
    login = Component(id="username")
    password = Component(id="password")
    submit = Button(id="enterBtn")
    sudir_login = Component(css='[type="button"]')
    content_title = Component(class_name="contentTitleIcon")

    def wait_for_loading(self) -> None:

        def condition() -> bool:
            try:
                assert self.header.visible

                assert self.title_auth.visible
                assert self.login.visible
                assert self.password.visible
                assert self.submit.visible
                assert self.sudir_login.visible
                assert self.content_title.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
