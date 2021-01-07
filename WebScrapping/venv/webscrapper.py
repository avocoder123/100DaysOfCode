import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome(executable_path='/Users/dishapatel/Downloads/chromedriver.exe')
driver.get('https://www.marketwatch.com/investing/stock/live')
results = []
content = driver.page_source
soup = BeautifulSoup(content)
for element in soup.findAll(attrs={'class': 'title'}): #iterate over all elements over parsed source file to find wanted attributes
    name = element.find('a')

#empty lists
company_name = []
company_ticker = []

