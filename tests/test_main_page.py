import allure
from pages.main_page import MainPage
from data.urls import URL

@allure.suite("Тестирование Главной страницы (Конструктора)")
class TestMainPage:

    @allure.title("Проверка открытия модального окна с деталями ингредиента")
    def test_open_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(URL.MAIN_PAGE)
        
        main_page.click_first_ingredient()
        assert main_page.is_modal_header_displayed()

    @allure.title("Проверка закрытия модального окна кликом на крестик")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(URL.MAIN_PAGE)
        
        main_page.click_first_ingredient()
        main_page.click_close_modal_button()
        assert main_page.is_modal_closed()

    @allure.title("Проверка перехода в Ленту заказов по кнопке в хедере")
    def test_navigation_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(URL.MAIN_PAGE)
        
        main_page.click_order_feed_button()
        assert "/feed" in driver.current_url

    @allure.title("Проверка добавления ингредиента в корзину через Drag and Drop")
    def test_drag_and_drop_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(URL.MAIN_PAGE)
        
        main_page.drag_and_drop_ingredient_to_basket()
        counter_value = main_page.get_ingredient_counter_value()
        assert int(counter_value) > 0