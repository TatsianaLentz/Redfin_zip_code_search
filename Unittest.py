# Cross browser unittest for www.redfin.com
# Testing different zipcode input


import unittest
from selenium.webdriver.support.wait import WebDriverWait
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


def delay():
    time.sleep(random.randint(1, 3))


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

# As per unittest module, individual test should start with test_
    def test_zip_code_90077_SergioUS(self):
        driver = self.driver
        driver.get("https://www.redfin.com")
        time.sleep(3)

        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").click()
        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").send_keys("90077")
        driver.find_element(By.XPATH, "(//button[@tabindex='0'])[3]").click()
        time.sleep(4)

        try:
            assert "90077, CA Real Estate & Homes for Sale | Redfin" in driver.title
            print("Test result: Page title is OK: ", driver.title)
        except AssertionError:
            print("Test result: Page title is different", driver.title)

        try:
            assert "https://www.redfin.com/zipcode/90077" in driver.current_url
            print("Test result: Page url is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page url is different", driver.current_url)

        zipcode = driver.find_element(By.XPATH, "//p[contains(@class,'Tag__text')]").text

        try:
            assert zipcode == "90077"
            print("Current ZIP is OK: ", zipcode)
        except AssertionError:
            print("Current ZIP is NOT OK: ", zipcode)

        zip_text = driver.find_element(By.XPATH, "//h1[contains(@data-rf-test-id,'h1-header')]").text

        try:
            assert zip_text == "90077, CA homes for sale & real estate"
            print("Current ZIP-TEXT is OK: ", zip_text)
        except AssertionError:
            print("Current ZIP-TEXT is NOT OK: ", zip_text)

        driver.close()

    def test_zip_code_78257_TatsianaLentz(self):
        driver = self.driver

# Opening the Redfin site
        driver.get("https://www.redfin.com")
        time.sleep(3)

# Locating Search bar and entering zip code
        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").click()
        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").send_keys("78257")
        driver.find_element(By.XPATH, "(//button[@tabindex='0'])[3]").click()
        time.sleep(3)


# Verifying that title is correct
        try:
            assert "78257, TX Real Estate & Homes for Sale | Redfin" in driver.title
            print("Test result: Page title is OK: ", driver.title)
        except AssertionError:
            print("Test result: Page title is different", driver.title)

# Verifying that URL is correct
        try:
            assert "https://www.redfin.com/zipcode/78257" in driver.current_url
            print("Test result: Page url is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page url is different", driver.current_url)

# Verifying that zip code and text are displayed on the page
        zipcode = driver.find_element(By.XPATH, "//p[contains(@class,'Tag__text')]").text

        try:
            assert zip == "78257"
            print("Current ZIP is OK: ", zipcode)
        except AssertionError:
            print("Current ZIP is NOT OK: ", zipcode)

        zip_text = driver.find_element(By.XPATH, "//h1[contains(@data-rf-test-id,'h1-header')]").text

        try:
            assert zip_text == "78257, TX homes for sale & real estate"
            print("Current ZIP-TEXT is OK: ", zip_text)
        except AssertionError:
            print("Current ZIP-TEXT is NOT OK: ", zip_text)

        driver.close()

    def test_zip_code_33160_DmitryAntipenko(self):
        driver = self.driver
        driver.get("https://www.redfin.com")
        time.sleep(3)

# Identification of the website
        print(driver.title)
        print(driver.current_url)

        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").click()
        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").send_keys("33160")
        driver.find_element(By.XPATH, "(//button[@tabindex='0'])[3]").click()
        time.sleep(3)

        try:
            assert "33160, FL Real Estate & Homes for Sale | Redfin" in driver.title
            print("Test result: Page title is OK: ", driver.title)
        except AssertionError:
            print("Test result: Page title is different", driver.title)

        try:
            assert "https://www.redfin.com/zipcode/33160" in driver.current_url
            print("Test result: Page url is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page url is different", driver.current_url)

        zipcode = driver.find_element(By.XPATH, "//p[contains(@class,'Tag__text')]").text

        try:
            assert zipcode == "33160"
            print("Current ZIP is OK: ", zipcode)
        except AssertionError:
            print("Current ZIP is NOT OK: ", zipcode)

        zip_text = driver.find_element(By.XPATH, "//h1[contains(@data-rf-test-id,'h1-header')]").text
        try:
            assert zip_text == "33160, FL homes for sale & real estate"
            print("Current ZIP-TEXT is OK: ", zip_text)
        except AssertionError:
            print("Current ZIP-TEXT is NOT OK: ", zip_text)

        driver.close()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()

# As per unittest module, individual test should start with test_
    def test_zip_code_90077_SergioUS(self):
        driver = self.driver
        driver.get("https://www.redfin.com")
        time.sleep(3)

