from typing import Callable
import allure
import pytest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE
from tests.steps import (open_start_widget_nio_page, open_start_widget_ts_page, open_transition_search_widget_ts_page)


@allure.label('owner', 't.sadykov')
@allure.label('component', 'OPN')
@allure.epic('OPN')
@allure.story('Загрузка стартовой страницы Виджета НИО')
@allure.title('Проверка открытия стартовой страницы виджета НИО')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_open_widget_nio(make_app: Callable[..., Application], browser: str, device_type: str
                         ) -> None:
    app = make_app(browser, device_type)

    open_start_widget_ts_page(app)

    open_transition_search_widget_ts_page(app) #вкладка 27 шаг 2 и вкладка 28 шаг 3, они практически идентичны,поместил в один тест

    open_start_widget_nio_page(app)
