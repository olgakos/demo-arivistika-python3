from selene import browser, by
from selene.support.conditions import have, be

class CoursePageMethods:
    def check_title_dec(self, s):
        browser.element(by.text(s)).should(be.visible);

    def click_button_more(self):
        browser.element(".buy-course-block a[href*='course-pro-declaration']").click()

    def click_button_bay(self):
        browser.element(by.text("Купить этот курс")).click()

    def button_pay_is_visible(self, data):
        browser.all('#paymentComponent').element_by(have.text(data)).should(be.visible)