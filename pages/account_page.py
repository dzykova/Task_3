import allure
from locators.account_page_locators import AccountPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage

class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Ждем загрузки "Профиль" табы')
    def wait_profile_tab_loading(self):
        self._wait.until(lambda d: "/profile" in d.current_url)
    
    @allure.step('Нажимаем на кнопку "История заказов"')
    def click_order_history_button(self):
        self.wait_for_invisability(BasePageLocators.loading)
        self.wait_for_clickable(AccountPageLocators.order_history_button).click()

    @allure.step('Нажимаем на кнопку "Выйти"')
    def click_exit_button(self):
        self.wait_for_invisability(BasePageLocators.loading)
        self.wait_for_clickable(AccountPageLocators.exit_button).click()

    @allure.step('Получаем номер заказа"')
    def get_order_number(self):
        self.wait_for_presence(AccountPageLocators.order_number)
        return self.get_text(AccountPageLocators.order_number)