import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base




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
        for element in elements[:3]:
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
        print('Старт корзины')
        self.addBasket()
        self.inBasket()




