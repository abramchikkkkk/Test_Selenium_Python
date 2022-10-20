from os import path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class browser(object):
    select_driver = 11
    """
    1 - Chrome    11 - Chrome headless
    2 - Firefox   22 - Firefox headless
    3 - Edge      33 - Edge headless
    """
    if select_driver == 1:
        sc = webdriver.chrome.service.Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=sc)
        driver.maximize_window()
    if select_driver == 2:
        sf = webdriver.firefox.service.Service(GeckoDriverManager().install(), log_path=path.devnull)
        driver = webdriver.Firefox(service=sf)
        driver.maximize_window()
    if select_driver == 3:
        se = webdriver.edge.service.Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=se)
        driver.maximize_window()
    if select_driver == 11:
        sc = webdriver.chrome.service.Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('disable-gpu')
        driver = webdriver.Chrome(service=sc, options=options)
        driver.maximize_window()
    if select_driver == 22:
        sf = webdriver.firefox.service.Service(GeckoDriverManager().install(), log_path=path.devnull)
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Firefox(service=sf, options=options)
    if select_driver == 33:
        se = webdriver.edge.service.Service(EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        options.add_argument('disable-gpu')
        driver = webdriver.Edge(service=se, options=options)
