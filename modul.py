#-*- coding: utf-8-*-
import unittest
from selenium import webdriver
from time import sleep

class WsbTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    def testDown(self):
        self.driver.quit()

    def test_search(self):
        driver = self.driver
        input = driver.find_element_by_text("czym jest sukces")
        input.send_keys('tester wsb katowice')
        sleep(3)

if __name__ == '__main__':
    unittest.main()
