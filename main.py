#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os

# Opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--disable-notifications')

driverPath = './chromedriver'

driver = webdriver.Chrome(driverPath, options=options)

# Iniciar navegador
driver.get('https://www.grupobancolombia.com/personas/usados-bancolombia')

print('[ESPERANDO 10 SEGUNDOS ...]')
time.sleep(10)

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="type-goods"]/div/div[1]/span')))\
    .click()

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-option-1031"]/span')))\
    .click()

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="goods"]/div/div[1]/span')))\
    .click()

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-option-1035"]/span')))\
    .click()

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-search-goods"]')))\
    .click()\

print('[ESPERANDO 10 SEGUNDOS DE CARGA...]')
time.sleep(10)

locations = driver.find_elements_by_class_name('location')

# Imprime la localizacion de los aptos de bancolombia
for location in locations:
    print(location.text)