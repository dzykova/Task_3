from pages.login_page import LoginPage
from urls import LOGIN_PAGE_URL
import allure
from data.user_data import UserData

class TestRecoverPassword:

    @allure.title('Проверка восстановления пароля')
    def test_recover_password(self,driver):
        
        login_page = LoginPage(driver)
        login_page.open_url(LOGIN_PAGE_URL)
        login_page.click_recover_password_button()
        login_page.set_email_in_recover_password_form(UserData.USER_DATA_1["email"])
        login_page.click_recover_button()
        login_page.click_eye_icon()

        test_class = login_page.get_class_for_password_field("class")

        assert "input_status_active" in test_class       