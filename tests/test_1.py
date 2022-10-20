from selenium.webdriver.common.by import By
from lib.screenschoter import Screenshot
from lib.authorization import Authorization
from lib.driver import browser


driver = browser.driver


class Test_url:

    def test_url_verification_and_the_product_value(self):
        """
        checking the URL and the value of the product field
        """
        Authorization.standard_user(driver)
        Screenshot.screen(driver, "url_verification_and_the_product_value")
        text_products = driver.find_element(By.XPATH, '//span[@class="title"]')
        value_text_products = text_products.text
        print(value_text_products)
        assert value_text_products == "PRODUCTS"
        print("Значение верно")

        url_1 = 'https://www.saucedemo.com/inventory.html'
        get_url = driver.current_url
        print(get_url)
        assert get_url == url_1
        print("URL TRUE")
