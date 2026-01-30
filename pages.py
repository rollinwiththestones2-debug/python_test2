from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")

    CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(text(),'Call a taxi')]")

    SUPPORTIVE_TARIFF = (
        By.XPATH,
        "//div[contains(@class,'tcard') and .//div[text()='Supportive']]"
    )

    PHONE_BUTTON = (By.CLASS_NAME, "np-text")
    PHONE_INPUT = (By.ID, "phone")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Next')]")

    SMS_CODE_FIELD = (By.ID, "code")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(),'Confirm')]")

    PAYMENT_METHOD = (By.CLASS_NAME, "pp-button")
    ADD_CARD_BUTTON = (By.XPATH, "//div[contains(text(),'Add card')]")
    CARD_NUMBER_FIELD = (By.ID, "number")
    CARD_CODE_FIELD = (By.ID, "code")
    LINK_BUTTON = (By.XPATH, "//button[contains(text(),'Link')]")

    COMMENT_FIELD = (By.ID, "comment")

    BLANKET_SWITCH = (By.CLASS_NAME, "r-sw")
    BLANKET_CHECKBOX = (By.CLASS_NAME, "switch-input")

    ICE_CREAM_PLUS = (By.CLASS_NAME, "counter-plus")
    ICE_CREAM_COUNT = (By.CLASS_NAME, "counter-value")

    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Order')]")
    CAR_SEARCH_MODAL = (By.CLASS_NAME, "order-body")

    def set_route(self, address_from, address_to):
        self.wait.until(EC.element_to_be_clickable(self.FROM_FIELD)).send_keys(address_from)
        self.wait.until(EC.element_to_be_clickable(self.TO_FIELD)).send_keys(address_to)

    def get_from_value(self):
        return self.driver.find_element(*self.FROM_FIELD).get_property("value")

    def get_to_value(self):
        return self.driver.find_element(*self.TO_FIELD).get_property("value")

    def call_taxi(self):
        self.wait.until(EC.element_to_be_clickable(self.CALL_TAXI_BUTTON)).click()

    def select_supportive_tariff(self):
        self.wait.until(EC.element_to_be_clickable(self.SUPPORTIVE_TARIFF)).click()

    def is_supportive_selected(self):
        supportive_card = self.driver.find_element(*self.SUPPORTIVE_TARIFF)
        return "active" in supportive_card.get_attribute("class")

    def enter_phone_number(self, phone_number):
        self.wait.until(EC.element_to_be_clickable(self.PHONE_BUTTON)).click()
        phone_input = self.wait.until(EC.visibility_of_element_located(self.PHONE_INPUT))
        phone_input.send_keys(phone_number)
        self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON)).click()

    def get_phone_value(self):
        return self.driver.find_element(*self.PHONE_INPUT).get_property("value")

    def submit_sms_code(self, code):
        self.wait.until(EC.visibility_of_element_located(self.SMS_CODE_FIELD)).send_keys(code)
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON)).click()

    def add_card(self, number, code):
        self.wait.until(EC.element_to_be_clickable(self.PAYMENT_METHOD)).click()
        self.wait.until(EC.element_to_be_clickable(self.ADD_CARD_BUTTON)).click()

        self.wait.until(EC.visibility_of_element_located(self.CARD_NUMBER_FIELD)).send_keys(number)

        cvv = self.wait.until(EC.visibility_of_element_located(self.CARD_CODE_FIELD))
        cvv.send_keys(code)
        cvv.send_keys(Keys.TAB)

        self.wait.until(EC.element_to_be_clickable(self.LINK_BUTTON)).click()

    def payment_method_is_card(self):
        return "Card" in self.driver.find_element(*self.PAYMENT_METHOD).text

    def add_comment(self, message):
        field = self.wait.until(EC.element_to_be_clickable(self.COMMENT_FIELD))
        field.clear()
        field.send_keys(message)

    def get_comment_value(self):
        return self.driver.find_element(*self.COMMENT_FIELD).get_property("value")

    def toggle_blanket(self):
        self.wait.until(EC.element_to_be_clickable(self.BLANKET_SWITCH)).click()

    def blanket_is_selected(self):
        return self.driver.find_element(*self.BLANKET_CHECKBOX).get_property("checked")

    def add_ice_creams(self, count):
        for _ in range(count):
            self.wait.until(EC.element_to_be_clickable(self.ICE_CREAM_PLUS)).click()

    def get_ice_cream_count(self):
        return int(self.driver.find_element(*self.ICE_CREAM_COUNT).text)

    def order_taxi(self):
        self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON)).click()

    def car_search_modal_is_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CAR_SEARCH_MODAL)
        ).is_displayed()
