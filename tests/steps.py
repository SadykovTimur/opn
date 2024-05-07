import allure
from coms.qa.fixtures.application import Application
from _pytest.fixtures import FixtureRequest
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException
from dit.qa.pages.main_page import MainPage
from dit.qa.pages.patents_page import PatentsPage
from dit.qa.pages.start_page import StartPage
from dit.qa.pages.mvk_page import MvkPage
from dit.qa.pages.unio_page import UnioPage
from dit.qa.pages.registry_object_table_page import RegistryObjectPage
from dit.qa.pages.object_map_page import ObjectMapPage
from dit.qa.pages.card_object_gin_page import CardObjectGinPage
from dit.qa.pages.start_patents_page import StartPatentsPage
from dit.qa.pages.ts_page import TsPage
from dit.qa.pages.income_page import IncomePage
from dit.qa.pages.ipp_page import IppPage
from dit.qa.pages.arm_lead_page import ArmLeadPage
from dit.qa.pages.registry_appeal_page import RegistryAppealPage
from dit.qa.pages.admin_page import AdminPage
from dit.qa.pages.widget_page import WidgetPage


__all__ = [
    'open_start_page',
    'sign_in',
    'open_main_page',
    'open_subsystem_mvk',
    'open_subsystem_unio',
    'open_registry_object',
    'open_object_map',
    'open_card_object_gin',
    'return_register_object',
    'view_information_object',
    'start_patents_page',
    'sign_in_patents_page',
    'open_patents_page',
    'open_filter_value_patents',
    'open_filter_patents',
    'open_data_filter_patents',
    'open_transition_card_ip_patents',
    'open_subsystem_ts',
    'open_transition_card_ts',
    'open_transition_registry_electronic_document_ts',
    'open_transition_registry_act_ts',
    'open_transition_detailed_registry_act_ts',
    'open_subsystem_income',
    'open_transition_registry_legal_entities_income',
    'open_search_legal_entities_income',
    'open_card_legal_entities_income',
    'open_transition_data_input_income',
    'open_transition_indicator_editor_income',
    'open_subsystem_ipp',
    'open_transition_card_statement_ipp',
    'open_transition_chapter_main_factors_ipp',
    'open_subsystem_arm_lead',
    'open_transition_group_list_arm_lead',
    'open_transition_trade_collection_arm_lead',
    'open_indicator_details_arm_lead',
    'open_transition_registry_meetings_mvk',
    'open_transition_card_meetings_mvk',
    'open_transition_report_mvk',
    'open_registration_new_appeal_mvk',
    'open_subsystem_registry_appeal',
    'open_filter_message_registry_appeal',
    'open_transition_constructor_response_registry_appeal',
    'open_registration_new_registry_appeal',
    'open_subsystem_admin',
    'open_transition_section_role_admin',
    'open_open_role_group_admin',
    'open_transition_person_unio',
    'open_start_widget_ts_page',
    'open_start_widget_nio_page',
    'open_start_widget_gin_page',
    'open_transition_search_widget_ts_page',
    'open_transition_search_widget_nio_page',
    'open_transition_search_widget_gin_page'
]


def open_start_page(app: Application, request: FixtureRequest) -> None:
    with allure.step('Opening Start page'):
        if request.config.option.block_urls:
            app.send_command('Network.setBlockedURLs', {'urls': ['fonts.googleapis.com', 'code.jquery.com', 'maxcdn.bootstrapcdn.com']})
            app.send_command('Network.enable', {})
        try:
            page = StartPage(app)
            page.open()
            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise TimeoutError('Start page was not loaded') from e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_form = StartPage(app)

            auth_form.login.send_keys(login)
            auth_form.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Entering data exception') from e

        auth_form.submit.click()


def open_main_page(app: Application) -> None:
    with allure.step('Opening Main page'):
        try:
            MainPage(app).wait_for_loading()

            screenshot_attach(app, 'main_page')
        except Exception as e:
            screenshot_attach(app, 'main_page_error')

            raise TimeoutError('Main page was not loaded') from e


