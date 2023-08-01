from selene import browser, be, by
from selene.support.conditions import be, have

class LoginPageMethods:

    def fill_username(self, s):
        browser.element('#username').should(be.blank).type(s)

    def fill_password(self, s):
        browser.element('#password').should(be.blank).type(s)

    def click_login_button(self):
        browser.element('[name="login"]').click()

    def check_error_alert(self, data):
        browser.element('.woocommerce-error').should(
            have.text(data))

