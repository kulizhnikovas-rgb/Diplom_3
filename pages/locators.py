from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    FIRST_INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")   
    MODAL_HEADER = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'modal__close')]")
    BURGER_BASKET = (By.XPATH, "//section[contains(@class, 'basket')]")
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class, 'counter_counter')]/p")
    
class OrderFeedLocators:  
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    ORDERS_IN_PROGRESS_LIST = (By.XPATH, "//ul[contains(@class, 'orderListReady')]")