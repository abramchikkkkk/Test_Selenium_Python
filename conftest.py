import pytest
from os import path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope='class')
def chrome(request):
    sc = webdriver.chrome.service.Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=sc, options=options)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.quit()

@pytest.fixture(scope='class')
def chrome_headless(request):
    sc = webdriver.chrome.service.Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(service=sc, options=options)
    request.cls.driver = driver

    yield driver
    driver.quit()

@pytest.fixture(scope='class')
def firefox(request):
    sf = webdriver.firefox.service.Service(GeckoDriverManager().install(), log_path=path.devnull)
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=sf, options=options)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.quit()

@pytest.fixture(scope='class')
def firefox_headless(request):
    sf = webdriver.firefox.service.Service(GeckoDriverManager().install(), log_path=path.devnull)
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(service=sf, options=options)
    request.cls.driver = driver

    yield driver
    driver.quit()

@pytest.fixture(scope='class')
def edge(request):
    se = webdriver.edge.service.Service(EdgeChromiumDriverManager().install())
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=se, options=options)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.quit()

@pytest.fixture(scope='class')
def edge_headless(request):
    se = webdriver.edge.service.Service(EdgeChromiumDriverManager().install())
    options = webdriver.EdgeOptions()
    options.add_argument('--headless')
    options.add_argument('disable-gpu')
    driver = webdriver.Edge(service=se, options=options)
    request.cls.driver = driver

    yield driver
    driver.quit()
