from typing import Callable

import allure
import pytest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE
from tests.steps import start_patents_page


@allure.label('owner', 't.sadykov')
@allure.label('component', 'OPN')
@allure.epic('OPN')
@allure.story('Стартовая страница')
@allure.title('Открытие стартовой страницы')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_start_patents_page(make_app: Callable[..., Application], browser: str, device_type: str) -> None:
    app = make_app(browser, device_type)

    start_patents_page(app)
