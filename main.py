import time
import os
import pickle

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from loader import USERNAME, PASSWORD
from mybook.coockies import Coockie
from mybook.get_page import get_browser
from mybook.format import Formatter


def main():
    # Coockie.create_coocke_mybook()
    book = get_browser("")
    pdfs = Formatter.convert_png_to_pdf(book["book"])
    Formatter.create_book(pdfs, book["name"])

if __name__ == "__main__":
    main()