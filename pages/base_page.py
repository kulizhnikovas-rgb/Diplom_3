from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def click_element(self, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def get_text(self, locator):
        return self.find_element_with_wait(locator).text
    
    def wait_for_element_to_disappear(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
    

    
    def wait_for_url_contains(self, url_part, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_part)
        )
    
    def get_text_after_loader_disappears(self, text_locator, loader_locator, time=15):
        WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element_located(loader_locator)
        )
        return self.driver.find_element(*text_locator).text
    
    def find_elements_with_wait(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_all_elements_located(locator)
        )
    
    def click_element_js(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].click();", element)