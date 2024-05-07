from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import open_main_page, open_start_page, sign_in, open_subsystem_income, open_transition_registry_legal_entities_income, open_search_legal_entities_income, open_card_legal_entities_income, open_transition_data_input_income


@allure.label('owner', 't.sadykov')
@allure.label('component', 'OPN')
@allure.epic('OPN')
@allure.story('Переход к вводу данных')
@allure.title('Проверка открытия модуля ввода данных')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_transition_data_input_income(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:

    app = make_app(browser, device_type)

    open_start_page(app)

    sign_in(app, request.config.option.username, request.config.option.password)
    open_main_page(app)

    open_subsystem_income(app)

    open_transition_registry_legal_entities_income(app)

    open_search_legal_entities_income(app, '7713076301')

    open_card_legal_entities_income(app)

    open_transition_data_input_income(app)






