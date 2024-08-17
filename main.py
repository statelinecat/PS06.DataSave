import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "https://www.divan.ru/category/divany-i-kresla"
driver.get(url)
time.sleep(30)
print("Скрипт запущен")
divans = browser.find_elements(By.CSS_SELECTOR, '._Ud0k')
print(divans)
parsed_data = []

for divan in divans:
    try:

        name = divan.find_element(By.CLASS_NAME, 'lsooF').text
        price = divan.find_element(By.CLASS_NAME, 'pY3d2').text
        link = divan.find_element(By.CLASS_NAME, 'a').get_attribute('href')

        print(link)

    except:
        print("произошла ошибка при парсинге")
        continue
    parsed_data.append({''

driver.quit()

with open("divans.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Ссылка'])
    writer.writerow(parsed_data)



