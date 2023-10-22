from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages_.BasePage import BasePage


class AmazonLoginPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        pass

    def fill_username_field_for_amazon(self, username):
        usernameFieldElement = self._find_element(By.ID, "ap_email")
        self._fill_field(usernameFieldElement, username)

    def click_to_continue_button(self):
        continueButtonElement = self._find_element(By.ID, "continue")
        self._click(continueButtonElement)

    def fill_password_field_for_amazon(self, password):
        paswordFieldElement = self._find_element(By.ID, "ap_password")
        self._fill_field(paswordFieldElement, password)

    def click_to_sign_in_button(self):
        sleep(6)
        signInButtonElement = self._find_element(By.ID, "signInSubmit")
        self._click(signInButtonElement)
        sleep(6)

