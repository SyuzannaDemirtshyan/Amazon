from selenium import webdriver
from pages_.group1Work import AmazonLoginPage
from pages_.BasePage import BasePage

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

logInPageObject = AmazonLoginPage(driver)
logInPageObject.fill_username_field_for_amazon("syuzannademirtshyan@gmail.com")
logInPageObject.click_to_continue_button()
logInPageObject.fill_password_field_for_amazon("Adriana2023*")
logInPageObject.click_to_sign_in_button()


driver.close()
