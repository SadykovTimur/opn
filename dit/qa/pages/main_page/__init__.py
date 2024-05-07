from __future__ import annotations
from coms.qa.core.helpers import wait_for
from coms.qa.frontend.constants import WEB_DRIVER_WAIT
from coms.qa.frontend.helpers.custom_wait_conditions import ElementToBeClickable
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

__all__ = ['MainPage']


class MainPage(Page):
    header = Component(class_name="header")
    footer = Component(class_name="footer")
    unio_box = Component(id="unio")
    ts_box = Component(id="ts")
    mvk_box = Button(id="mvk")
    income_box = Component(id="income")
    widget_box = Component(id="widget")
    ipp_box = Component(id="ipp")
    supervisor_box = Component(id="supervisor")
    admin_box = Component(id="admin")
    rar_box = Component(id="rar")

    def open_page(self, name: str) -> None:
        wait = WebDriverWait(self.driver, WEB_DRIVER_WAIT)
        el = self.driver.find_element(By.XPATH, f'//div[text()="{name}"]')
        wait.until(ElementToBeClickable(element=el))
        el.click()

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.visible

                assert self.unio_box.visible
                assert self.ts_box.visible
                assert self.mvk_box.visible
                assert self.income_box.visible
                assert self.widget_box.visible
                assert self.ipp_box.visible
                assert self.supervisor_box.visible
                assert self.admin_box.visible
                assert self.rar_box.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
