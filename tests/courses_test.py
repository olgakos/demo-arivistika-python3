import allure
from allure_commons.types import Severity
from selene import browser
from selene.support.shared import browser

from models.courses_page import CoursePageMethods

@allure.title('Оплата через Robokassa')
@allure.tag('pay')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Olga')
@allure.feature(f'Проверка оплаты')
@allure.story('Доступна оплата через Robokassa')
@allure.link('https://arivistika.ru', name="Link to Home Page")

def test_course_pay_robokassa():

    course = CoursePageMethods()

    with allure.step("Открыть страницу курсов"):
        browser.open('/cources-list')
    with allure.step("Открыть страницу курса Декларирование"):
        course.check_title_dec('Курс PRO Декларирование')
    with allure.step("Нажать кнопку \"Подробнее\""):
        course.click_button_more()
    with allure.step("Нажать кнопку \"Купить\""):
        course.click_button_bay()
        # Expect:
    with allure.step("Модуль ввода платежных данных доступен"):
        course.button_pay_is_visible("Оплатить")