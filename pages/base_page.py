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

    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def wait_for_invisibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
    
    def wait_for_text_in_element(self, locator, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )
    
    def wait_for_text_to_appear_in_list(self, locator, expected_text, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            lambda driver: expected_text in [el.text for el in driver.find_elements(*locator)]
        )
    
    def wait_for_text_to_disappear_from_element(self, locator, text, timeout=10):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        return WebDriverWait(self.driver, timeout).until_not(
            EC.text_to_be_present_in_element(locator, text)
        )
    
    def drag_and_drop_via_js(self, from_locator, to_locator):
        
        source = self.find_element_with_wait(from_locator)
        target = self.find_element_with_wait(to_locator)
        
        js_script = """
        var src = arguments[0], tgt = arguments[1];
        var dataTransfer = new DataTransfer();
        var emit = function(target, name) {
            var event = new DragEvent(name, { bubbles: true, cancelable: true, dataTransfer: dataTransfer });
            target.dispatchEvent(event);
        };
        emit(src, 'dragstart');
        emit(tgt, 'dragenter');
        emit(tgt, 'dragover');
        emit(tgt, 'drop');
        emit(src, 'dragend');
        """
        self.driver.execute_script(js_script, source, target)