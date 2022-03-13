from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from element_mapper.element_mapper import AllVariables


class Campaigns:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def launch_page(self):
        self.driver.get(AllVariables.payment_page)


    def select_payment_currency(self):
        self.driver.get(AllVariables.payment_page)
        currency_dropdown = self.driver.find_element(By.CSS_SELECTOR, AllVariables.currency)
        select_currency = Select(currency_dropdown)
        select_currency.select_by_visible_text("EUR")
        self.driver.implicitly_wait(20)


    def make_paypal_payment(self):
        self.driver.get(AllVariables.payment_page)
        currency_dropdown = self.driver.find_element(By.CSS_SELECTOR, AllVariables.currency)
        select_currency = Select(currency_dropdown)
        select_currency.select_by_visible_text("EUR")
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.CSS_SELECTOR, "#paypal-button").click()


    def make_creditcard_payment(self):
        self.driver.get(AllVariables.payment_page)
        currency_dropdown = self.driver.find_element(By.CSS_SELECTOR, AllVariables.currency)
        select_currency = Select(currency_dropdown)
        select_currency.select_by_visible_text("EUR")
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, "//input[@value='stripe']").click()
        self.driver.find_element(By.CSS_SELECTOR, "#stripe-button").click()
        self.driver.find_element(By.CSS_SELECTOR, "#stripe-card-email").send_keys("test@test.com")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(ec.visibility_of_element_located("//iframe[@title='Secure card payment input frame']"))
        self.driver.find_element((By.XPATH, "//iframe[@title='Secure card payment input frame']")).click()
        self.driver.find_element((By.XPATH, "//iframe[@title='Secure card payment input frame']")).send_keys(
            "4242 4242 4242 4242")




