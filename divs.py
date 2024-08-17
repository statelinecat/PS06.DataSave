import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
driver = webdriver.Firefox()





# Открытие страницы
url = "https://www.divan.ru/category/divany-i-kresla"
driver.get(url)

# Подождать, чтобы страница полностью загрузилась
time.sleep(5)

# Сбор информации о товарах
products = []
product_elements = driver.find_elements(By.CLASS_NAME, '_Ud0k')
print(product_elements)
for product in product_elements:
    try:
        name = product.find_element(By.CSS_SELECTOR, 'lsooF').text
        price = product.find_element(By.CSS_SELECTOR, 'pY3d2').text
        link = product.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        # products.append({"название": name, "цена": price, "ссылка на товар": link})
    except Exception as e:
        print(f"Error occurred: {e}")

    products.append({"название": name, "цена": price, "ссылка на товар": link})

# Закрыть драйвер
driver.quit()

# Сохранение данных в CSV
with open("divs1.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['название', 'цена', 'ссылка на товар'])
    writer.writerows(products)

print("Данные успешно сохранены в divs1.csv")