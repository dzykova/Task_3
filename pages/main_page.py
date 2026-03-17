import allure
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Нажимаем на кнопку "Личный кабинет"')
    def click_personal_account_button(self):
        self.wait_for_invisability(BasePageLocators.loading)
        element = self.wait_for_clickable(MainPageLocators.personal_account_button)
        self.hard_click(element)

    @allure.step('Нажимаем на игредиент')
    def click_ingredient(self):
        self.wait_for_invisability(BasePageLocators.loading)
        self.click(MainPageLocators.ingredient)

    @allure.step('Получаем детали ингредиента')
    def get_ingredient_details(self):
        return self.get_text(MainPageLocators.ingredient_details_window)
    
    @allure.step('Закрываем окно с деталями ингредиента')
    def click_ingredient_details_window_close_button(self):
        self.click(MainPageLocators.ingredient_details_window_close_button)

    @allure.step('Проверяем видимость окна с деталями ингредиента')
    def is_ingredient_details_visible(self):
        self.is_element_visible(MainPageLocators.ingredient_details_window)

    @allure.step('Нажимаем на кнопку "Лента Заказов"')
    def click_orders_list_button(self):
        self.wait_for_invisability(BasePageLocators.loading)
        element = self.wait_for_clickable(MainPageLocators.orders_list_button)
        self.hard_click(element)

    @allure.step('Ждем загрузки ленты заказов')
    def wait_orders_list_loading(self):
        self._wait.until(lambda d: "/feed" in d.current_url)

    @allure.step('Нажимаем на кнопку "Конструктор"')
    def click_builder_button(self):
        self.wait_for_invisability(BasePageLocators.loading)
        self.click(MainPageLocators.builder_button)

    @allure.step('Добавляем ингредиент')
    def add_ingredient(self):
        self.wait_for_invisability(BasePageLocators.loading)
        ingredient = self.find_element(MainPageLocators.ingredient)
        constructor = self.find_element(MainPageLocators.constructor)
        self.drag_and_drop(ingredient,constructor)

    @allure.step('Получаем значение счестчика ингредиента')
    def get_ingredient_counter(self):
        return self.get_text(MainPageLocators.ingredient_counter)
    
    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_create_order_button(self):
        self.click(MainPageLocators.creare_order_button)

    @allure.step('Получаем подтверждение, что заказ оформлен')
    def get_order_confirmation_details(self):
        self.wait_for_invisability(BasePageLocators.loading)
        return self.get_text(MainPageLocators.order_window)
    
    @allure.step('Закрываем окно подтверждающее оформление заказа')
    def click_order_confirmation_window_close_button(self):
        self.wait_for_invisability(BasePageLocators.loading)
        element = self.wait_for_clickable(MainPageLocators.order_window_close_button)
        self.hard_click(element)

    def create_order(self):
        self.add_ingredient()
        self.click_create_order_button()
        self.click_order_confirmation_window_close_button()

    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        self.wait_for_invisability(BasePageLocators.loading)
        return self.get_text(MainPageLocators.order_number)