import datetime
from pathlib import PurePath

class Screenshot:
    @staticmethod
    def screen(driver, test_name):
        date_time = datetime.datetime.utcnow().strftime("%Y.%m.%d.-%H.%M.%S")
        name = f'screenschot_{test_name}_{date_time}.png'
        path = PurePath("test_results", " ")
        driver.save_screenshot(f"{path}{name}")