def open_registry_object(app: Application) -> None:
    with allure.step('Opening Registry object page'):
        try:
            UnioPage(app).navigation.register.click()
            RegistryObjectPage(app).wait_for_loading()

            screenshot_attach(app, 'registry_page')
        except Exception as e:
            screenshot_attach(app, 'registry_page_error')

            raise TimeoutError('Registry page was not loaded') from e


def open_object_map(app: Application) -> None:
    with allure.step('Opening Object map page'):
        try:
            RegistryObjectPage(app).object_register.map.click()
            ObjectMapPage(app).wait_for_loading()

            screenshot_attach(app, 'object_page')
        except Exception as e:
            screenshot_attach(app, 'object_page_error')

            raise TimeoutError('Object page was not loaded') from e


def open_card_object_gin(app: Application) -> None:
    with allure.step('Opening Card object gin page'):
        try:
            RegistryObjectPage(app).navigation.gin.click()
            RegistryObjectPage(app).navigation.gin_list.click()
            CardObjectGinPage(app).wait_for_loading()

            screenshot_attach(app, 'card_page')
        except Exception as e:
            screenshot_attach(app, 'card_page_error')

            raise TimeoutError('Card object gin page was not loaded') from e


def return_register_object(app: Application) -> None:
    with allure.step('Return register object page'):
        try:
            CardObjectGinPage(app).navigation.register.click()
            RegistryObjectPage(app).wait_for_loading()

            screenshot_attach(app, 'return_page')
        except Exception as e:
            screenshot_attach(app, 'return_page_error')

            raise TimeoutError('Return register object was not loaded') from e


def view_information_object(app: Application) -> None:
    with allure.step('View information object page'):
        try:
            app.move_to_element(RegistryObjectPage(app).register_table.line.webelement)
            RegistryObjectPage(app).register_table.line.click()
            RegistryObjectPage(app).wait_for_information_object()

            screenshot_attach(app, 'view_page')
        except Exception as e:
            screenshot_attach(app, 'view_page_error')

            raise TimeoutError('View information object page was not loaded') from e


def start_patents_page(app: Application) -> None:
    with allure.step('Opening Start page patents'):
        try:
            page = StartPatentsPage(app)
            page.base_url = 'https://tr.mos.ru/Patents'
            page.open()
            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise TimeoutError('Start page patents was not loaded') from e


def sign_in_patents_page(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login, password} signing in'):
        try:
            auth_form = StartPatentsPage(app)

            auth_form.login.send_keys('testUser')
            auth_form.password.send_keys('O0yydAmPrH$Z')

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Entering data exception') from e

        auth_form.submit.click()


def open_patents_page(app: Application) -> None:
    with allure.step('Opening Patents page'):
        try:
            PatentsPage(app).wait_for_loading()

            screenshot_attach(app, 'patents_page')
        except Exception as e:
            screenshot_attach(app, 'patents_page_error')

            raise TimeoutError('Patents page was not loaded') from e


def open_filter_value_patents(app: Application) -> None:
    with allure.step('Opening Filter value page'):
        try:
            PatentsPage(app).sidebar.select.click()
            PatentsPage(app).sidebar.multiselect.click()
            PatentsPage(app).wait_for_loading_filter_value()

            screenshot_attach(app, 'filter_page')
        except Exception as e:
            screenshot_attach(app, 'filter_page_error')

            raise TimeoutError('Filter value page was not loaded') from e


def open_data_filter_patents(app: Application, begin: str, end: str) -> None:
    with allure.step('Opening Data filter  page'):
        try:
            PatentsPage(app).sidebar.data_begin.send_keys(begin)
            PatentsPage(app).sidebar.data_end.send_keys(end)
            PatentsPage(app).wait_for_loading_data_filter(begin, end)

            screenshot_attach(app, 'data_page')
        except Exception as e:
            screenshot_attach(app, 'data_page_error')

            raise TimeoutError('Data filter page was not loaded') from e


