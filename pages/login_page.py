import allure
from locators.login_page_locators import LoginPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Нажимаем на кнопку "Восстановить пароль"')
    def click_recover_password_button(self):
        self.wait_for_invisability(BasePageLocators.loading)
        self.click(LoginPageLocators.recover_password_button)

    @allure.step('Вводим почту в форме восстановления пароля')
    def set_email_in_recover_password_form(self, email):
        self.type(LoginPageLocators.email_field,email)

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def click_recover_button(self):
        self.click(LoginPageLocators.recover_button)

    @allure.step('Нажимаем на иконку "Показать пароль"')
    def click_eye_icon(self):
        self.wait_for_invisability(BasePageLocators.loading)
        self.click(LoginPageLocators.eye_icon)
    
    @allure.step('Получаем подсветку для поля "Пароль"')
    def get_class_for_password_field(self, attribute):
        return self.get_attribute(LoginPageLocators.password_field,attribute)
    
    @allure.step('Вводим почту')
    def set_email(self, email):
        self.wait_for_invisability(BasePageLocators.loading)
        self.type(LoginPageLocators.email_field,email)

    @allure.step('Вводим пароль')
    def set_password(self, password):
        self.wait_for_invisability(BasePageLocators.loading)
        self.type(LoginPageLocators.password_input,password)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_enter_button(self):
        self.click(LoginPageLocators.enter_button)

    @allure.step('Заходим в аккаунт')
    def login_to_account(self,email,password):
        self.set_email(email)
        self.set_password(password)
        self.click_enter_button()

    @allure.step('Ждем загрузки страницы входа в аккаунт')
    def wait_login_page_loading(self):
        self.wait_for_loading("/login")
    

    