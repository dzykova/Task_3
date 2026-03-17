from selenium.webdriver.common.by import By


class AccountPageLocators:
    order_history_button = [By.XPATH, ".//*[text()='История заказов']"]
    exit_button = [By.XPATH, ".//*[text()='Выход']"]
    order_number = [By.XPATH, "(//a[contains(@class,'OrderHistory_link')]//p[contains(@class,'text_type_digits-default')])[1]"]