def open_filter_patents(app: Application) -> None:
    with allure.step('Opening Filter page'):
        try:
            PatentsPage(app).sidebar.search.click()
            PatentsPage(app).wait_for_loading_filters()

            screenshot_attach(app, 'filter_page')
        except Exception as e:
            screenshot_attach(app, 'filter_page_error')

            raise TimeoutError('Filter page was not loaded') from e


def open_transition_card_ip_patents(app: Application) -> None:
    with allure.step('Opening Transition card page'):
        try:
            PatentsPage(app).content.person.click()
            PatentsPage(app).wait_for_loading_transition_card()

            screenshot_attach(app, 'transition_page')
        except Exception as e:
            screenshot_attach(app, 'transition_page_error')

            raise TimeoutError('Transition card page was not loaded') from e


def open_subsystem_ts(app: Application, request: FixtureRequest) -> None:
    with allure.step('Opening Subsystem ts page'):
        if request.config.option.block_urls:
            app.send_command('Network.setBlockedURLs', {'urls': ['maps.google.com']})
            app.send_command('Network.enable', {})
        try:
            MainPage(app).open_page("Торговый сбор")
            TsPage(app).wait_for_loading()

            screenshot_attach(app, 'subsystem_ts_page')
        except Exception as e:
            screenshot_attach(app, 'subsystem_ts_page_error')

            raise TimeoutError('Subsystem ts page was not loaded') from e


def open_transition_card_ts(app: Application) -> None:
    with allure.step('Opening Transition card ts page'):
        try:
            TsPage(app).cap_block.pictogram.click()
            TsPage(app).wait_for_loading_card_ts()

            screenshot_attach(app, 'transition_page')
        except Exception as e:
            screenshot_attach(app, 'transition_error')

            raise TimeoutError('Transition card ts page was not loaded') from e


def open_transition_registry_electronic_document_ts(app: Application) -> None:
    with allure.step('Opening Transition registry electronic document ts page'):
        try:
            TsPage(app).navbar.registry.click()
            TsPage(app).navbar.objects_eds.click()
            TsPage(app).wait_for_loading_transition_registry_electronic_document_ts()

            screenshot_attach(app, 'electronic_page')
        except Exception as e:
            screenshot_attach(app, 'electronic_error')

            raise TimeoutError('Transition registry electronic document ts page was not loaded') from e


def open_transition_registry_act_ts(app: Application) -> None:
    with allure.step('Opening Registry act ts page'):
        try:
            TsPage(app).navbar.registry.click()
            TsPage(app).navbar.objects_acts.click()
            TsPage(app).wait_for_loading_transition_registry_act_ts()

            screenshot_attach(app, 'registry_page')
        except Exception as e:
            screenshot_attach(app, 'registry_error')

            raise TimeoutError('Registry act ts page was not loaded') from e


def open_transition_detailed_registry_act_ts(app: Application) -> None:
    with allure.step('Opening Detailed act ts page'):
        try:
            TsPage(app).cap_block.objects.click()
            TsPage(app).wait_for_loading_transition_detailed_registry_act_ts()

            screenshot_attach(app, 'detailed_page')
        except Exception as e:
            screenshot_attach(app, 'detailed_error')

            raise TimeoutError('Detailed act ts page was not loaded') from e


def open_subsystem_income(app: Application) -> None:
    with allure.step('Opening Subsystem income page'):
        try:
            MainPage(app).open_page("Доходы")
            IncomePage(app).wait_for_loading()

            screenshot_attach(app, 'subsystem_income_page')
        except Exception as e:
            screenshot_attach(app, 'subsystem_income_page_error')

            raise TimeoutError('Subsystem income page was not loaded') from e


