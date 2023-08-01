import allure
from allure_commons.types import Severity
from selene import browser

from models.home_page import HomePageMethods

home = HomePageMethods()

@allure.title('Заголовки на главной странице')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Olga')
@allure.feature(f'Проверка текстов')
@allure.story('Текстовые данные соответствуют ожидаемым')
@allure.link('https://arivistika.ru', name="Link to Home Page")
def test_homepage_texts():

    school_name = 'ШКОЛА [ВЭД] АРИВИСТИКИ'
    school_adress = 'Санкт-Петербург, ул. Гапсальская, д. 5, БЦ «Балтика»'
    school_email = "info@arivistika.ru"
    school_title2 = "Тест на профориентацию"

    with allure.step("Открыть страницу"):
        # browser.open('https://arivistika.ru/')
        browser.open('/')
    with allure.step("Проверить текст: название Школы"):
        home.check_title(school_name)
    with allure.step("Проверить текст: фактический адрес"):
        home.check_adress(school_adress)
    with allure.step("Проверить текст: e-mail"):
        home.check_mail(school_email)
    with allure.step("Проверить текст: заголовок2"):
        home.check_paragraf_text(school_title2)

@allure.title('Подсказки в форме регистрации')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Olga')
@allure.feature(f'Проверка заполения формы')
@allure.story('Пользователь получает подсказку при регистрации')
@allure.link('https://arivistika.ru', name="Link to Home Page")
def test_fill_form():

    error_text = "Одно или несколько полей содержат ошибочные данные. Пожалуйста, проверьте их и попробуйте ещё раз."
    #error_text = "Контактный телефон"

    with allure.step("Открыть страницу"):
        browser.open('/')
    with allure.step("Ввести имя"):
        home.type_name("Olga")
    with allure.step("Ввести должность"):
        home.type_role("QA engineer")
    #with allure.step("Ввести телефон"):
        #home.type_phone("7921ххххххх") #вызов исключения
    with allure.step("Ввести e-mail"):
        home.type_email("test@test.test")
    with allure.step("Ввести название компании"):
        home.type_company("Test Company")
    with allure.step("Откуда узнали"):
        home.type_some_text("Test Info")
    with allure.step("Опишите цель обучения"):
        home.type_goals("Test Text")
    # with allure.step("Нажать кнопку \"Зарегистрироватья\""):
        # home.registration_button_click() # скрыто на время отладки
        # Expect:
    # with allure.step("Проверить тест сообщения об ошибке"):
    #     home.check_error_alert(error_text) # скрыто на время отладки