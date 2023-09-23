import time

from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import Main_Page
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from pages.catalog_page_internal_filter import Catalog_Page_Internal_filter
import undetected_chromedriver as uc
from base.base_class import Base

import json




useragent = UserAgent()

urlStart='https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?from=under_search'

# geckodriver_path = 'F:/learn/WorkProject/geckodriver.exe'
# geckodriver_log ='F:/learn/WorkProject/geckodriver.log'
# options=webdriver.FirefoxOptions()
# options.set_preference("general.useragent.override",useragent.firefox) #опция юзер агента
# service = Service(geckodriver_path ,log_output = open(geckodriver_log, "a+", encoding="utf-8"))
# driver = webdriver.Firefox(service=service,options=options)

driver=uc.Chrome()
driver.get(urlStart)

driver.maximize_window()


class BasketPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    addBasketUrl = "//span[contains(text(),'В корзину')]"
    inBasketUrl = "//p[contains(text(),'Корзина')]"
    count = "//mvid-bubble[contains(text(),3)]" #цифра на корзине
    goFinal="//div[contains(text(), 'Перейти к оформлению')]"
    goNext="//div[contains(text(), 'Продолжить')]"
    phoneNumber="//input[@type='tel']"
    tru="//h2[contains(text(), 'Подтверждение')]"

    def addBasket(self):
        basket = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.addBasketUrl)))  # для ожидания появления
        elements = self.driver.find_elements(By.XPATH, self.addBasketUrl)
        for element in elements[:4]:
            element.click()
            self.scroll_down(600)
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.count))) #когда в корзине будет 3 товара
        element.click() #переход в корзину



    def inBasket(self):
        final = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.goFinal)))
        final.click()
        phone=WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.XPATH,self.phoneNumber)))
        phone.click()
        phone.send_keys("1281111111")
        final = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.goNext)))
        final.click()
        successfully=WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.tru)))
        print(successfully.text)
        print('Номер успешно запрошен\n'
              'Тест завершен')



    def start(self):
        self.addBasket()
        self.inBasket()

go = BasketPage(driver)
go.start()

time.sleep(20)


