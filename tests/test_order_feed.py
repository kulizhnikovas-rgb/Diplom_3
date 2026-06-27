import allure
from data.urls import URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import OrderFeedLocators
from pages.locators import MainPageLocators

@allure.suite("Тестирование Ленты заказов")
class TestOrderFeed:

    @allure.title("Проверка активности счётчиков в Ленте заказов")
    def test_order_feed_counters(self, main_page, order_feed_page, make_ui_order):
        make_ui_order()
        
        main_page.click_order_feed_button()
        
        assert order_feed_page.get_total_orders_value().isdigit()
        assert order_feed_page.get_today_orders_value().isdigit()

    @allure.title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_total_orders_counter_increases(self, main_page, order_feed_page, make_ui_order):
        
        main_page.open_page(URL.MAIN_PAGE)
        main_page.click_order_feed_button()
        before_total = int(order_feed_page.get_total_orders_value())

        make_ui_order()
        
      
        main_page.click_order_feed_button()
        after_total = int(order_feed_page.get_total_orders_value())
        assert after_total > before_total 
    
    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_number_appears_in_work_section(self, main_page, order_feed_page, make_ui_order):
        raw_order = str(make_ui_order()).strip()
        order_num = f"0{raw_order}"
    
        main_page.click_order_feed_button()
    
        order_feed_page.wait_for_order_to_appear(order_num)
    
        assert order_num in order_feed_page.get_orders_in_progress_values()

    @allure.title("При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_orders_counter_increases(self, main_page, order_feed_page, make_ui_order):
        main_page.open_page(URL.MAIN_PAGE)
        main_page.click_order_feed_button()
        before_today = int(order_feed_page.get_today_orders_value())

        make_ui_order()
        
        main_page.click_order_feed_button()
        order_feed_page.wait_for_today_counter_to_change(before_today)
        after_today = int(order_feed_page.get_today_orders_value())
        assert after_today > before_today