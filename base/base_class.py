from fake_useragent import UserAgent
import time

class Base():
    def __init__(self,driver):
        self.driver=driver

    urlStart='https://www.mvideo.ru/'
    urlNoteBooks='https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?from=under_search'




    '''Method current url'''
    def get_current_url(self):
        get_url=self.driver.current_url
        print('Current url ' + get_url)
        return get_url


    def asser_word(self,word,result):
        value_word = word.text
        assert value_word==result
        print('Good value word')

    def asser_url(self,result):
        value_word = self.get_current_url()
        assert value_word==result
        print('Good value url')


    '''Scroll'''
    def scroll_down(self,size):
        time.sleep(1)
        self.driver.execute_script(f"window.scrollTo(0, {size});")