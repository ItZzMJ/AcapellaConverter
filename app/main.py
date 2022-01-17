import os
import time
from pprint import pprint
import requests
from selenium import webdriver
import page
from MailClass import MailClass
from webdriver_manager.chrome import ChromeDriverManager


CHROMEPATH = "/usr/bin/chromedriver"  # chromedriver path
BASEDIR = "/home/jannik/Musik/NeueTracks/ConvertToAcapellas"  # dir were the music to convert is
DOWNLOADPATH = "/home/jannik/Musik/NeueTracks/Acapellas"  # target dir for Acapellas

HIDECHROME = False  # wether the process in chrome browser is shown or not


class Main:
    def __init__(self):
        self.mailer = MailClass()

        self.create_browser()

        self.url = "https://www.lalal.ai/"

    def convert(self, file):
        driver = self.driver

        driver.get(self.url)
        main_page = page.MainPage(self.driver)

        main_page.select_file(file)

        main_page.wait_for_processing()

        main_page.click_process_file()

        main_page.enter_email(self.mailer.getMail())

        main_page.click_submit_button()

        while True:
            content = self.mailer.checkMails()
            if content is not None:
                break
            else:
                time.sleep(5)

        splitted_content = content.split()

        link = None

        for line in splitted_content:
            if "https://www.lalal.ai/" in line and "/?token=" in line:
                link = line
                print("Link found " + line + "\n")
                break

        if link is not None:
            driver.get(link)
        else:
            print("No link found in Email")
            exit(-1)

        process_page = page.ProcessingPage(self.driver)

        process_page.click_process_entire_file()

        process_page.wait_for_processing_to_finish()

        dl_link = process_page.get_dl_link()

        driver.get(dl_link)

        print("Download Finished!")

    def rename_files(self):
        time.sleep(10)  # wait for download to finish
        print("Renaming files..")

        files = os.listdir(DOWNLOADPATH)
        os.chdir(DOWNLOADPATH)
        for file in files:
            if "_vocals_splitted_by_lalalai" in file:
                print(file)
                os.rename(file, file.replace("_vocals_splitted_by_lalalai", " (Acapella)"))

        print("Finished Fasching Mafensen!!")

    def create_browser(self):
        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": DOWNLOADPATH}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--incognito")
        # options.add_argument("--user-agent=" + ua)
        # options.add_argument("--window-size=" + res)
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("--disable-notifications")
        options.add_argument('--disable-dev-shm-usage')

        if HIDECHROME:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        self.driver.set_window_position(1000, 0)
        self.driver.maximize_window()

    def run(self):
        files = os.listdir(BASEDIR)
        for file in files:
            print("Converting " + file)
            self.convert(os.path.join(BASEDIR, file))
            time.sleep(3)

            # move base file
            os.rename(os.path.join(BASEDIR, file), os.path.join(DOWNLOADPATH, file))

            self.mailer.deleteMail()
            self.mailer = MailClass()
            self.driver.quit()
            self.create_browser()

        self.rename_files()

    def tearDown(self):
        print("Cleaning up..")
        self.driver.quit()
        self.mailer.deleteMail()


if __name__ == "__main__":
    x = Main()
    try:
        x.run()
    finally:
        x.tearDown()
