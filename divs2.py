from selenium import webdriver
import time
import csv


browser =  webdriver.Firefox()

# Open the webpage
url = 'https://www.divan.ru/category/divany-i-kresla'
browser.get(url)
time.sleep(5)  # Wait for the page to load

products = []
product_elements = browser.find_elements_by_class_name('_Ud0k')  # Adjust selector based on actual structure

for product in product_elements:
    name_element = product.find_element_by_class_name('lsooF')
    price_element = product.find_element_by_class_name('pY3d2')
    link_element = product.find_element_by_class_name('a')

    products.append([name_element.text, price_element.text, link_element.get_attribute('href')])

with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["название", "цена", "ссылка на товар"])  # Write header
    writer.writerows(products)  # Write rows

browser.quit()
