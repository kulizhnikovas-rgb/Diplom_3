import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from pages.locators import MainPageLocators
import time

class MainPage(BasePage):
    
    @allure.step("Кликнуть на кнопку 'Конструктор' в хедере")
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на кнопку 'Лента заказов' в хедере")
    def click_order_feed_button(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

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
        return WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(MainPageLocators.MODAL_HEADER)
        )

    @allure.step("Перетащить ингредиент в корзину конструктора")
    def drag_and_drop_ingredient_to_basket(self):
        ingredient = self.find_element_with_wait(MainPageLocators.FIRST_INGREDIENT)
        basket = self.find_element_with_wait(MainPageLocators.BURGER_BASKET)
    
        actions = ActionChains(self.driver)
    
        actions.click_and_hold(ingredient).move_to_element(basket).release().perform()
    
        time.sleep(1)
    
    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter_value(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNTER)

