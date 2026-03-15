from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.account_page import AccountPage
from urls import PROFILE_URL, ORDER_HISTORY_URL, LOGIN_PAGE_URL
import allure

class TestPersonalAccount:


    @allure.title('Проверка Личного кабинета - "Профиль"')
    def test_personal_account_profile(self,user,driver):
        
        login_page = LoginPage(driver)
        login_page.open_url(LOGIN_PAGE_URL)
        login_page.login_to_account(user["email"],user["password"])
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        account_page = AccountPage(driver)
        account_page.wait_profile_tab_loading()

        current_url = account_page.get_current_url()

        assert current_url == PROFILE_URL

    @allure.title('Проверка Личного кабинета - "История заказов"')
    def test_personal_account_order_history(self,user,driver):
        
        login_page = LoginPage(driver)
        login_page.open_url(LOGIN_PAGE_URL)
        login_page.login_to_account(user["email"],user["password"])
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        account_page = AccountPage(driver)
        account_page.click_order_history_button()

        current_url = account_page.get_current_url()

        assert current_url == ORDER_HISTORY_URL

    @allure.title('Выход из личного кабинета')
    def test_personal_account_exit(self,user,driver):
        
        login_page = LoginPage(driver)
        login_page.open_url(LOGIN_PAGE_URL)
        login_page.login_to_account(user["email"],user["password"])
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        account_page = AccountPage(driver)
        account_page.click_exit_button()
        login_page.wait_login_page_loading()

        current_url = login_page.get_current_url()

        assert current_url == LOGIN_PAGE_URL