from selenium.webdriver.common.by import By


class OrdersPageLocators:
    order = [By.XPATH, "(//a[contains(@class,'OrderHistory_link')])[1]"]
    order_details_window = [By.XPATH, "//div[contains(@class,'Modal_orderBox')]/p[contains(@class,'text_type_main-medium')]"]
    order_number = [By.XPATH, "(//a[contains(@class,'OrderHistory_link')]//p[contains(@class,'text_type_digits-default')])[1]"]
    orders_for_all_time_counter = [By.XPATH, ".//*[text()='Выполнено за все время:']/parent::div/p[contains(@class,'OrderFeed_number')]"]
    orders_for_today = [By.XPATH, ".//*[text()='Выполнено за сегодня:']/parent::div/p[contains(@class,'OrderFeed_number')]"]
    in_progress_order = [By.XPATH, "(//ul[contains(@class,'OrderFeed_orderListReady')]/li)[1]"]