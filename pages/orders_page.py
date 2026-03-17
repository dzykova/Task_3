import allure
from locators.orders_page_locators import OrdersPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage

class OrdersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Нажимаем на заказ')
    def click_order(self):
        element = self.wait_for_clickable(OrdersPageLocators.order)
        self.hard_click(element)

    @allure.step('Получаем детали заказа')
    def get_order_details(self):
        return self.get_text(OrdersPageLocators.order_details_window)
    
    @allure.step('Получаем номер заказа"')
    def get_order_number(self):
        self.wait_for_invisability(BasePageLocators.loading)
        self.wait_for_visability(OrdersPageLocators.order_number)
        return self.get_text(OrdersPageLocators.order_number)
    
    @allure.step('Получаем количество заказов за все время"')
    def get_orders_for_all_time(self):
        self.wait_for_invisability(BasePageLocators.loading)
        self.wait_for_visability(OrdersPageLocators.orders_for_all_time_counter)
        return self.get_text(OrdersPageLocators.orders_for_all_time_counter)
    
    @allure.step('Получаем количество заказов за сегодня"')
    def get_orders_for_today(self):
        self.wait_for_invisability(BasePageLocators.loading)
        self.wait_for_visability(OrdersPageLocators.orders_for_today)
        return self.get_text(OrdersPageLocators.orders_for_today)
    
    @allure.step('Получаем номер заказа в секции "В работе"')
    def get_in_progress_order(self):
        self.wait_for_invisability(BasePageLocators.loading)
        self.wait_for_visability(OrdersPageLocators.in_progress_order)
        return self.get_text(OrdersPageLocators.in_progress_order)