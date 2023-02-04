import time
import os
import pickle
import re

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup as bs

from loader import USERNAME, PASSWORD
from fake_useragent import UserAgent

def get_browser(url):
    start = time.time()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=793,1100");
    driver = webdriver.Chrome("chromedriver", options=options)
    with driver as browser:
        browser.get(url)
        for coockie in pickle.load(open('test', 'rb')):
            browser.add_cookie(coockie)
        browser.refresh()
        name_book = WebDriverWait(
                driver=browser, 
                timeout=5
                ).until(
                    EC.presence_of_element_located(
                        (By.XPATH, 
                        '//*[@id="__next"]/div/section/div[1]/div[3]/div[1]/div/div/div[3]/div/h1')
                        )
                        ).text
        name_book = name_book.replace(" ", "_").split(".")[0]
        dir = os.makedirs(name_book, exist_ok=True)
        
        browser.get(url + "reader")

        body = WebDriverWait(
                driver=browser, 
                timeout=5
                ).until(
                    EC.presence_of_element_located(
                        (By.XPATH, 
                        '/html/body')
                        )
                        )
        
        page_source = browser.page_source
        soup = bs(page_source, 'html.parser')
        data = []
        count_page = soup.find("div", class_="rdr-nav-pages").find_all("em")
        for integer in count_page:
            res = re.findall(r'\d+', integer.text)
            for r in res:
                data.append(int(r))
        if len(data) == 0:
            raise Exception("Не удалось найти страницы")           
        book = []
        page = 0
        while True:
            if len(data) == 4:
                new_data = []
                page_source = browser.page_source
                soup = bs(page_source, 'html.parser')
                count_page = soup.find("div", class_="rdr-nav-pages").find_all("em")
                
                for integer in count_page:
                    res = re.findall(r'\d+', integer.text)
                    for r in res:
                        new_data.append(int(r))                
                browser.save_screenshot(f"{name_book}/{page}.png")
                book.append(os.path.abspath(f"{name_book}/{page}.png"))
                if (new_data[0] != new_data[1]) or (new_data[2] != new_data[3]):
                    body.send_keys(Keys.RIGHT)
                    time.sleep(1)
                    page += 1
                    new_data = []
                else:
                    break
        # for page in range(int(count_page[1])):
        #     browser.save_screenshot(f"{name_book}/{page}.png")
        #     body.send_keys(Keys.RIGHT)
        #     time.sleep(1)
        #     book.append(os.path.abspath(f"{name_book}/{page}.png"))
        
        end = time.time() - start
        print(f"Книга в {len(book) + 1} страниц спарсена за {end / 60} минут")
        return {"book" : book, "name" : name_book}
    
    # element = driver.find_element(By.TAG_NAME, 'body')
    # element.screenshot("screenshot_full.png")
