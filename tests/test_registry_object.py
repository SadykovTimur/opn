from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE
from tests.steps import open_main_page, open_start_page, sign_in, open_subsystem_unio, open_registry_object


@allure.label('owner', 't.sadykov')
@allure.label('component', 'OPN')
@allure.epic('OPN')
@allure.story('Переход к Реестру объектов недвижимости')
@allure.title('Проверка открытия Реестра объектов с прогруженной таблицей')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_registry_object(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:

    app = make_app(browser, device_type)

    open_start_page(app)

    sign_in(app, request.config.option.username, request.config.option.password)
    open_main_page(app)

    open_subsystem_unio(app)

    open_registry_object(app)

