from selenium.webdriver.common.by import By


class CartPage():
    def __init__(self, driver):
        self.driver = driver

    def click_to_cart_button(self):
        cartButtonElement = self.driver.find_element(By.ID, "nav-cart-text-container")
        cartButtonElement.click()

    def click_to_compare_with_similar_items_button(self):
        compareWithSimilarItemsButtonElement = self.driver.find_element(By.XPATH, "//input[@value='Compare with similar items'][1]")
        compareWithSimilarItemsButtonElement.click()

    def close_compare_with_similar_items_page(self):
        closeCompareWithSimilarItemsButtonElement = self.driver.find_element(By.CLASS_NAME, "a-icon a-icon-close")
        closeCompareWithSimilarItemsButtonElement.click()

    def click_to_save_for_later_button(self):
        saveForLaterButtonElement = self.driver.find_element(By.XPATH, "//input[@value='Save for later'][1]")
        saveForLaterButtonElement.click()

    def move_to_cart_saved_for_later_item(self):
        moveToCartButtonElement = self.driver.find_element(By.ID, "a-autoid-6")
        moveToCartButtonElement.click()

    def delete_first_product_from_cart(self):
        firstProductDeleteButtonElement = self.driver.find_element(By.XPATH, "//input[@value='Delete'][1]")
        firstProductDeleteButtonElement.click()
