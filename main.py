from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        # Sprint 7 server availability check
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print('Connected to the Urban Routes server')
        else:
            print('Cannot connect to Urban Routes. Check the server is on and still running')

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_set_address(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        assert page.get_from_value() == data.ADDRESS_FROM
        assert page.get_to_value() == data.ADDRESS_TO

    def test_select_supportive_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.call_taxi()
        page.select_supportive_tariff()

        assert page.is_supportive_selected() is True

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.call_taxi()
        page.select_supportive_tariff()
        page.enter_phone_number(data.PHONE_NUMBER)

        code = helpers.retrieve_phone_code(self.driver)
        page.submit_sms_code(code)

        assert page.get_phone_value() == data.PHONE_NUMBER

    def test_add_credit_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.call_taxi()
        page.select_supportive_tariff()
        page.add_card(data.CARD_NUMBER, data.CARD_CODE)

        assert page.payment_method_is_card() is True

    def test_add_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.call_taxi()
        page.select_supportive_tariff()

        page.add_comment(data.MESSAGE_FOR_DRIVER)

        assert page.get_comment_value() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.call_taxi()
        page.select_supportive_tariff()
        page.toggle_blanket()

        assert page.blanket_is_selected() is True

    def test_order_two_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.call_taxi()
        page.select_supportive_tariff()
        page.add_ice_creams(2)

        assert page.get_ice_cream_count() == 2

    def test_order_taxi_supportive(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.call_taxi()
        page.select_supportive_tariff()
        page.enter_phone_number(data.PHONE_NUMBER)

        code = helpers.retrieve_phone_code(self.driver)
        page.submit_sms_code(code)

        page.add_comment(data.MESSAGE_FOR_DRIVER)
        page.order_taxi()

        assert page.car_search_modal_is_visible() is True

