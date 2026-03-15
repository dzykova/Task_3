from selenium.webdriver.common.by import By


class LoginPageLocators:
    recover_password_button = [By.XPATH, ".//*[text()='Восстановить пароль']"]
    email_field = [By.XPATH, ".//*[text()='Email']/parent::div/input"]
    recover_button = [By.XPATH, ".//*[text()='Восстановить']"]
    eye_icon = [By.CLASS_NAME, "input__icon-action"]
    password_field = [By.XPATH, ".//*[text()='Пароль']/parent::div"]
    loading = [By.CSS_SELECTOR, "[class*='loading']"]
    password_input = [By.XPATH, ".//*[text()='Пароль']/parent::div/input"]
    enter_button = [By.XPATH, ".//*[text()='Войти']"]
