from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.orders_page import OrdersPage
from pages.account_page import AccountPage
from urls import BASE_URL, ORDERS_LIST_URL, LOGIN_PAGE_URL
import allure

class TestOrdersList:

    @allure.title('Проверка открытия ленты заказов')
    def test_open_orders_list(self,driver):
        
        main_page = MainPage(driver)
        main_page.open_url(BASE_URL)
        main_page.click_orders_list_button()
        main_page.wait_orders_list_loading()

        current_url = main_page.get_current_url()

        assert current_url == ORDERS_LIST_URL

    @allure.title('Проверка открытия окна с деталями заказа')
    def test_open_order_details(self,user,driver):
        
        login_page = LoginPage(driver)
        login_page.open_url(LOGIN_PAGE_URL)
        login_page.login_to_account(user["email"],user["password"])
        main_page = MainPage(driver)
        main_page.create_order()
        main_page.click_orders_list_button()
        orders_page = OrdersPage(driver)
        orders_page.click_order()
        
        details = orders_page.get_order_details()

        assert 'Cостав' in details

    @allure.title('Проверка, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_compare_orders_in_different_pages_authorized_user(self,user,driver):
        
        login_page = LoginPage(driver)
        login_page.open_url(LOGIN_PAGE_URL)
        login_page.login_to_account(user["email"],user["password"])
        main_page = MainPage(driver)
        main_page.create_order()
        main_page.click_personal_account_button()
        account_page = AccountPage(driver)
        account_page.click_order_history_button()
        
        order_number_1 = account_page.get_order_number()
        
        main_page.click_orders_list_button()
        orders_page = OrdersPage(driver)
        
        order_number_2 = orders_page.get_order_number()

        assert order_number_1 == order_number_2

    @allure.title('Проверка увеличения счётчика "Выполнено за всё время" при создании нового заказа')
    def test_increase_orders_for_all_time_counter(self,user,driver):
        
        login_page = LoginPage(driver)
        login_page.open_url(LOGIN_PAGE_URL)
        login_page.login_to_account(user["email"],user["password"])
        main_page = MainPage(driver)
        main_page.click_orders_list_button()
        orders_page = OrdersPage(driver)

        orders_for_all_time_1 = int(orders_page.get_orders_for_all_time())

        main_page.click_builder_button()
        main_page = MainPage(driver)
        main_page.create_order()
        main_page.click_orders_list_button()

        orders_for_all_time_2 = int(orders_page.get_orders_for_all_time())

        assert orders_for_all_time_2 == orders_for_all_time_1 + 1

    @allure.title('Проверка увеличения счётчика "Выполнено за сегодня" при создании нового заказа')
    def test_increase_orders_for_today_counter(self,user,driver):
        
        login_page = LoginPage(driver)
        login_page.open_url(LOGIN_PAGE_URL)
        login_page.login_to_account(user["email"],user["password"])
        main_page = MainPage(driver)
        main_page.click_orders_list_button()
        orders_page = OrdersPage(driver)

        orders_for_today_1 = int(orders_page.get_orders_for_today())

        main_page.click_builder_button()
        main_page = MainPage(driver)
        main_page.create_order()
        main_page.click_orders_list_button()

        orders_for_today_2 = int(orders_page.get_orders_for_today())

        assert orders_for_today_2 == orders_for_today_1 + 1

    @allure.title('Проверка отображения созданного заказа в разделе "В работе"')
    def test_display_created_order_in_in_progress_section(self,user,driver):
        
        login_page = LoginPage(driver)
        login_page.open_url(LOGIN_PAGE_URL)
        login_page.login_to_account(user["email"],user["password"])
        main_page = MainPage(driver)
        main_page.create_order()

        order_number_1 = int(main_page.get_order_number())

        main_page.click_orders_list_button()
        orders_page = OrdersPage(driver)
        
        order_number_2 = int(orders_page.get_in_progress_order())

        assert order_number_1 == order_number_2