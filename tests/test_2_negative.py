from selenium.webdriver.common.by import By
from lib.screenschoter import Screenshot
from lib.authorization import Authorization
from lib.driver import browser

driver = browser.driver


class Test_negative_authorization:
    def test_negative_login(self):
        """
        authorization with a negative login
        """
        Authorization.login_negative(driver)
        Screenshot.screen(driver, "negative_login")
        value_error = "Epic sadface: Username and password do not match any user in this service"
        value_test = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        value_test_text = value_test.text
        assert value_test_text == value_error
        print("ERROR gooD")

    def test_negative_password(self):
        """
        authorization with a negative password
        """
        Authorization.password_negative(driver)
        Screenshot.screen(driver, "negative_password")
        value_error = "Epic sadface: Username and password do not match any user in this service"
        value_test = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        value_test_text = value_test.text
        assert value_test_text == value_error
        print("ERROR gooD")
