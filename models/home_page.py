from selene import browser, by
from selene.support.conditions import have, be

class HomePageMethods:

    def check_title(self, s):
        browser.element('.site-branding').should(have.text(s))

    def check_adress(self, s):
        browser.element('.footer-address').should(have.text(s))

    def check_paragraf_text(self, s):
        browser.element(by.text(s)).should(be.visible)

    def check_mail(self, s):
        browser.element(by.link_text(s)).should(be.visible)

    def type_name(self, s):
        browser.element('input[placeholder="Ваше имя"]').should(be.blank).type(s)

    def type_role(self, s):
        browser.element('input[placeholder="Должность"]').should(be.blank).type(s)

    def type_phone(self, s):
        browser.element('input[placeholder="Контактный телефон"]').should(be.blank).type(s)

    def type_email(self, s):
        browser.element('input[placeholder="Ваш email"]').should(be.blank).type(s)

    def type_company(self, s):
        browser.element('input[placeholder="Название компании"]').should(be.blank).type(s)

    def type_some_text(self, s):
        browser.element('input[placeholder="Откуда узнали"]').should(be.blank).type(s)

    def type_goals(self, s):
        browser.element('textarea[placeholder="Опишите цель обучения"]').type(s)

    def registration_button_click(self):
        browser.element('input[value="Зарегистрироваться"]').click()

    def check_error_alert(self, s):
        alert = browser.element('.wpcf7-response-output [role="alert"]')
        alert.should(have.text(s))



