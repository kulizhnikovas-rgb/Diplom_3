import pytest
import random
import allure
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from pages.locators import MainPageLocators
from data.urls import URL
from pages.order_feed_page import OrderFeedPage

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        driver.set_window_size(1920, 1080) 
    
    yield driver
    
    driver.quit()

@pytest.fixture
def user():
    random_num = random.randint(100000, 999999)
    user_data = {
        "email": f"kotsar_{random_num}@yandex.ru",
        "password": f"pass_{random_num}",
        "name": f"Sofya_{random_num}"
    }

    with allure.step("Предусловие: Регистрация нового пользователя"):
        response = requests.post(URL.CREATE_USER, json=user_data)
        token = response.json().get("accessToken")
        
    yield user_data, token, response

    if token:
        with allure.step("Постусловие: Удаление пользователя"):
            requests.delete(URL.USER_DATA, headers={"Authorization": token})

@pytest.fixture
def make_ui_order(main_page, user):
    def _make_order():
        user_data, _, _ = user
        
        main_page.open_page(URL.MAIN_PAGE)

        try:
            close_btn = WebDriverWait(main_page.driver, 2).until(
        EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
    )
            close_btn.click()
        except:
            pass
        
        main_page.click_element(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)
        
        main_page.find_element_with_wait(MainPageLocators.EMAIL_INPUT).send_keys(user_data["email"])
        main_page.find_element_with_wait(MainPageLocators.PASSWORD_INPUT).send_keys(user_data["password"])
        main_page.click_element(MainPageLocators.LOGIN_BUTTON)
        
  
        WebDriverWait(main_page.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.CHECKOUT_BUTTON)
        )
        main_page.drag_and_drop_ingredient_to_basket()
        
        WebDriverWait(main_page.driver, 10).until_not(
            EC.visibility_of_element_located(MainPageLocators.MODAL_OVERLAY)
        )
        main_page.click_checkout_button()
        
        WebDriverWait(main_page.driver, 10).until_not(
            EC.text_to_be_present_in_element(MainPageLocators.ORDER_NUMBER_IN_MODAL, "9999")
        )
    
  
        order_num = main_page.get_order_number_from_modal()
        main_page.wait_for_order_modal_to_close()
        
        return order_num
        
    return _make_order

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)