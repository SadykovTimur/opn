from __future__ import annotations
from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from selenium.common.exceptions import NoSuchElementException
from dit.qa.pages.income_page.components.content import Content
from dit.qa.pages.income_page.components.main import Main
from dit.qa.pages.income_page.components.settings_panel import SettingsPanel
from dit.qa.pages.income_page.components.tree_panel import TreePanel
from coms.qa.frontend.pages.component import Component

__all__ = ['IncomePage']


class IncomePage(Page):
    content = Content(id="h-content")
    main = Main(id="content-container")
    settings_panel = SettingsPanel(id="c_settingsPanel")
    tree_panel = TreePanel(id="c_treePanel")
    grid_panel = Component(id="c_gridPanel")
    body_content = Component(class_name="grid-body-content")
    params_panel = Component(id="c_paramsPanel")
    one_panel = Component(id="c_onePanel")
    edit_panel = Component(id="c_editPanel")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.content.logo.visible
                assert self.content.book.visible
                assert self.content.navi.visible
                assert self.content.help.visible
                assert self.content.docs.visible
                assert self.content.user.visible
                assert self.content.news.visible
                assert self.content.inds.visible
                assert self.content.input.visible
                assert self.content.show_legal.visible
                assert self.content.reports.visible
                assert self.content.present.visible
                assert self.content.map.visible

                assert self.main.search_name.visible
                assert self.main.search.visible
                assert self.main.reset.visible

                return self.main.news_block[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_transition_registry_legal_entities_income(self) -> None:
        def condition() -> bool:
            try:
                assert self.content.logo.visible
                assert self.content.book.visible
                assert self.content.navi.visible
                assert self.content.help.visible
                assert self.content.docs.visible
                assert self.content.user.visible
                assert self.content.news.visible
                assert self.content.inds.visible
                assert self.content.input.visible
                assert self.content.show_legal.visible
                assert self.content.reports.visible
                assert self.content.present.visible
                assert self.content.map.visible

                assert self.settings_panel.title.visible
                assert self.settings_panel.apply_btn.visible

                assert self.tree_panel.visible
                assert self.grid_panel.visible

                return self.content.title_registry.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_legal_entities_income(self) -> None:
        def condition() -> bool:
            try:
                assert self.tree_panel.name.visible

                return self.tree_panel.inn.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_open_card_entities_income(self) -> None:
        def condition() -> bool:
            try:
                return self.body_content.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_transition_data_input_income(self) -> None:
        def condition() -> bool:
            try:
                assert self.content.data.visible
                assert self.params_panel.visible

                return self.one_panel.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_transition_indicator_editor_income(self) -> None:
        def condition() -> bool:
            try:
                assert self.content.title_editor.visible
                assert self.tree_panel.tree.visible

                return self.edit_panel.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
