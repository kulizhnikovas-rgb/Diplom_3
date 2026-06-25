import allure
from pages.base_page import BasePage
from pages.locators import OrderFeedLocators

class OrderFeedPage(BasePage):

    @allure.step("Получить значение счетчика 'Выполнено за всё время'")
    def get_total_orders_value(self):
        return self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNTER)

    @allure.step("Получить значение счетчика 'Выполнено за сегодня'")
    def get_today_orders_value(self):
        return self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNTER)

    @allure.step("Получить текст списка номеров заказов из раздела 'В работе'")
    def get_orders_in_progress_text(self):
        return self.get_text(OrderFeedLocators.ORDERS_IN_PROGRESS_LIST)