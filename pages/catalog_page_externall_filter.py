import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base



class Catalog_Page_External_filter(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    minPrice="//Input[@name='minPrice']"
    maxPrice="//Input[@name='maxPrice']"
    filterMinMax="//span[contains(text(),'Сначала популярные')]"
    filterMin="//div[contains(text(),'Сначала дешевле')]"
    filterMax="//div[contains(text(),'Сначала дороже')]"
    allBlocks='//div[@class="product-cards-layout product-cards-layout--list"]'
    firstLastBlocks = "//div[@class='product-cards-layout__item ng-star-inserted']"

    firstPrice=0 #первая цена сначала дешевле
    secondPrice=0 #вторая цена сначала дороже

    def putPrice(self):
        print('Устанавливаю мин и макс сумму')
        min= WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.minPrice)))
        max= WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.maxPrice)))
        min.send_keys('34000')
        max.click()
        time.sleep(1)
        max.click()
        max.clear()
        max.send_keys('40000')
        min.click()

        print('Выборка обновилась')


    def comparison(self): #for getMinMax
        find = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.allBlocks)))  # для ожидания появления
        elements = self.driver.find_elements(By.XPATH, self.firstLastBlocks)  # ищем первый элемент и последний в списке
        mass = []
        for element in elements:
            text = element.text
            mass.append(text)
            print(text)
        if mass[0].split('\n')[0] =='Нет в наличии':
            print('Элемента нет в наличии')
            third_line=0
            return third_line
        else:
            third_line = mass[0].split('\n')[10].replace(' ₽', '').replace(' ', '')  # получаю стоимость первого элемента
            if "Бонусных" in third_line: #на случай если появится бонусная строка - доп проверка
                third_line = mass[0].split('\n')[9].replace(' ₽', '').replace(' ', '')  # получаю стоимость первого элемента
                return third_line
            return third_line

    def getMinMax(self):
        print('Устанавливаю фильтр "Сначала дешевле/дороже"')
        self.driver.refresh()
        MinMax=WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.filterMinMax)))
        time.sleep(0.5)
        MinMax.click()
        min=WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.filterMin)))
        min.click()
        self.firstPrice = self.comparison()
        MinMax.click()
        max=WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.filterMax)))
        max.click()
        self.secondPrice = self.comparison()
        print(self.firstPrice ,' Самая маленькая цена')
        print(self.secondPrice, ' Самая большая цена')

        try:
            assert int(self.firstPrice) < int(self.secondPrice)
            print('Фильтр "Сначала дешевле/дороже" работает')
        except AssertionError as EX:
            print(EX)
            print('Проблема с фильтрами "Сначала дешевле/дороже"')








    def go_ExternalFilter(self):
        print('Старт внешних фильтров')
        self.scroll_down(200)
        self.putPrice() #стоимость от и до
        self.getMinMax()

        print('Внутренние фильтры отработали')