def open_transition_registry_legal_entities_income(app: Application) -> None:
    with allure.step('Opening Transition registry legal income page'):
        try:
            IncomePage(app).content.show_legal.click()
            IncomePage(app).wait_for_loading_transition_registry_legal_entities_income()

            screenshot_attach(app, 'transition_income_page')
        except Exception as e:
            screenshot_attach(app, 'transition_income_page_error')

            raise TimeoutError('Transition registry legal income page was not loaded') from e


def open_search_legal_entities_income(app: Application, search: str) -> None:
    with allure.step('Opening Search legal entities income page'):
        try:
            IncomePage(app).settings_panel.coff_filter.click()
            IncomePage(app).tree_panel.search_tree.send_keys(search)
            IncomePage(app).tree_panel.search.click()
            IncomePage(app).wait_for_loading_legal_entities_income()

            screenshot_attach(app, 'search_legal_income_page')
        except Exception as e:
            screenshot_attach(app, 'search_legal_income_page_error')

            raise TimeoutError('Search legal entities income page was not loaded') from e


def open_card_legal_entities_income(app: Application) -> None:
    with allure.step('Opening Card legal entities income page'):
        try:
            IncomePage(app).tree_panel.checkbox.click()
            IncomePage(app).tree_panel.show.click()
            IncomePage(app).wait_for_loading_open_card_entities_income()

            screenshot_attach(app, 'card_legal_income_page')
        except Exception as e:
            screenshot_attach(app, 'card_legal_income_page_error')

            raise TimeoutError('Card legal entities income page was not loaded') from e


def open_transition_data_input_income(app: Application) -> None:
    with allure.step('Opening Transition data input income page'):
        try:
            IncomePage(app).content.input.click()
            IncomePage(app).wait_for_loading_transition_data_input_income()

            screenshot_attach(app, 'transition_data_income_page')
        except Exception as e:
            screenshot_attach(app, 'transition_data_income_page_error')

            raise TimeoutError('Transition data input income page was not loaded') from e


def open_transition_indicator_editor_income(app: Application) -> None:
    with allure.step('Opening Transition indicator editor income page'):
        try:
            IncomePage(app).content.inds.click()
            IncomePage(app).wait_for_loading_transition_indicator_editor_income()

            screenshot_attach(app, 'transition_indicator_income_page')
        except Exception as e:
            screenshot_attach(app, 'transition_indicator_income_page_error')

            raise TimeoutError('Transition indicator editor income page was not loaded') from e


def open_subsystem_ipp(app: Application, request: FixtureRequest) -> None:
    with allure.step('Opening Subsystem ipp page'):
        if request.config.option.block_urls:
            app.send_command('Network.setBlockedURLs', {'urls': ['fonts.googleapis.com']})
            app.send_command('Network.enable', {})
        try:
            MainPage(app).open_page("ИПП")
            IppPage(app).wait_for_loading()

            screenshot_attach(app, 'ipp_page')
        except Exception as e:
            screenshot_attach(app, 'ipp_page_error')

            raise TimeoutError('Subsystem ipp page was not loaded') from e


def open_transition_card_statement_ipp(app: Application) -> None:
    with allure.step('Opening Transition card statement ipp page'):
        try:
            IppPage(app).main_wrapper.open.click()
            IppPage(app).wait_for_loading_card_statement()

            screenshot_attach(app, 'transition_card_page')
        except Exception as e:
            screenshot_attach(app, 'transition_card_page_error')

            raise TimeoutError('Transition card statement ipp page was not loaded') from e


def open_transition_chapter_main_factors_ipp(app: Application) -> None:
    with allure.step('Opening Transition chapter main factors page'):
        try:
            IppPage(app).navbar.dashboard.click()
            IppPage(app).wait_for_loading_chapter_main_factors()

            screenshot_attach(app, 'transition_chapter_page')
        except Exception as e:
            screenshot_attach(app, 'transition_chapter_page_error')

            raise TimeoutError('Transition chapter main factors page was not loaded') from e


