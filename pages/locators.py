from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    FIRST_INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")   
    MODAL_HEADER = (By.XPATH, "//h2[text()='Детали ингредиента']")
    BURGER_BASKET = (By.XPATH, "//section[contains(@class, 'basket')]")
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class, 'counter_counter')]/p")
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_LOADING_MODAL = (By.CLASS_NAME, "Modal_modal__loading__3534A")
    ORDER_NUMBER_IN_MODAL = (By.CSS_SELECTOR, ".text_type_digits-large")
    MODAL_ORDER_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    EMAIL_INPUT = (By.XPATH, ".//input[@type='text' or @name='name']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    MODAL_OVERLAY = (By.XPATH, "//*[contains(@class, 'Modal_modal_overlay')]")
    
class OrderFeedLocators:  
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    ORDERS_IN_PROGRESS_LIST = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul/li")