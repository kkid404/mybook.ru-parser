import time
import os
import pickle

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from mybook.get_page import get_browser

from loader import USERNAME, PASSWORD
from fake_useragent import UserAgent

class Coockie:

    def create_coocke_mybook(book, url = "https://mybook.ru/"):
        useragent = UserAgent()
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        # options.add_argument(f"user-agent={useragent.random}")
        driver = webdriver.Chrome("chromedriver", options=options)
        with driver as browser:
            browser.get(url)

            login_btn = WebDriverWait(
                driver=browser, 
                timeout=5
                ).until(
                    EC.presence_of_element_located(
                        (By.XPATH, 
                        '/html/body/div[1]/div/div[1]/header/div/div[1]/div/div[5]/div/a')
                        )
                        )
            login_btn.click()
            
            input_email = WebDriverWait(
                driver=browser, 
                timeout=5
                ).until(
                    EC.presence_of_element_located(
                        (By.XPATH, 
                        '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div[1]/div/input')
                        )
                        )
            input_email.send_keys(USERNAME)

            input_password = WebDriverWait(
                driver=browser, 
                timeout=5
                ).until(
                    EC.presence_of_element_located(
                        (By.XPATH, 
                        '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/form/div[2]/div[2]/div[1]/div/span/input')
                        )
                        )
            input_password.send_keys(PASSWORD)

            login_btn = WebDriverWait(
                driver=browser, 
                timeout=5
                ).until(
                    EC.presence_of_element_located(
                        (By.XPATH, 
                        '/html/body/div[2]/div/div[2]/div/div[2]/div/div/button')
                        )
                        )
            login_btn.click()
            time.sleep(15)
            pickle.dump(browser.get_cookies(), open("test", "wb"))

            # get_browser(book, browser)

