from typing import Callable
import allure
import pytest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE
from tests.steps import (open_start_widget_nio_page, open_start_widget_ts_page, open_transition_search_widget_ts_page,
                         open_transition_search_widget_nio_page)


@allure.label('owner', 't.sadykov')
@allure.label('component', 'OPN')
@allure.epic('OPN')
@allure.story('Переход к поиску в виджете НИО')
@allure.title('Проверка открытия формы поиска')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_open_widget_nio(make_app: Callable[..., Application], browser: str, device_type: str) -> None:
    app = make_app(browser, device_type)

    open_start_widget_ts_page(app)

    open_transition_search_widget_ts_page(app)

    open_start_widget_nio_page(app)

    open_transition_search_widget_nio_page(app)
