import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base



class Catalog_Page_Internal_filter(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    btnShowFilter="//div[contains(text(),'Показать все фильтры')]" #поиск по тексту кнопки
    btnSSD="//div[contains(text(), 'Объем SSD')]"
    btnSSD512="//a[contains(@class, 'filter-name') and contains(., '512 ГБ')]"
    btnShowProducts=".filter-container__submit-btn > button:nth-child(1)" #css




    def get_btn_Filter(self):
        find= WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.btnShowFilter)))
        find.click()
        print('Нажата кнопка "Показать все фильтры"')

    def get_btn_SSD(self):
        time.sleep(0.5)
        find= WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.btnSSD)))
        find.click()
        print('Выбран чек бокс "SSD"')

    def get_btn_SSD512(self):
        time.sleep(0.5)
        find= WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.btnSSD512)))
        find.click()
        print('Выбран размер "SSD 512 ГБ"')

    def get_btn_ShowProducts(self):
        time.sleep(0.5)
        find= WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,self.btnShowProducts)))
        find.click()
        print('Нажата кнопка "Показать N товаров"')



    def go_InternalFilter(self):
        self.scroll_down(1550) #base
        self.get_btn_Filter()
        self.get_btn_SSD()
        self.get_btn_SSD512()
        self.get_btn_ShowProducts()
        print('Внутренние фильтры отработали')


