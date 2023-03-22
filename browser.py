from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(10)

    def close(self):
        self.driver.quit()