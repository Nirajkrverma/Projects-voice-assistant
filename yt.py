from selenium import webdriver
from selenium.webdriver.common.by import By


class Music():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)

        # Update to use 'find_element' with 'By.XPATH'
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        video.click()
