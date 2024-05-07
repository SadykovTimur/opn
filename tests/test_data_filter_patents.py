from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE
from tests.steps import start_patents_page, sign_in_patents_page, open_patents_page, open_filter_value_patents, open_data_filter_patents


@allure.label('owner', 't.sadykov')
@allure.label('component', 'OPN')
@allure.epic('OPN')
@allure.story('Выбор дат фильтра')
@allure.title('Проверка выбора значения фильтра')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_data_filter_patents(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:

    app = make_app(browser, device_type)

    start_patents_page(app)

    sign_in_patents_page(app, request.config.option.username, request.config.option.password)
    open_patents_page(app)

    open_filter_value_patents(app)

    open_data_filter_patents(app, '01.01.2018', '31.12.2018')
