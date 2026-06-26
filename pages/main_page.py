import allure
from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class MainPage(BasePage):
    
    @allure.step("Кликнуть на кнопку 'Конструктор' в хедере")
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)


    @allure.step("Кликнуть на первый ингредиент (булку)")
    def click_first_ingredient(self):
        self.click_element(MainPageLocators.FIRST_INGREDIENT)

    @allure.step("Проверить отображение заголовка модального окна")
    def is_modal_header_displayed(self):
        return self.find_element_with_wait(MainPageLocators.MODAL_HEADER).is_displayed()

    @allure.step("Закрыть модальное окно кликом по крестику")
    def click_close_modal_button(self):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
    ).click()

    @allure.step("Проверить, что модальное окно закрылось (исчезло из DOM)")
    def is_modal_closed(self):
        return self.wait_for_element_to_disappear(MainPageLocators.MODAL_HEADER)

    @allure.step("Перетащить ингредиент в корзину конструктора")
    def drag_and_drop_ingredient_to_basket(self):
        source = self.driver.find_element(*MainPageLocators.FIRST_INGREDIENT)
        target = self.driver.find_element(*MainPageLocators.BURGER_BASKET)
    
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
    
    
    @allure.step("Кликнуть на кнопку 'Оформить заказ'")
    def click_checkout_button(self):
        checkout_btn = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.CHECKOUT_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", checkout_btn)

    @allure.step("Получить номер созданного заказа из модального окна")
    def get_order_number_from_modal(self):
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER_IN_MODAL)
    )
        return self.get_text_after_loader_disappears(
        MainPageLocators.ORDER_NUMBER_IN_MODAL,
        MainPageLocators.ORDER_LOADING_MODAL
    )
    
    @allure.step("Дождаться закрытия модального окна подтверждения заказа")
    def wait_for_order_modal_to_close(self):
        
        self.click_element(MainPageLocators.MODAL_ORDER_CLOSE_BUTTON)
        return self.wait_for_element_to_disappear(MainPageLocators.ORDER_NUMBER_IN_MODAL)
    
    
    @allure.step("Кликнуть по кнопке 'Лента заказов' в хедере с ожиданием кликабельности")
    def click_order_feed_button(self):
   
        order_feed_btn = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_FEED_BUTTON)
        )
        order_feed_btn.click()
    
    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter_value(self):
        return self.find_element_with_wait(MainPageLocators.INGREDIENT_COUNTER).text
