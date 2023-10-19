from selenium.webdriver.common.by import By
from time import sleep

class MyNavigationBar():
    def __init__(self, driver):
        self.driver = driver

    def fill_search_field_element(self, text):
        searchFieldElement = self.driver.find_element(By.ID, "twotabsearchtextbox")
        searchFieldElement.clear()
        searchFieldElement.send_keys(text)

    def click_to_search_button(self):
        searchButtonElement = self.driver.find_element(By.ID, "nav-search-submit-button")
        searchButtonElement.click()


    def click_to_the_searched_first_product(self):
        selectSearchedFirstElement = self.driver.find_element(By.XPATH, "//div[@class='a-section aok-relative s-image-fixed-height'][1]")
        selectSearchedFirstElement.click()


    def click_to_add_to_cart_button(self):
        addToCartButtonElement = self.driver.find_element(By.ID, "add-to-cart-button")
        addToCartButtonElement.click()

    def click_to_cart_button(self):
        cartButtonElement=self.driver.find_element(By.ID, "nav-cart-text-container")
        cartButtonElement.click()
