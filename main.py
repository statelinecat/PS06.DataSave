from selenium import webdriver
import time
import csv
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
url = 'https://sneakerhead.ru/shoes/sneakers/'
browser.get(url)
time.sleep(5)
print("Парсинг начался")
products = []

product_elements = browser.find_elements(By.CLASS_NAME, 'product-cards__item')

for product in product_elements:
    try:
        name_element = product.find_element(By.CLASS_NAME,'product-card__link').get_attribute('title')
        price_element = product.find_element(By.CSS_SELECTOR,'span.product-card__price-value').text
        link_element = product.find_element(By.CSS_SELECTOR,'a.product-card__link').get_attribute('href')
    except:
        print("произошла ошибка при парсинге")
        continue
    products.append([name_element, price_element, link_element])

browser.quit()

with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["название", "цена", "ссылка на товар"])
    writer.writerows(products)

print("Парсинг завершен. Файл products.csv создан.")

