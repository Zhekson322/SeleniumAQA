import time

from fake_useragent import UserAgent

from pages.main_page import Main_Page
from pages.catalog_page_internal_filter import Catalog_Page_Internal_filter
from pages.catalog_page_externall_filter import Catalog_Page_External_filter
from pages.basket_page import BasketPage
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
import undetected_chromedriver as uc




def test_buy_notebooks():

    driver = uc.Chrome()
    driver.maximize_window()
    print('Start test')
    go=Main_Page(driver)
    go.go_catalog()

    print('Проверка внутренних фильтров')
    go= Catalog_Page_Internal_filter(driver)
    go.go_InternalFilter()


    go=Catalog_Page_External_filter(driver)
    go.go_ExternalFilter()

    go=BasketPage(driver)
    go.start()


    driver.close()