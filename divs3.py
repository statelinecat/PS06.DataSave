from selenium import webdriver
import time
import csv


browser = webdriver.Firefox()

# Открываем веб-страницу
url = 'https://www.divan.ru/category/divany-i-kresla'
browser.get(url)
time.sleep(5)  # Ждем загрузки страницы

products = []
# Используем CSS-селектор для поиска элементов
product_elements = browser.find_elements(By.CLASS_NAME, '_Ud0k') #(by_css_selector='_Ud0k')
print(product_elements)

for product in product_elements:
    name_element = product.find_element(by_css_selector='.lsooF')
    price_element = product.find_element(by_css_selector='.pY3d2')
    link_element = product.find_element(by_css_selector='.a')

    products.append([name_element.text, price_element.text, link_element.get_attribute('href')])

with open('products3.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["название", "цена", "ссылка на товар"])  # Запись заголовка
    writer.writerows(products)  # Запись строк

browser.quit()
