from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # =====================
    # Locators
    # =====================

    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")

    CALL_TAXI_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Call a taxi')]"
    )

    SUPPORTIVE_TARIFF = (
        By.XPATH,
        "//div[contains(@class, 'tcard') and .//div[text()='Supportive']]"
    )

    PHONE_NUMBER_FIELD = (By.CLASS_NAME, "np-text")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Next')]")

    SMS_CODE_FIELD = (By.ID, "code")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(),'Confirm')]")

    PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, "pp-button")
    ADD_CARD_BUTTON = (By.XPATH, "//div[contains(text(),'Add card')]")

    CARD_NUMBER_FIELD = (By.ID, "number")
    CARD_CODE_FIELD = (By.XPATH, "//input[@placeholder='12']")
    LINK_BUTTON = (By.XPATH, "//button[contains(text(),'Link')]")

    CLOSE_PAYMENT_MODAL = (
        By.XPATH,
        "//button[@class='close-button section-close']"
    )

    MESSAGE_FOR_DRIVER_FIELD = (By.ID, "comment")

    BLANKET_SWITCH = (By.XPATH, "//div[@class='r-sw']")
    BLANKET_CHECKBOX = (By.CLASS_NAME, "switch-input")

    ICE_CREAM_COUNTER = (By.CLASS_NAME, "counter-plus")

    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Order')]")

    # =====================
    # Methods
    # =====================

    def set_from(self, from_address: str) -> None:
        field = self.wait.until(EC.element_to_be_clickable(self.FROM_FIELD))
        field.clear()
        field.send_keys(from_address)

    def set_to(self, to_address: str) -> None:
        field = self.wait.until(EC.element_to_be_clickable(self.TO_FIELD))
        field.clear()
        field.send_keys(to_address)

    def get_from(self) -> str:
        return self.driver.find_element(*self.FROM_FIELD).get_property("value")

    def get_to(self) -> str:
        return self.driver.find_element(*self.TO_FIELD).get_property("value")

    def click_call_taxi_button(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.CALL_TAXI_BUTTON)).click()

    def select_supportive_tariff(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.SUPPORTIVE_TARIFF)).click()

    def set_phone_number(self, phone_number: str) -> None:
        self.wait.until(
            EC.element_to_be_clickable(self.PHONE_NUMBER_FIELD)
        ).send_keys(phone_number)

    def click_next_button(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON)).click()

    def set_sms_code(self, sms_code: str) -> None:
        self.wait.until(
            EC.visibility_of_element_located(self.SMS_CODE_FIELD)
        ).send_keys(sms_code)

    def click_confirm_button(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON)).click()

    def click_payment_method_button(self) -> None:
        self.wait.until(
            EC.element_to_be_clickable(self.PAYMENT_METHOD_BUTTON)
        ).click()

    def click_add_card_button(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.ADD_CARD_BUTTON)).click()

    def set_card_number(self, card_number: str) -> None:
        self.wait.until(
            EC.visibility_of_element_located(self.CARD_NUMBER_FIELD)
        ).send_keys(card_number)

    def set_card_code(self, card_code: str) -> None:
        self.wait.until(
            EC.visibility_of_element_located(self.CARD_CODE_FIELD)
        ).send_keys(card_code)

    def click_link_button(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.LINK_BUTTON)).click()

    def close_payment(self) -> None:
        self.wait.until(
            EC.element_to_be_clickable(self.CLOSE_PAYMENT_MODAL)
        ).click()

    def add_message_for_driver(self, message: str) -> None:
        self.wait.until(
            EC.element_to_be_clickable(self.MESSAGE_FOR_DRIVER_FIELD)
        ).send_keys(message)

    def toggle_blanket(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.BLANKET_SWITCH)).click()

    def add_ice_cream(self) -> None:
        self.wait.until(
            EC.element_to_be_clickable(self.ICE_CREAM_COUNTER)
        ).click()

    def click_order_button(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON)).click()