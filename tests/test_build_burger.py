from pages.login_page import LoginPage
from pages.main_page import MainPage
from urls import BASE_URL, LOGIN_PAGE_URL
import allure

class TestBuildBurger:

    @allure.title('Проверка открытия окна с деталями ингредиента')
    def test_open_igredient_details(self,driver):
        
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_ingredient()

        details = main_page.get_ingredient_details()

        assert 'Детали ингредиента' in details

    @allure.title('Проверка закрытиия окна с деталями ингредиента')
    def test_close_igredient_details(self,driver):
        
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_ingredient()
        main_page.click_ingredient_details_window_close_button()

        assert not main_page.is_ingredient_details_visible()

    @allure.title('Проверка открытия конструктора')
    def test_open_builder(self,driver):
        
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_orders_list_button()
        main_page.wait_orders_list_loading()
        main_page.click_builder_button()

        current_url = main_page.get_current_url()

        assert current_url == BASE_URL

    @allure.title('Проверка увеличения счетчика ингредиента при добавлении в заказ')
    def test_increase_igredient_counter_after_adding_to_order(self,driver):
        
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.add_ingredient()
        
        counter = main_page.get_ingredient_counter()

        assert counter == '2'

    @allure.title('Проверка, что залогиненный пользователь может создать заказ')
    def test_create_order_authorized_user(self,user,driver):
        
        login_page = LoginPage(driver)
        login_page.open_url(LOGIN_PAGE_URL)
        login_page.login_to_account(user["email"],user["password"])
        main_page = MainPage(driver)
        main_page.add_ingredient()
        main_page.click_create_order_button()

        details = main_page.get_order_confirmation_details()

        assert 'идентификатор заказа' in details
        