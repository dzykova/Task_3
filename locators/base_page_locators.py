from selenium.webdriver.common.by import By


class BasePageLocators:
    loading = [By.CSS_SELECTOR, "[class*='loading']"]