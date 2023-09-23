import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base



class Main_Page(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    btnNotebooks='div.bottom-navbar-link:nth-child(3) > a:nth-child(1)' #css


    def get_btn_notebooks(self):
        find= WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,self.btnNotebooks)))
        find.click()

    def scroll_down(self): #скрол для следующего теста
        self.driver.execute_script("window.scrollTo(0, 10550);")

    def go_catalog(self):
        self.driver.get(self.urlStart)
        self.driver.maximize_window()
        self.get_current_url()
        print('Главная страница загружена')
        self.get_btn_notebooks()
        print('Перешел в раздел ноутбуки')
        self.asser_url(self.urlNoteBooks) #сравнию url и url ноутбуков


