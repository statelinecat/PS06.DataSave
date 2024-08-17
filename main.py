import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "https://www.divan.ru/category/divany-i-kresla"
driver.get(url)
time.sleep(5)

divans = driver.find_elements(By.CLASS_NAME, '_Ud0k U4KZV')
print(divans)
parsed_data = []

for divan in divans:
    try:

        # name = divan.find_element(By.CSS_SELECTOR, 'span.name').text
        price = divan.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU KIkOH').text
        link = divan.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')

        print( price, link)

    except:
        print("произошла ошибка при парсинге")
        continue
    parsed_data.append({'Цена': price, 'ссылка на товар': link})

driver.quit()

with open("divans.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Цена', 'ссылка на товар'])
    writer.writerow(parsed_data)



