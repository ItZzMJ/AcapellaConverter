from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from math import ceil
from time import sleep
from locator import MainPageLocators, ProcessPageLocators
from selenium.webdriver.support import expected_conditions as EC

from element import BasePageElement

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def select_file(self, file):
        # file = "/home/jannik/Musik/NeueTracks#4/Acapellas/test.mp3"
        driver = self.driver

        elems = WebDriverWait(driver, 5).until(
            lambda driver: driver.find_elements(*MainPageLocators.SELECT_FILE_INPUT))

        elem = elems[0]

        if not elem.is_displayed():
            print("executing script")
            driver.execute_script("arguments[0].style.display = 'block';", elem)

        #print(elem.getAttribute("style"))

        elem.send_keys(file)

    def wait_for_processing(self):
        driver = self.driver
        elem = WebDriverWait(driver, 120).until(
            lambda driver: driver.find_element(*MainPageLocators.SELECT_FREE_BUTTON))

        print("Element found!")

        sleep(5)

        elem.click()

    def click_process_file(self):
        driver = self.driver
        elem = WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element(*MainPageLocators.PROCESS_FILE_BUTTON))

        print("Clicking Process Button")
        sleep(1)
        elem.click()

    def enter_email(self, email):
        driver = self.driver
        elem = WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element(*MainPageLocators.EMAIL_INPUT))

        print("Entering Email")

        elem.send_keys(email)

    def click_submit_button(self):
        driver = self.driver
        elem = WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element(*MainPageLocators.SUBMIT_BUTTON))

        print("Clicking Submit button")

        sleep(1)
        elem.click()


class ProcessingPage(BasePage):
    def click_process_entire_file(self):
        driver = self.driver
        elem = WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element(*ProcessPageLocators.PROCESS_ENTIRE_FILE_BUTTON))

        print("Clicking Process Entire File Button")

        sleep(1)
        elem.click()

    def wait_for_processing_to_finish(self):
        driver = self.driver

        print("Waiting for download button to be clickable")
        # elem = WebDriverWait(driver, 300).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "body > main > section.promo.promo--styles.promo--first > div.promo__widget.promo__widget--second > div > div > div:nth-child(1) > footer > a"))
        # )
        WebDriverWait(driver, 300).until(EC.invisibility_of_element_located(ProcessPageLocators.DL_BUTTON_SHADOW))

        print("Finished waiting")

    def get_dl_link(self):
        driver = self.driver

        elem = WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element(*ProcessPageLocators.DL_BUTTON)
        )

        link = elem.get_attribute("href")

        print("DL Link: " + link)

        return link



    #
    # def wait_for_processing_to_finish(self):
    #     driver = self.driver
    #
    #     WebDriverWait(driver, 5).until(
    #
    #     )


