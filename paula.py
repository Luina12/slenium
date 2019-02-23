# -*- coding: utf-8 -*-
# Zaimportowanie bibliotek
from selenium import webdriver
import time
#nowy sterownik chrome
driver = webdriver .Chrome()
#Maksimalizuj okno
driver.maximize_window()
#ide do strony web
driver.get ('http://www.wsb.pl')
#wyswietl tytul strony
print(driver.title)
#Poczekaj 5 sekund
#Uwaga!!
time.sleep(5)
#zamknij
driver.quit()
