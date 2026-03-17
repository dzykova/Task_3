from selenium.webdriver.common.by import By


class MainPageLocators:
    personal_account_button = [By.XPATH, ".//*[text()='Личный Кабинет']/parent::a"]
    ingredient_details_window = [By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']/div/h2"]
    ingredient_details_window_close_button = [By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']/button"]
    orders_list_button = [By.XPATH, ".//*[text()='Лента Заказов']/parent::a"]
    builder_button = [By.XPATH, ".//*[text()='Конструктор']/parent::a"]
    ingredient_counter = [By.XPATH, ".//*[text()='Флюоресцентная булка R2-D3']/parent::a/div[contains(@class,'counter')]/p"]
    ingredient = [By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']"]
    constructor = [By.XPATH, "//section[contains(@class,'BurgerConstructor')]"]
    creare_order_button = [By.XPATH, ".//button[text()='Оформить заказ']"]
    order_window = [By.XPATH, "//div[contains(@class,'Modal_modal__container')]/div/p"]
    order_window_close_button = [By.XPATH, "//div[contains(@class,'Modal_modal__container')]/button"]
    order_number = [By.XPATH, "//div[contains(@class,'Modal_modal__container')]/div/h2"]