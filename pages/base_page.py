from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(driver, 5)

    @allure.step('Получаем текущую ссылку')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Открываем ссылку')
    def open_url(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def hard_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text
    
    def get_attribute(self, locator, attribute):
        return self.driver.find_element(*locator).get_attribute(attribute)
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def wait_for_clickable(self, locator):
        return self._wait.until(EC.element_to_be_clickable(locator))  
  
    def wait_for_presence(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))
    
    def wait_for_invisability(self, locator):
        return self._wait.until(EC.invisibility_of_element_located(locator))
    
    def wait_for_visability(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def is_element_visible(self, locator):
        return self.driver.find_element(*locator).is_displayed()
    
    def wait(self):
        time.sleep(3)
    
    def drag_and_drop(self,element,place):
        self.driver.execute_script("""
        function simulateDragDrop(sourceNode, destinationNode) {
            const EVENT_TYPES = ['dragstart','dragover','drop','dragend'];

            function createCustomEvent(type) {
                const event = new CustomEvent(type, {bubbles: true, cancelable: true});
                event.dataTransfer = {
                    data: {},
                    setData: function(k,v){ this.data[k] = v; },
                    getData: function(k){ return this.data[k]; }
                };
                return event;
            }

            const dragStartEvent = createCustomEvent('dragstart');
            sourceNode.dispatchEvent(dragStartEvent);

            const dropEvent = createCustomEvent('drop');
            dropEvent.dataTransfer = dragStartEvent.dataTransfer;
            destinationNode.dispatchEvent(dropEvent);

            const dragEndEvent = createCustomEvent('dragend');
            dragEndEvent.dataTransfer = dragStartEvent.dataTransfer;
            sourceNode.dispatchEvent(dragEndEvent);
        }

        simulateDragDrop(arguments[0], arguments[1]);
        """, element, place)