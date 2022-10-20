import time
from selenium.webdriver.common.by import By
from lib.screenschoter import Screenshot
from lib.authorization import Authorization
from lib.driver import browser

driver = browser.driver

def authorization():
    Authorization.standard_user(driver)


class Test_smoke:
    def test_buy_product(self):
        """
         adding a product to the cart, placing an order
        """
        authorization()
        """info product1"""
        product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
        value_product1_name = product_1.text
        print(value_product1_name)

        product1_price = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
        value_product1_price = product1_price.text
        print(value_product1_price)
        Screenshot.screen(driver, "test_buy_product")
        time.sleep(1)

        add_to_cart = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        add_to_cart.click()
        Screenshot.screen(driver, "test_buy_product")
        time.sleep(1)
        cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        cart.click()

        """info product1 cart"""
        Screenshot.screen(driver, "test_buy_product")
        time.sleep(1)
        product_1_cart = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
        value_product1_name_cart = product_1_cart.text
        print(value_product1_name_cart)
        assert value_product1_name == value_product1_name_cart
        print("info product1 name good")

        product1_price_cart = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div["
                                                            "3]/div[2]/div[2]/div")
        value_product1_price_cart = product1_price_cart.text
        print(value_product1_price_cart)
        assert value_product1_price == value_product1_price_cart
        print("info product1 price good")

        checkout = driver.find_element(By.XPATH, "//button[@class='btn btn_action btn_medium checkout_button']")
        checkout.click()

        """select user info"""
        fist_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
        fist_name.send_keys("alex")
        last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
        last_name.send_keys("bey")
        postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
        postal_code.send_keys("bey_13r5")
        continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
        continue_button.click()

        """final chek product1"""
        Screenshot.screen(driver, "test_buy_product")
        product_1_final = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
        value_product1_name_final = product_1_final.text
        print(value_product1_name_final)
        assert value_product1_name == value_product1_name_final
        print("info product1 name final good")

        product1_price_final = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div["
                                                             "3]/div[2]/div[2]/div")
        value_product1_price_final = product1_price_final.text
        print(value_product1_price_final)
        assert value_product1_price == value_product1_price_final
        print("info product1 price final good")

        summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
        value_summary_price = summary_price.text
        print(value_summary_price)
        item_total = f"Item total: {value_product1_price_final}"
        assert item_total == value_summary_price
        print("info product1 price final_total good")
