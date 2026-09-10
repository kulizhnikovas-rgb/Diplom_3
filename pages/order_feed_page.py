import allure
from pages.base_page import BasePage
from pages.locators import OrderFeedLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class OrderFeedPage(BasePage):

    @allure.step("Получить значение счетчика 'Выполнено за всё время'")
    def get_total_orders_value(self):
        return self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNTER)

    @allure.step("Получить значение счетчика 'Выполнено за сегодня'")
    def get_today_orders_value(self):
        return self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNTER)

    @allure.step("Получить текст списка номеров заказов из раздела 'В работе'")
    def get_orders_in_progress_values(self):
    
        elements = self.find_elements_with_wait(OrderFeedLocators.ORDERS_IN_PROGRESS_LIST)
        
        order_numbers = []
        
        for el in elements:
            order_numbers.append(el.text)
            
      
        return order_numbers
    
    @allure.step("Дождаться обновления счётчика и получить его значение")
    def wait_and_get_total_orders_value(self, expected_value):
        self.wait_for_text_in_element(OrderFeedLocators.TOTAL_ORDERS_COUNTER, str(expected_value))
        return int(self.get_total_orders_value())
    
    @allure.step("Получить список номеров заказов в разделе 'В работе'")
    def get_orders_in_progress_values(self):
        elements = self.find_elements_with_wait(OrderFeedLocators.ORDERS_IN_PROGRESS_LIST)
        return [el.text for el in elements]
    
    def wait_for_order_to_appear(self, order_num):
        self.wait_for_text_to_appear_in_list(
            OrderFeedLocators.ORDERS_IN_PROGRESS_LIST, 
            str(order_num)
        )
        
    def wait_and_get_total_orders_value(self, expected_value):
        self.wait_for_text_in_element(OrderFeedLocators.TOTAL_ORDERS_COUNTER, str(expected_value))
        return int(self.get_total_orders_value())
    
    @allure.step("Дождаться изменения счётчика заказов за сегодня")
    def wait_for_today_counter_to_change(self, before_value):
        self.wait_for_text_to_disappear_from_element(
            OrderFeedLocators.TODAY_ORDERS_COUNTER, 
            str(before_value)
        )