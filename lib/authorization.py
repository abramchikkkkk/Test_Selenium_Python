from selenium.webdriver.common.by import By

base_url = 'https://www.saucedemo.com/'

standard_user = 'standard_user'
login_negative = 'qwreethj'
locked_out_user = 'locked_out_user'
problem_user = 'problem_user'
performance_glitch_user = 'performance_glitch_user'
password_valid = 'secret_sauce'
password_negative = 'briewuv'

class Authorization:
    @staticmethod
    def authorization(driver, login, password):
        driver.get(base_url)
        user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')
        user_name.send_keys(login)
        password_add = driver.find_element(By.XPATH, '//*[@id="password"]')
        password_add.send_keys(password)
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_button.click()

    @staticmethod
    def standard_user(driver):
        Authorization.authorization(driver=driver, login=standard_user, password=password_valid)

    @staticmethod
    def locked_out_user(driver):
        Authorization.authorization(driver=driver, login=locked_out_user, password=password_valid)

    @staticmethod
    def problem_user(driver):
        Authorization.authorization(driver=driver, login=problem_user, password=password_valid)

    @staticmethod
    def performance_glitch_user(driver):
        Authorization.authorization(driver=driver, login=performance_glitch_user, password=password_valid)

    @staticmethod
    def login_negative(driver):
        Authorization.authorization(driver=driver, login=login_negative, password=password_valid)

    @staticmethod
    def password_negative(driver):
        Authorization.authorization(driver=driver, login=standard_user, password=password_negative)
