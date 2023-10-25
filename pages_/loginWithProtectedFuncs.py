from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        pass

    def fill_username_field(self, username):
        usernameFieldElement = self._find_element(By.ID, "ap_email")
        self._fill_field(usernameFieldElement, username)

    def click_to_continue_button(self):
        continueButtonElement = self._find_element(By.ID, "continue")
        self._click(continueButtonElement)

    def fill_password_field(self, password):
        paswordFieldElement = self._find_element(By.ID, "ap_password")
        self._fill_field(paswordFieldElement, password)

    def click_to_sign_in_button(self):
        signInButtonElement = self._find_element(By.ID, "signInSubmit")
        self._click(signInButtonElement)

    def validate_continue_button_text(self):
        continueButtonElement=self._find_element(By.ID, "continue")
        if self._get_text(continueButtonElement) != "Continue":
            print("Error: Wrong continue button text")
            exit(2)