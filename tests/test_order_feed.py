import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from data.urls import URL

@allure.suite("Тестирование Ленты заказов")
class TestOrderFeed:

    @allure.title("Проверка активности счётчиков в Ленте заказов")
    def test_order_feed_counters(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.open_page(URL.MAIN_PAGE)
        main_page.click_order_feed_button()
        
        total_orders = order_feed_page.get_total_orders_value()
        today_orders = order_feed_page.get_today_orders_value()
        
        assert total_orders.isdigit()
        assert today_orders.isdigit()