from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    SELECT_FILE_INPUT = (By.CLASS_NAME, "react_widget-input__element")
    SELECT_FREE_BUTTON = (By.CSS_SELECTOR, "body > main > section.promo.promo--styles.promo--first > div.promo__widget.promo__widget--second > div > div > div.widget-pay.widget-pay--styles.widget-pay--background > div > section.widget-pay-item.widget-pay-item--styles.widget-pay-item--gray > header > div.widget-pay-item__header_wrapper > div.widget-pay-item__header_block > h5")
    PROCESS_FILE_BUTTON = (By.CSS_SELECTOR, "body > main > section.promo.promo--styles.promo--first > div.promo__widget.promo__widget--second > div > div > div.widget-pay.widget-pay--styles.widget-pay--background > div > section.widget-pay-item.widget-pay-item--styles.widget-pay-item--gray > div > button")
    EMAIL_INPUT = (By.CSS_SELECTOR, "body > main > section.promo.promo--styles.promo--first > div.promo__widget.promo__widget--second > div > div > div.widget-pay.widget-pay--styles.widget-pay--background > div > section.widget-pay-item.widget-pay-item--styles.widget-pay-item--gray > div > form > div > input")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "body > main > section.promo.promo--styles.promo--first > div.promo__widget.promo__widget--second > div > div > div.widget-pay.widget-pay--styles.widget-pay--background > div > section.widget-pay-item.widget-pay-item--styles.widget-pay-item--gray > div > form > button")


class ProcessPageLocators(object):
    PROCESS_ENTIRE_FILE_BUTTON = (By.CSS_SELECTOR, "body > main > section.promo.promo--styles.promo--first > div.promo__widget.promo__widget--second > div > div > div.widget-pay.widget-pay--styles.widget-pay--background > section > button")
    DL_BUTTON = (By.CSS_SELECTOR, "body > main > section.promo.promo--styles.promo--first > div.promo__widget.promo__widget--second > div > div > div:nth-child(1) > footer > a")
    DL_BUTTON_SHADOW = (By.CSS_SELECTOR, "body > main > section.promo.promo--styles.promo--first > div.promo__widget.promo__widget--second > div > div > div:nth-child(1) > div")
    #body > main > section.promo.promo--styles.promo--first > div.promo__widget.promo__widget--second > div > div > div.widget-full-block.widget-full-block--styles > div > div