def open_subsystem_arm_lead(app: Application) -> None:
    with allure.step('Opening Subsystem arm page'):
        try:
            MainPage(app).open_page("АРМ Руководителя")
            ArmLeadPage(app).wait_for_loading()

            screenshot_attach(app, 'subsystem_arm_page')
        except Exception as e:
            screenshot_attach(app, 'subsystem_arm_page_error')

            raise TimeoutError('Subsystem arm page was not loaded') from e


def open_transition_group_list_arm_lead(app: Application) -> None:
    with allure.step('Opening Transition group list page'):
        try:
            ArmLeadPage(app).filter.list_2014.click()
            ArmLeadPage(app).wait_for_loading_transition_group_arm_lead()

            screenshot_attach(app, 'transition_group_page')
        except Exception as e:
            screenshot_attach(app, 'transition_group_page_error')

            raise TimeoutError('Transition group list page was not loaded') from e


def open_transition_trade_collection_arm_lead(app: Application) -> None:
    with allure.step('Opening Transition trade collection page'):
        try:
            ArmLeadPage(app).navbar.ts_nav.click()
            ArmLeadPage(app).wait_for_loading_transition_trade_collection_arm_lead()

            screenshot_attach(app, 'trade_collection_page')
        except Exception as e:
            screenshot_attach(app, 'trade_collection_page_error')

            raise TimeoutError('Transition trade collection page was not loaded') from e


def open_indicator_details_arm_lead(app: Application) -> None:
    with allure.step('Opening Indicator details page'):
        try:
            ArmLeadPage(app).filter.indicator.click()
            ArmLeadPage(app).wait_for_loading_open_indicator_details_arm_lead()

            screenshot_attach(app, 'indicator_details_page')
        except Exception as e:
            screenshot_attach(app, 'indicator_details_page_error')

            raise TimeoutError('Indicator details page was not loaded') from e


def open_subsystem_mvk(app: Application) -> None:
    with allure.step('Opening Subsystem mvk page'):
        try:
            MainPage(app).open_page("МВК")
            MvkPage(app).wait_for_loading()

            screenshot_attach(app, 'subsystem_mvk_page')
        except Exception as e:
            screenshot_attach(app, 'subsystem_mvk_page_error')

            raise TimeoutError('Subsystem mvk page was not loaded') from e


def open_transition_registry_meetings_mvk(app: Application) -> None:
    with allure.step('Opening Transition registry meetings mvk page'):
        try:
            MvkPage(app).navbar.mvk.click()
            MvkPage(app).navbar.registry_meeting.click()
            MvkPage(app).wait_for_loading_transition_registry_meetings_mvk()

            screenshot_attach(app, 'transition_registry_mvk_page')
        except Exception as e:
            screenshot_attach(app, 'transition_registry_mvk_page_error')

            raise TimeoutError('Transition registry meetings mvk page was not loaded') from e


def open_transition_card_meetings_mvk(app: Application) -> None:
    with allure.step('Opening Transition card meetings mvk page'):
        try:
            MvkPage(app).content_table.table_data.click()
            MvkPage(app).wait_for_loading_transition_card_meetings_mvk()

            screenshot_attach(app, 'transition_card_mvk_page')
        except Exception as e:
            screenshot_attach(app, 'transition_card_mvk_page_error')

            raise TimeoutError('Transition card meetings mvk page was not loaded') from e


def open_transition_report_mvk(app: Application) -> None:
    with allure.step('Opening Transition report mvk page'):
        try:
            MvkPage(app).navbar.report.click()
            MvkPage(app).navbar.menu_reports.click()
            MvkPage(app).wait_for_loading_transition_report_mvk()

            screenshot_attach(app, 'transition_report_mvk_page')
        except Exception as e:
            screenshot_attach(app, 'transition_report_mvk_page_error')

            raise TimeoutError('Transition report mvk page was not loaded') from e