# Locating and closing popup window in iframe
        iframe = driver.find_element(By.XPATH, "//iframe[contains(@src, 'https://accounts.google.com/gsi/iframe/select')]")
        driver.switch_to.frame(iframe)
        driver.find_element(By.XPATH, '//*[@id="close"]').click()
        driver.switch_to.default_content()

        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").click()
        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").send_keys("90077")
        driver.find_element(By.XPATH, "(//button[@tabindex='0'])[3]").click()
        time.sleep(5)

        try:
            assert "90077, CA Real Estate & Homes for Sale | Redfin" in driver.title
            print("Test result: Page title is OK: ", driver.title)
        except AssertionError:
            print("Test result: Page title is different", driver.title)

        try:
            assert "https://www.redfin.com/zipcode/90077" in driver.current_url
            print("Test result: Page url is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page url is different", driver.current_url)

        time.sleep(3)

        zipcode = driver.find_element(By.XPATH, "//p[contains(@class,'Tag__text')]").text

        try:
            assert zip == "90077"
            print("Current ZIP is OK: ", zipcode)
        except AssertionError:
            print("Current ZIP is NOT OK: ", zipcode)

        zip_text = driver.find_element(By.XPATH, "//h1[contains(@data-rf-test-id,'h1-header')]").text

        try:
            assert zip_text == "90077, CA homes for sale & real estate"
            print("Current ZIP-TEXT is OK: ", zip_text)
        except AssertionError:
            print("Current ZIP-TEXT is NOT OK: ", zip_text)

        driver.close()

    def test_zip_code_78257_TatsianaLentz(self):
        driver = self.driver

# Opening the Redfin site
        driver.get("https://www.redfin.com")
        time.sleep(4)

# Locating and closing popup window in iframe
        iframe = driver.find_element(By.XPATH,
                                     "//iframe[contains(@src, 'https://accounts.google.com/gsi/iframe/select')]")

        driver.switch_to.frame(iframe)
        driver.find_element(By.XPATH, '//*[@id="close"]').click()

# Switching back to current window
        driver.switch_to.default_content()

# Locating Search bar and entering zip code
        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").click()
        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").send_keys("78257")
        driver.find_element(By.XPATH, "(//button[@tabindex='0'])[3]").click()
        time.sleep(4)

# Verifying that title is correct
        try:
            assert "78257, TX Real Estate & Homes for Sale | Redfin" in driver.title
            print("Test result: Page title is OK: ", driver.title)
        except AssertionError:
            print("Test result: Page title is different", driver.title)

# Verifying that URL is correct
        try:
            assert "https://www.redfin.com/zipcode/78257" in driver.current_url
            print("Test result: Page url is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page url is different", driver.current_url)

# Verifying that zip code and text are displayed on the page
        zipcode = driver.find_element(By.XPATH, "//p[contains(@class,'Tag__text')]").text

        try:
            assert zip == "78257"
            print("Current ZIP is OK: ", zipcode)
        except AssertionError:
            print("Current ZIP is NOT OK: ", zipcode)

        zip_text = driver.find_element(By.XPATH, "//h1[contains(@data-rf-test-id,'h1-header')]").text

        try:
            assert zip_text == "78257, TX homes for sale & real estate"
            print("Current ZIP-TEXT is OK: ", zip_text)
        except AssertionError:
            print("Current ZIP-TEXT is NOT OK: ", zip_text)

        driver.close()

    def test_zip_code_33160_DmitryAntipenko(self):
        driver = self.driver
        driver.get("https://www.redfin.com")

# Identification of the website
        print(driver.title)
        print(driver.current_url)
        time.sleep(4)
        iframe = driver.find_element(By.XPATH,
                                     "//iframe[contains(@src, 'https://accounts.google.com/gsi/iframe/select')]")

        driver.switch_to.frame(iframe)
        driver.find_element(By.XPATH, '//*[@id="close"]').click()
        driver.switch_to.default_content()

        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").click()
        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").send_keys("33160")
        driver.find_element(By.XPATH, "(//button[@tabindex='0'])[3]").click()
        time.sleep(5)

        try:
            assert "33160, FL Real Estate & Homes for Sale | Redfin" in driver.title
            print("Test result: Page title is OK: ", driver.title)
        except AssertionError:
            print("Test result: Page title is different", driver.title)

        try:
            assert "https://www.redfin.com/zipcode/33160" in driver.current_url
            print("Test result: Page url is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page url is different", driver.current_url)

        time.sleep(3)

        zipcode = driver.find_element(By.XPATH, "//p[contains(@class,'Tag__text')]").text

        try:
            assert zip == "33160"
            print("Current ZIP is OK: ", zipcode)
        except AssertionError:
            print("Current ZIP is NOT OK: ", zipcode)

        zip_text = driver.find_element(By.XPATH, "//h1[contains(@data-rf-test-id,'h1-header')]").text

        try:
            assert zip_text == "33160, FL homes for sale & real estate"
            print("Current ZIP-TEXT is OK: ", zip_text)
        except AssertionError:
            print("Current ZIP-TEXT is NOT OK: ", zip_text)

        driver.close()


