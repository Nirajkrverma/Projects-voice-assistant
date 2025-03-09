from selenium import webdriver
from selenium.webdriver.common.by import By


class News:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_news(self,query):
        self.query=query
        # Open Google News
        self.driver.get(url="https://news.google.com/"+query)

        # Find the first news headline and click it
        first_headline = self.driver.find_element(By.XPATH, '(//h3)[1]')
        first_headline.click()
        input("Press Enter to close the browser...")



