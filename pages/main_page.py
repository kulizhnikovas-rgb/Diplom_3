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
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)
    
    @allure.step("Проверить, что модальное окно закрылось (исчезло из DOM)")
    def is_modal_closed(self):
        return self.wait_for_element_to_disappear(MainPageLocators.MODAL_HEADER)

    @allure.step("Перетащить ингредиент в корзину конструктора")
    def drag_and_drop_ingredient_to_basket(self):
        self.drag_and_drop_via_js(
            MainPageLocators.FIRST_INGREDIENT, 
            MainPageLocators.BURGER_BASKET
        )
    
    
    @allure.step("Кликнуть на кнопку 'Оформить заказ'")
    def click_checkout_button(self):
        self.click_element_js(MainPageLocators.CHECKOUT_BUTTON)

    @allure.step("Получить номер созданного заказа из модального окна")
    def get_order_number_from_modal(self):
        self.wait_for_visibility(MainPageLocators.ORDER_NUMBER_IN_MODAL)
        
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
       self.click_element(MainPageLocators.ORDER_FEED_BUTTON)
    
    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter_value(self):
        return self.find_element_with_wait(MainPageLocators.INGREDIENT_COUNTER).text
