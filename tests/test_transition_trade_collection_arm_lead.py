from typing import Callable
import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE
from tests.steps import (open_main_page, open_start_page, sign_in, open_subsystem_arm_lead,
                         open_transition_group_list_arm_lead, open_transition_trade_collection_arm_lead)


@allure.label('owner', 't.sadykov')
@allure.label('component', 'OPN')
@allure.epic('OPN')
@allure.story('Переход в раздел "Торговый сбор"')
@allure.title('Проверка открытия раздела "Торговый сбор"')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_transition_group_list_arm_lead(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:

    app = make_app(browser, device_type)

    open_start_page(app)

    sign_in(app, request.config.option.username, request.config.option.password)
    open_main_page(app)

    open_subsystem_arm_lead(app)

    open_transition_group_list_arm_lead(app)

    open_transition_trade_collection_arm_lead(app)
