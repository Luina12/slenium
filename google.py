#-*- coding: utf-8-*-
import unittest
from selenium import webdriver
from time import sleep

class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window
        self.driver.get("https://wizzair.com/pl-pl#/")

    def testDown(self):
        self.driver.quit()


    def test_wrong_email(self):
        zaloguj_btns= self.driver.find_elements_by_tag_name('button')

    #def test_search(self):
        #driver = self.driver
        #driver.get('http://www.google.pl')
        #input = driver.find_element_by_name("q")
        #input.send_keys('tester wsb katowice')
        #sleep(3)



if __name__ == '__main__':
    unittest.main()