def open_registration_new_appeal_mvk(app: Application) -> None:
    with allure.step('Opening Registration new appeal mvk page'):
        try:
            MvkPage(app).content_table.appeal.click()
            MvkPage(app).wait_for_loading_registration_new_appeal_mvk()

            screenshot_attach(app, 'registration_appeal_mvk_page')
        except Exception as e:
            screenshot_attach(app, 'registration_appeal_mvk_page_error')

            raise TimeoutError('Registration new appeal page was not loaded') from e


def open_subsystem_registry_appeal(app: Application,) -> None:
    with allure.step('Opening Subsystem registry appeal page'):
        try:
            MainPage(app).open_page("Реестр обращений")
            RegistryAppealPage(app).wait_for_loading()

            screenshot_attach(app, 'subsystem_registry_appeal_page')
        except Exception as e:
            screenshot_attach(app, 'subsystem_registry_appeal_error')

            raise TimeoutError('Subsystem registry appeal page was not loaded') from e


def open_filter_message_registry_appeal(app: Application) -> None:
    with allure.step('Opening Filter message appeal registry page'):
        try:
            RegistryAppealPage(app).toolbar.switch.click()
            RegistryAppealPage(app).wait_for_loading_filer_message_registry_appeal()

            screenshot_attach(app, 'filter_message_appeal_page')
        except Exception as e:
            screenshot_attach(app, 'filter_message_appeal_page_error')

            raise TimeoutError('Filter message appeal registry page was not loaded') from e


def open_transition_constructor_response_registry_appeal(app: Application) -> None:
    with allure.step('Opening Transition constructor response registry page'):
        try:
            RegistryAppealPage(app).navbar.nav_constructor.click()
            RegistryAppealPage(app).wait_for_loading_transition_constructor_response_registry_appeal()

            screenshot_attach(app, 'transition_constructor_appeal_page')
        except Exception as e:
            screenshot_attach(app, 'transition_constructor_appeal_page_error')

            raise TimeoutError('Transition constructor response registry page was not loaded') from e


def open_registration_new_registry_appeal(app: Application) -> None:
    with allure.step('Opening Subsystem registry appeal page'):
        try:
            RegistryAppealPage(app).toolbar.reg_appeal.click()
            RegistryAppealPage(app).wait_for_loading_registration_new_registry_appeal()

            screenshot_attach(app, 'subsystem_registry_appeal_page')
        except Exception as e:
            screenshot_attach(app, 'subsystem_registry_appeal_error')

            raise TimeoutError('Subsystem registry appeal page was not loaded') from e


def open_subsystem_admin(app: Application) -> None:
    with allure.step('Opening Subsystem admin page'):
        try:
            MainPage(app).open_page("Администрирование")
            AdminPage(app).wait_for_loading()

            screenshot_attach(app, 'subsystem_admin_page')
        except Exception as e:
            screenshot_attach(app, 'subsystem_admin_error')

            raise TimeoutError('Subsystem admin page was not loaded') from e


def open_transition_section_role_admin(app: Application) -> None:
    with allure.step('Opening Transition section role page'):
        try:
            AdminPage(app).navbar.roles.click()
            AdminPage(app).wait_for_loading_transition_section_role_admin()

            screenshot_attach(app, 'transition_section_admin_page')
        except Exception as e:
            screenshot_attach(app, 'transition_section_admin_error')

            raise TimeoutError('Transition section role page was not loaded') from e


def open_open_role_group_admin(app: Application) -> None:
    with allure.step('Opening Open role group page'):
        try:
            AdminPage(app).content.admin.click()
            AdminPage(app).wait_for_loading_open_role_group_admin()

            screenshot_attach(app, 'open_role_admin_page')
        except Exception as e:
            screenshot_attach(app, 'open_role_admin_error')

            raise TimeoutError('Transition section role page was not loaded') from e


