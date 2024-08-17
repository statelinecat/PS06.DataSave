import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()





# Открытие страницы
url = "https://www.divan.ru/category/divany-i-kresla"
driver.get(url)

# Подождать, чтобы страница полностью загрузилась
time.sleep(5)

# Сбор информации о товарах
products = []
product_elements = driver.find_elements(By.CSS_SELECTOR, '.product-card')

for product in product_elements:
    try:
        name = product.find_element(By.CSS_SELECTOR, '.product-card').text
        price = product.find_element(By.CSS_SELECTOR, '.product-card__price-current').text
        link = product.find_element(By.CSS_SELECTOR, '.product-card__link').get_attribute('href')
        products.append({"название": name, "цена": price, "ссылка на товар": link})
    except Exception as e:
        print(f"Error occurred: {e}")

# Закрыть драйвер
driver.quit()

# Сохранение данных в CSV
df = pd.DataFrame(products)
df.to_csv('pp1.csv', index=False, encoding='utf-8-sig')

print("Данные успешно сохранены в products.csv")