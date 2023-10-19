from selenium import webdriver
from pages_.login import LoginPage
from pages_.myNavigation import MyNavigationBar
from pages_.myCart import MyCartPage

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get(
    "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

loginPageObj = LoginPage(driver)
loginPageObj.fill_username_field("syuzannademirtshyan@gmail.com")
loginPageObj.click_to_continue_button()
loginPageObj.fill_password_field("Adriana2023*")
loginPageObj.click_to_signin_button()

navigationBarObject = MyNavigationBar(driver)
navigationBarObject.fill_search_field_element("smart Case for Apple AirPods Max grey")
navigationBarObject.click_to_search_button()
navigationBarObject.click_to_the_searched_first_product()
navigationBarObject.click_to_add_to_cart_button()
navigationBarObject.click_to_cart_button()

cartPageObject = MyCartPage(driver)
cartPageObject.click_to_save_for_later_button()

navigationBarObject.click_to_cart_button()
cartPageObject.move_to_cart_saved_for_later_item()

navigationBarObject.click_to_cart_button()
cartPageObject.delete_first_product_from_cart()

driver.close()