def open_subsystem_unio(app: Application) -> None:
    with allure.step('Opening Subsystem page'):
        try:
            MainPage(app).open_page("УНИО")
            UnioPage(app).wait_for_loading()

            screenshot_attach(app, 'subsystem_page')
        except Exception as e:
            screenshot_attach(app, 'subsystem_page_error')

            raise TimeoutError('Subsystem page was not loaded') from e


def open_transition_person_unio(app: Application) -> None:
    with allure.step('Opening Transition personal page'):
        try:
            UnioPage(app).navigation.user_data.click()
            UnioPage(app).wait_for_loading_open_transition_person_unio()

            screenshot_attach(app, 'transition_personal_unio_page')
        except Exception as e:
            screenshot_attach(app, 'transition_personal_unio_page_error')

            raise TimeoutError('Transition personal page was not loaded') from e


def open_start_widget_ts_page(app: Application) -> None:
    with allure.step('Opening Widget ts page'):
        try:
            page = WidgetPage(app)
            page.base_url = 'https://tr.mos.ru/widget-ts/'
            page.open()
            page.wait_for_loading()

            screenshot_attach(app, 'widget_ts_page')
        except Exception as e:
            screenshot_attach(app, 'widget_ts_page_error')

            raise TimeoutError('Widget ts page was not loaded') from e


def open_transition_search_widget_ts_page(app: Application) -> None:
    with allure.step('Opening Transition search widget ts page'):
        try:
            page = WidgetPage(app)
            page.base_url = 'https://tr.mos.ru/widget-ts/'
            page.open()
            page.search.click()
            page.wait_for_loading_transition_search_widget_ts()

            screenshot_attach(app, 'transition_search_widget_ts_page')
        except Exception as e:
            screenshot_attach(app, 'transition_search_widget_ts_page_error')

            raise TimeoutError('Transition search widget ts page was not loaded') from e


def open_start_widget_nio_page(app: Application) -> None:
    with allure.step('Opening Widget nio page'):
        try:
            page = WidgetPage(app)
            page.base_url = 'https://tr.mos.ru/widget-niok/'
            page.open()
            page.wait_for_loading_widget_nio()

            screenshot_attach(app, 'widget_nio_page')
        except Exception as e:
            screenshot_attach(app, 'widget_nio_page_error')

            raise TimeoutError('Widget nio page was not loaded') from e


def open_transition_search_widget_nio_page(app: Application) -> None:
    with allure.step('Opening Transition search widget nio page'):
        try:
            page = WidgetPage(app)
            page.base_url = 'https://tr.mos.ru/widget-niok/'
            page.open()
            page.search.click()
            page.wait_for_loading_transition_search_widget_nio()

            screenshot_attach(app, 'transition_search_widget_nio_page')
        except Exception as e:
            screenshot_attach(app, 'transition_search_widget_nio_page_error')

            raise TimeoutError('Transition search widget nio page was not loaded') from e


def open_start_widget_gin_page(app: Application) -> None:
    with allure.step('Opening Widget gin page'):
        try:
            page = WidgetPage(app)
            page.base_url = 'https://tr.mos.ru/widget-gin/'
            page.open()
            page.wait_for_loading_widget_gin()

            screenshot_attach(app, 'widget_gin_page')
        except Exception as e:
            screenshot_attach(app, 'widget_gin_page_error')

            raise TimeoutError('Widget gin page was not loaded') from e


def open_transition_search_widget_gin_page(app: Application) -> None:
    with allure.step('Opening Transition search widget gin page'):
        try:
            page = WidgetPage(app)
            page.base_url = 'https://tr.mos.ru/widget-gin/'
            page.open()
            page.search.click()
            page.wait_for_loading_transition_search_widget_gin()

            screenshot_attach(app, 'transition_search_widget_gin_page')
        except Exception as e:
            screenshot_attach(app, 'transition_search_widget_gin_page_error')

            raise TimeoutError('Transition search widget gin page was not loaded') from e
