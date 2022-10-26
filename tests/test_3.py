import time
import pytest
from selenium.webdriver.common.by import By
from lib.screenschoter import Screenshot
from lib.authorization import Authorization


@pytest.mark.usefixtures('chrome_headless')
class Test_111:
    def test_adding_to_cart(self):
        """
        adding and removing a product from the shopping cart
        """
        driver = self.driver
        Authorization.standard_user(driver)
        add_to_cart = driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
        add_to_cart.click()
        go_to_cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        go_to_cart.click()
        Screenshot.screen(driver, "test_adding_to_cart")
        remove_product = driver.find_element(By.XPATH, "//button[@data-test='remove-sauce-labs-backpack']")
        remove_product.click()

    def test_menu(self):
        driver = self.driver
        Authorization.standard_user(driver)
        menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
        menu.click()
        time.sleep(2)
        Screenshot.screen(driver, "test_menu")
        about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
        about.click()
        time.sleep(2)
        Screenshot.screen(driver, "test_menu2")