class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()

# As per unittest module, individual test should start with test_
    def test_zip_code_90077_SergioUS(self):
        driver = self.driver
        driver.get("https://www.redfin.com")
        time.sleep(3)

        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").click()
        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").send_keys("90077")
        driver.find_element(By.XPATH, "(//button[@tabindex='0'])[3]").click()
        time.sleep(3)

        try:
            assert "90077, CA Real Estate & Homes for Sale | Redfin" in driver.title
            print("Test result: Page title is OK: ", driver.title)
        except AssertionError:
            print("Test result: Page title is different", driver.title)

        try:
            assert "https://www.redfin.com/zipcode/90077" in driver.current_url
            print("Test result: Page url is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page url is different", driver.current_url)

        zipcode = driver.find_element(By.XPATH, "//p[contains(@class,'Tag__text')]").text

        try:
            assert zip == "90077"
            print("Current ZIP is OK: ", zipcode)
        except AssertionError:
            print("Current ZIP is NOT OK: ", zipcode)

        zip_text = driver.find_element(By.XPATH, "//h1[contains(@data-rf-test-id,'h1-header')]").text

        try:
            assert zip_text == "90077, CA homes for sale & real estate"
            print("Current ZIP-TEXT is OK: ", zip_text)
        except AssertionError:
            print("Current ZIP-TEXT is NOT OK: ", zip_text)

        driver.close()

    def test_zip_code_78257_TatsianaLentz(self):
        driver = self.driver

# Opening the Redfin site
        driver.get("https://www.redfin.com")
        time.sleep(3)

# Locating Search bar and entering zip code
        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").click()
        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").send_keys("78257")
        driver.find_element(By.XPATH, "(//button[@tabindex='0'])[3]").click()
        time.sleep(4)

# Verifying that title is correct
        try:
            assert "78257, TX Real Estate & Homes for Sale | Redfin" in driver.title
            print("Test result: Page title is OK: ", driver.title)
        except AssertionError:
            print("Test result: Page title is different", driver.title)

# Verifying that URL is correct
        try:
            assert "https://www.redfin.com/zipcode/78257" in driver.current_url
            print("Test result: Page url is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page url is different", driver.current_url)

# Verifying that zip code and text are displayed on the page
        zipcode = driver.find_element(By.XPATH, "//p[contains(@class,'Tag__text')]").text

        try:
            assert zip == "78257"
            print("Current ZIP is OK: ", zipcode)
        except AssertionError:
            print("Current ZIP is NOT OK: ", zipcode)

        zip_text = driver.find_element(By.XPATH, "//h1[contains(@data-rf-test-id,'h1-header')]").text

        try:
            assert zip_text == "78257, TX homes for sale & real estate"
            print("Current ZIP-TEXT is OK: ", zip_text)
        except AssertionError:
            print("Current ZIP-TEXT is NOT OK: ", zip_text)

        driver.close()

    def test_zip_code_33160_DmitryAntipenko(self):
        driver = self.driver
        driver.get("https://www.redfin.com")
        time.sleep(3)

# Identification of the website
        print(driver.title)
        print(driver.current_url)

        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").click()
        driver.find_element(By.XPATH, "(//input[@type='search'])[1]").send_keys("33160")
        driver.find_element(By.XPATH, "(//button[@tabindex='0'])[3]").click()
        time.sleep(3)

        try:
            assert "33160, FL Real Estate & Homes for Sale | Redfin" in driver.title
            print("Test result: Page title is OK: ", driver.title)
        except AssertionError:
            print("Test result: Page title is different", driver.title)

        try:
            assert "https://www.redfin.com/zipcode/33160" in driver.current_url
            print("Test result: Page url is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page url is different", driver.current_url)

        zipcode = driver.find_element(By.XPATH, "//p[contains(@class,'Tag__text')]").text

        try:
            assert zipcode == "33160"
            print("Current ZIP is OK: ", zipcode)
        except AssertionError:
            print("Current ZIP is NOT OK: ", zipcode)

        zip_text = driver.find_element(By.XPATH, "//h1[contains(@data-rf-test-id,'h1-header')]").text

        try:
            assert zip_text == "33160, FL homes for sale & real estate"
            print("Current ZIP-TEXT is OK: ", zip_text)
        except AssertionError:
            print("Current ZIP-TEXT is NOT OK: ", zip_text)


def teardown(self):
    self.driver.quit()
