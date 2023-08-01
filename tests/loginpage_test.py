import allure
from allure_commons.types import Severity
from selene import browser
from selene.support.shared import browser

from models.login_page import LoginPageMethods


login = LoginPageMethods()

@allure.title('Подсказки при залогине')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Olga')
@allure.feature(f'Залогин')
@allure.story('Пользователь получает подсказку')
@allure.link('https://arivistika.ru', name="Link to Home Page")
def test_login():

    email_value = 'test@test.com'
    pass_value = '123'

    with allure.step("Открыть страницу залогина"):
        browser.open('/my-account')
    with allure.step("Ввести логин"):
        login.fill_username(email_value)
    with allure.step("Ввести пароль"):
        login.fill_password(pass_value)
    # with allure.step("Нажать кнопку вход"):
    #      login.click_login_button() # скрыто на время отладки
    # with allure.step("Прочитать сообщение об ошибке"):
    #      login.check_error_alert("Неверный адрес e-mail") # скрыто на время отладки

#local
@allure.title('Подсказки при залогине_LOC')
@allure.tag('web_LOC')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Olga_LOC')
@allure.feature(f'Проверка залогина_LOC')
@allure.story('Пользователь получает подсказку_LOC')
@allure.link('https://arivistika.ru', name="Link to Home Page")
def test_login_LOCALTIME():

    email_value = 'test@test.com'
    pass_value = '123'

    with allure.step("Открыть страницу залогина"):
        browser.open('https://arivistika.ru/my-account') #!
    with allure.step("Ввести логин"):
        login.fill_username(email_value)
    with allure.step("Ввести пароль"):
        login.fill_password(pass_value)

